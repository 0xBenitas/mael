"""Code execution module — parse, write, and run code from LLM responses.

This is what makes MAEL real: the LLM proposes code, this module writes it
to disk and executes validation commands.
"""

import re
import subprocess
from pathlib import Path
from dataclasses import dataclass, field


@dataclass
class FileAction:
    """A file to create or modify."""
    path: str
    content: str


@dataclass
class ExecutionResult:
    """Result of executing LLM-proposed actions."""
    files_written: list[str] = field(default_factory=list)
    commands_run: list[dict] = field(default_factory=list)
    success: bool = True
    errors: list[str] = field(default_factory=list)


def parse_response(response: str) -> tuple[list[FileAction], list[str]]:
    """Parse an LLM response to extract files and commands.

    Expects format:
        ```path: some/file.py
        content here
        ```

        ### Commande de validation
        ```bash
        python -m pytest tests/
        ```

    Returns:
        (files, commands) — list of FileAction and list of shell commands.
    """
    files = []
    commands = []

    # Pattern 1: ```path: filepath\n...content...\n```
    file_pattern = re.compile(
        r"```(?:python|py)?\s*path:\s*(.+?)\n(.*?)```",
        re.DOTALL,
    )
    for match in file_pattern.finditer(response):
        filepath = match.group(1).strip()
        content = match.group(2)
        # Remove trailing whitespace but keep structure
        content = content.rstrip() + "\n"
        files.append(FileAction(path=filepath, content=content))

    # Pattern 2: ```bash\n...command...\n``` after "validation" or "commande"
    cmd_pattern = re.compile(
        r"```(?:bash|sh|shell)\n(.*?)```",
        re.DOTALL,
    )
    for match in cmd_pattern.finditer(response):
        cmd = match.group(1).strip()
        if cmd and _is_safe_command(cmd):
            commands.append(cmd)

    return files, commands


def apply_files(files: list[FileAction], base_dir: Path | None = None) -> list[str]:
    """Write parsed files to disk.

    Returns list of written file paths.
    """
    base = base_dir or Path(".")
    written = []

    for f in files:
        target = base / f.path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(f.content, encoding="utf-8")
        written.append(str(target))

    return written


def run_command(cmd: str, timeout: int = 60) -> dict:
    """Run a shell command safely with timeout.

    Returns dict with stdout, stderr, returncode, success.
    """
    try:
        result = subprocess.run(
            cmd, shell=True, capture_output=True, text=True,
            timeout=timeout, cwd=str(Path(".")),
        )
        return {
            "command": cmd,
            "stdout": result.stdout[-2000:],  # Limit output size
            "stderr": result.stderr[-1000:],
            "returncode": result.returncode,
            "success": result.returncode == 0,
        }
    except subprocess.TimeoutExpired:
        return {
            "command": cmd,
            "stdout": "",
            "stderr": f"Command timed out after {timeout}s",
            "returncode": -1,
            "success": False,
        }


def execute_response(response: str, base_dir: Path | None = None) -> ExecutionResult:
    """Full pipeline: parse response → write files → run commands.

    Returns ExecutionResult with all details.
    """
    files, commands = parse_response(response)
    result = ExecutionResult()

    # Write files
    if files:
        try:
            result.files_written = apply_files(files, base_dir)
        except Exception as e:
            result.errors.append(f"File write error: {e}")
            result.success = False

    # Run commands
    for cmd in commands:
        cmd_result = run_command(cmd)
        result.commands_run.append(cmd_result)
        if not cmd_result["success"]:
            result.errors.append(
                f"Command failed: {cmd}\n{cmd_result['stderr']}"
            )
            result.success = False

    return result


# ── Safety ───────────────────────────────────────────────────────────

# Commands that are never allowed
_BLOCKED_PATTERNS = [
    r"\brm\s+-rf\s+/",       # rm -rf /
    r"\brm\s+-rf\s+~",       # rm -rf ~
    r"\bmkfs\b",             # format disk
    r"\bdd\s+if=",           # disk destroyer
    r"\b:(){ :\|:& };:",     # fork bomb
    r"\bcurl\b.*\|\s*bash",  # pipe curl to bash
    r"\bwget\b.*\|\s*bash",  # pipe wget to bash
    r"\bsudo\b",             # no sudo
    r"\bchmod\s+777\b",      # world-writable
    r"\bgit\s+push\s+.*--force", # no force push
]


def _is_safe_command(cmd: str) -> bool:
    """Check if a command is safe to execute."""
    for pattern in _BLOCKED_PATTERNS:
        if re.search(pattern, cmd):
            return False
    return True
