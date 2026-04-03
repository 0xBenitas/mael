# Meta-Analyse : Auto-Prompting Autonome & Boucles Auto-Améliorantes

> **Projet MAEL** — Analyse exhaustive des algorithmes d'auto-amélioration de prompts,
> des plus académiques aux plus accessibles en "vibe coding".
> Objectif final : concevoir une boucle auto-améliorante pour Claude Code.

---

## Table des matières

1. [Vue d'ensemble & Taxonomie](#1-vue-densemble--taxonomie)
2. [Les Algorithmes Fondamentaux](#2-les-algorithmes-fondamentaux)
3. [Les Approches "Vibe Coding" Accessibles](#3-les-approches-vibe-coding-accessibles)
4. [Méta-Audit des Outils Disponibles](#4-méta-audit-des-outils-disponibles)
5. [Architecture Proposée : Boucle MAEL](#5-architecture-proposée--boucle-mael)
6. [Feuille de Route](#6-feuille-de-route)
7. [Sources](#7-sources)

---

## 1. Vue d'ensemble & Taxonomie

Les algorithmes d'auto-prompting se classent en **3 niveaux de récursivité** :

```
Niveau 0 : Optimisation statique
  └─ Un humain teste des prompts → garde le meilleur

Niveau 1 : Optimisation automatique (une boucle)
  └─ L'IA génère des variantes de prompt → évalue → sélectionne
  └─ Ex: APE, OPRO, DSPy

Niveau 2 : Auto-amélioration récursive (boucle de boucles)
  └─ L'IA améliore AUSSI le processus qui améliore les prompts
  └─ Ex: PromptBreeder (mutation des mutation-prompts)

Niveau 3 : Ouroboros / Méta-récursion complète
  └─ L'IA améliore ses propres critères d'évaluation,
     ses stratégies de mutation, ET ses prompts de tâche
  └─ Ex: Self-Improving Claude Code Bootstrap, Ralph Loop
```

### Matrice de comparaison rapide

| Technique | Niveau | Accessibilité | Compatible Claude | Open Source |
|-----------|--------|---------------|-------------------|-------------|
| APE | 1 | Moyenne | Oui | Oui |
| OPRO | 1 | Moyenne | Oui | Oui |
| Self-Refine | 1 | **Facile** | Oui | Oui |
| DSPy | 1-2 | Moyenne | Oui | Oui |
| PromptBreeder | 2 | Difficile | Oui (adapté) | Partiel |
| Ralph Loop | 2-3 | **Facile** | **Natif** | Oui |
| Bootstrap Seed | 3 | **Facile** | **Natif** | Oui (CC-BY) |
| Compounding Eng. | 2 | Moyenne | Adaptable | Oui |
| TextGrad | 1-2 | **Facile** | Oui (litellm) | Oui |
| GEPA (DSPy) | 2 | Moyenne | **Oui officiel** | Oui |
| EvoPrompt | 1 | Moyenne | Oui | Oui |
| Meta Prompting | 2 | Moyenne | Oui | Oui |
| STaR | 2 | Difficile | Non (fine-tune) | Oui |

### Classement par accessibilité "Vibe Coding" (du plus facile au plus dur)

| Rang | Technique | Difficulté | Pourquoi |
|------|-----------|------------|----------|
| 1 | **Self-Refine** | Trivial | Boucle generate-critique-refine en ~20 lignes |
| 2 | **TextGrad** | Facile | `pip install textgrad`, API style PyTorch |
| 3 | **Ralph Loop** | Facile | Un script bash + CLAUDE.md, c'est tout |
| 4 | **Bootstrap Seed** | Facile | Un prompt de 1400 tokens qui s'auto-configure |
| 5 | **DSPy + MIPROv2** | Facile/Moyen | `pip install dspy`, support Claude officiel |
| 6 | **GEPA (via DSPy)** | Moyen | `dspy.GEPA`, notebooks fournis, SOTA 2025 |
| 7 | **OPRO** | Moyen | Concept simple, facile à re-implémenter |
| 8 | **APE** | Moyen | Besoin d'exemples I/O + fonction d'évaluation |
| 9 | **EvoPrompt** | Moyen | Algorithme évolutionnaire + dev set |
| 10 | **PromptBreeder** | Difficile | Multi-population, coûteux en tokens |
| 11 | **STaR / RISE** | Difficile | Nécessite du fine-tuning, pas via API |

---

## 2. Les Algorithmes Fondamentaux

### 2.1 APE — Automatic Prompt Engineer
**Paper** : Zhou et al., 2023

**Comment ça marche** :
1. Donne des exemples input/output au LLM
2. Le LLM génère N candidats de prompts
3. Chaque candidat est évalué sur un jeu de test
4. Le meilleur prompt est sélectionné
5. Optionnel : itération avec les meilleurs candidats comme "parents"

**Force** : Simple, efficace, bien documenté
**Limite** : Optimise le prompt, pas le processus d'optimisation

---

### 2.2 OPRO — Optimization by PROmpting
**Paper** : Yang et al. (Google DeepMind), 2023

**Comment ça marche** :
1. Un "méta-prompt" contient l'historique des tentatives précédentes avec leurs scores
2. Le LLM joue le rôle d'optimiseur : il propose un nouveau prompt
3. Un scorer évalue le prompt sur la tâche cible
4. Le couple (prompt, score) est ajouté à la trajectoire
5. Répéter → le LLM apprend de la trajectoire

**Résultat marquant** : A découvert "Take a deep breath and work on this problem step-by-step" → 80.2% sur GSM8K

**Force** : Pas besoin de gradient, fonctionne en zero-shot
**Limite** : Convergence lente, sensible au méta-prompt initial

---

### 2.3 PromptBreeder — L'Ouroboros Académique
**Paper** : Fernando et al. (DeepMind), 2023 — ICLR 2024

**C'est l'algorithme le plus "Ouroboros" de la littérature.**

**Architecture à 3 niveaux** :
```
Niveau 3 : Hyper-mutation prompts
    ↓ mutent
Niveau 2 : Mutation-prompts (comment muter les task-prompts)
    ↓ mutent
Niveau 1 : Task-prompts (les prompts de travail)
    ↓ évalués sur
Niveau 0 : Jeu de données / tâche cible
```

**Opérateurs de mutation** :
- **Direct Mutation** : Le LLM mute un task-prompt guidé par un mutation-prompt
- **Estimation of Distribution** : Génère de nouveaux prompts à partir des meilleurs
- **Hypermutation** : Mute les mutation-prompts eux-mêmes
- **Lamarckian Mutation** : Rétro-propage la "pensée de travail" vers le prompt
- **Prompt Crossover** : Croise deux task-prompts performants

**Résultat** : 83.9% sur GSM8K (vs 80.2% pour OPRO) avec le prompt contre-intuitif "SOLUTION"

**Force** : Véritablement auto-référentiel — le serpent se mord la queue
**Limite** : Complexe à implémenter, coûteux en tokens

---

### 2.4 Self-Refine
**Paper** : Madaan et al., 2023

**Le plus simple des algorithmes d'auto-amélioration** :
```
Boucle :
  1. Générer une réponse
  2. Critiquer la réponse (même LLM ou différent)
  3. Raffiner la réponse en intégrant la critique
  4. Répéter jusqu'à satisfaction ou N itérations
```

**Force** : Trivial à implémenter, fonctionne sur n'importe quelle tâche
**Limite** : Pas d'amélioration du processus de critique lui-même

---

### 2.5 DSPy — Le Framework Programmatique
**Stanford NLP Group** — https://dspy.ai

**Paradigme** : Ne pas écrire des prompts, mais des **programmes** que DSPy compile en prompts optimaux.

**Concepts clés** :
- **Signature** : Déclaration input/output (`question -> answer`)
- **Module** : Technique de prompting (ChainOfThought, ReAct, etc.)
- **Optimizer** : Algorithme qui trouve les meilleurs prompts/exemples
  - `BootstrapFewShot` : Génère automatiquement des few-shot examples
  - `MIPROv2` : Optimise instructions + exemples simultanément
  - `BayesianSignatureOptimizer` : Exploration bayésienne de l'espace des prompts

**Pourquoi c'est puissant** :
```python
import dspy

class AnswerQuestion(dspy.Signature):
    """Répond à une question avec une explication."""
    question = dspy.InputField()
    answer = dspy.OutputField()

# DSPy optimise automatiquement le prompt
optimizer = dspy.MIPROv2(metric=my_metric, num_threads=4)
optimized = optimizer.compile(dspy.ChainOfThought(AnswerQuestion), trainset=data)
```

**Force** : Le plus mature, le plus utilisable en production
**Limite** : Nécessite un dataset d'évaluation

---

### 2.6 GEPA — Reflective Prompt Evolution (SOTA 2025)
**Paper** : Agrawal et al., 2025 — [arXiv:2507.19457](https://arxiv.org/abs/2507.19457)

**L'évolution la plus récente et la plus performante.**

Contrairement à MIPROv2 (recherche bayésienne), GEPA lit les **traces d'exécution complètes** (erreurs, logs de raisonnement, profiling) et utilise un LLM pour **diagnostiquer** pourquoi un candidat a échoué, puis propose des corrections ciblées.

```
Boucle GEPA :
  1. Exécuter le programme DSPy sur des exemples
  2. Analyser les traces d'erreur (pas juste le score)
  3. Diagnostiquer la cause racine comme un humain
  4. Proposer des mutations ciblées du prompt/programme
  5. Répéter
```

**Résultat** : 93% sur MATH (vs 67% avec ChainOfThought basique), surpasse GRPO de 6% en moyenne.
Disponible via `dspy.GEPA`.

---

### 2.7 TextGrad — Descente de Gradient en Langage Naturel
**Paper** : Yuksekgonul et al. (Stanford), 2024 — Publié dans **Nature** (2025)

**L'idée géniale** : Implémenter la rétro-propagation mais avec du texte au lieu de nombres.

```python
import textgrad as tg

# Exactement comme PyTorch, mais avec du texte
variable = tg.Variable("mon prompt initial", requires_grad=True)
loss = tg.TextLoss("Évalue la qualité de ce prompt")

# "Gradients textuels" = critique en langage naturel
loss.backward()  # → "Le prompt manque de spécificité sur X..."
optimizer.step()  # → applique la critique pour améliorer le prompt
```

**Force** : API familière pour les dev ML, `pip install textgrad`
**Résultat** : Pousse GPT-3.5 proche des performances de GPT-4 sur le raisonnement

---

### 2.8 EvoPrompt — Algorithmes Évolutionnaires pour Prompts
**Paper** : Guo et al., 2023 — [arXiv:2309.08532](https://arxiv.org/abs/2309.08532)

Applique des algorithmes génétiques (GA) et de l'évolution différentielle (DE) aux prompts :
- Population de prompts
- Crossover : le LLM croise deux prompts parents en un enfant cohérent
- Mutation : perturbation aléatoire
- Sélection : fitness sur un dev set

**Force** : Explore largement l'espace des solutions
**Limite** : Coûteux en évaluations, besoin d'un dev set

---

### 2.9 Meta Prompting & Récursivité
**Paper** : Suzgun & Kalai, 2023 — [arXiv:2311.11482](https://arxiv.org/abs/2311.11482)

Au lieu de donner des exemples spécifiques, on donne un **template structurel de pensée** applicable à toute une catégorie de tâches.

**Recursive Meta Prompting (RMP)** étend cela : le LLM génère des prompts, les évalue, accumule des stratégies d'édition, et raffine récursivement. Modélisé comme une **Writer Monad** — chaque itération transporte un log de transformations.

**Résultat** : Qwen-72B avec un seul meta-prompt atteint 46.3% sur MATH (vs 42.5% pour GPT-4)

---

## 3. Les Approches "Vibe Coding" Accessibles

### 3.1 Le "Ralph Loop" — La Boucle la Plus Simple

Popularisé par Geoffrey Huntley, c'est la version "vibe coding" d'une boucle auto-améliorante.

**Principe** : Un simple `while true` qui relance Claude Code avec un contexte persistant.

```bash
#!/bin/bash
# ralph.sh — La boucle la plus simple
while true; do
  claude --print --dangerously-skip-permissions \
    "Lis CLAUDE.md et progress.txt. Prends la prochaine tâche de prd.json.
     Implémente-la, teste-la, commite. Mets à jour progress.txt." \
    > progress.txt 2>&1

  if grep -q "ALL_TASKS_COMPLETE" progress.txt; then
    echo "Terminé !"
    break
  fi
done
```

**Fichiers nécessaires** :
- `CLAUDE.md` : Mémoire persistante (conventions, patterns, gotchas)
- `prd.json` : Liste de tâches avec statut
- `progress.txt` : Log chronologique

**Auto-amélioration** : L'agent met à jour `CLAUDE.md` avec ses apprentissages → les itérations suivantes sont meilleures.

**Implémentations notables** :
- [ralph-claude-code](https://github.com/frankbria/ralph-claude-code) — Version avec détection de sortie intelligente
- [continuous-claude](https://github.com/AnandChowdhary/continuous-claude) — Version avec création automatique de PRs

---

### 3.2 Bootstrap Seed — L'Auto-Configuration Évolutive

Par Christopher Allen (CC-BY-4.0) — Un prompt de ~1400 tokens qui bootstrappe un système complet.

**Les 4 phases** :

```
Session 1 : BOOTSTRAP
  → Identifie le cas d'usage
  → Crée .claude/learnings.md et .claude/rules/
  → Établit l'infrastructure d'auto-amélioration

Session 2+ : ÉVOLUTION
  → Réfléchit sur ce qui a marché/échoué
  → Trie : Appliquer maintenant / Capturer / Rejeter
  → Cascade les améliorations

TRIGGERS D'ÉVOLUTION :
  → Learning utilisé 2+ fois → promu en Rule
  → >30 learnings → consolidation par thème
  → >50 lignes de rules → split en process/requirements
```

**C'est du Niveau 3** car le système améliore ses propres critères de triage et ses règles d'évolution.

---

### 3.3 Compounding Engineering (DSPy local-first)

**Repo** : Strategic-Automation/dspy-compounding-engineering

Transforme un repo Git en environnement d'apprentissage persistant :

```bash
ce init --lm openai/gpt-5.2    # ou ollama pour du local
ce run                          # Cycle complet : review → triage → plan → learn
ce optimize my_module.py        # Optimisation ciblée
```

**Stockage** : FAISS/Chroma local (fonctionne offline)
**Auto-amélioration** : Les plans échoués deviennent des few-shot examples pour les prochaines tentatives

---

### 3.4 Le Pattern "Self-Improving Coding Agent" (Addy Osmani)

Architecture en 4 couches de mémoire :

| Couche | Fichier | Rôle |
|--------|---------|------|
| Historique | `git log` | Comprendre les changements passés |
| Progression | `progress.txt` | Suivi chronologique des tâches |
| État | `prd.json` | Statut de chaque requirement |
| Connaissance | `AGENTS.md` | Mémoire sémantique persistante |

**Patterns de qualité** :
- Tests après chaque tâche
- Halt on failure (l'agent doit fix avant de continuer)
- Max N tentatives avant de passer
- Stop conditions : max itérations, time limit, idle detection

**Scaling** : Modèle Planner-Worker-Judge
- Planner lit tout le codebase, spawne des tâches
- Workers implémentent en parallèle
- Judge évalue si l'objectif est atteint

---

## 4. Méta-Audit des Outils Disponibles

### Outils testés dans cette session

| Outil | Statut | Usage pour la Boucle MAEL |
|-------|--------|---------------------------|
| `Bash` | OK | Exécution de scripts, git, tests |
| `Read` | OK | Lecture de fichiers (code, config, logs) |
| `Write` | OK | Création de fichiers (prompts, configs) |
| `Edit` | OK | Modification chirurgicale de code |
| `Glob` | OK | Recherche de fichiers par pattern |
| `Grep` | OK | Recherche dans le contenu des fichiers |
| `WebSearch` | OK | Recherche web pour enrichir la boucle |
| `WebFetch` | OK | Extraction de contenu web détaillé |
| `Agent` (sub-agents) | OK | Parallélisation de tâches complexes |
| `TodoWrite` | OK | Suivi de progression structuré |
| `AskUserQuestion` | OK | Interaction guidée avec l'utilisateur |
| `Skill` (hooks) | Disponible | Configuration de hooks automatiques |

### Capacités critiques pour une boucle auto-améliorante

- **Persistance** : `Write` + `Edit` + Git → mémoire durable
- **Évaluation** : `Bash` (tests, linters) → scoring automatique
- **Recherche** : `WebSearch` + `WebFetch` → enrichissement externe
- **Parallélisme** : `Agent` → plusieurs sous-tâches simultanées
- **Interaction** : `AskUserQuestion` → human-in-the-loop quand nécessaire
- **Récursivité** : `/loop` skill → exécution récurrente

---

## 5. Architecture Proposée : Boucle MAEL

### Philosophie

**MAEL** = **M**éta-**A**mélioration **É**volutive en **L**igne

Combiner le meilleur de chaque approche :
- La **simplicité** du Ralph Loop
- La **persistance** du Bootstrap Seed
- La **rigueur** de Self-Refine
- L'**auto-référentialité** de PromptBreeder

### Architecture

```
┌─────────────────────────────────────────────────────┐
│                    BOUCLE MAEL                       │
│                                                      │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐       │
│  │  AGIR    │───→│ ÉVALUER  │───→│ APPRENDRE│       │
│  │          │    │          │    │          │       │
│  │ Exécute  │    │ Tests    │    │ Met à    │       │
│  │ la tâche │    │ Score    │    │ jour les │       │
│  │ courante │    │ Critique │    │ learnings│       │
│  └──────────┘    └──────────┘    └──────────┘       │
│       ↑                               │              │
│       │          ┌──────────┐         │              │
│       └──────────│  MUTER   │←────────┘              │
│                  │          │                         │
│                  │ Améliore │                         │
│                  │ le       │                         │
│                  │ processus│                         │
│                  └──────────┘                         │
│                                                      │
│  Fichiers persistants :                              │
│  ├── CLAUDE.md          (mémoire sémantique)         │
│  ├── .mael/state.json   (état des tâches)            │
│  ├── .mael/learnings.md (apprentissages)             │
│  ├── .mael/metrics.json (scores & métriques)         │
│  └── .mael/mutations.md (log des mutations)          │
└─────────────────────────────────────────────────────┘
```

### Les 4 Phases

#### Phase 1 : AGIR
```
- Lire .mael/state.json → identifier la tâche suivante
- Lire CLAUDE.md → charger le contexte accumulé
- Exécuter la tâche (code, refactor, fix, etc.)
- Git commit si modification
```

#### Phase 2 : ÉVALUER
```
- Exécuter les tests → score numérique
- Auto-critique : "qu'est-ce qui pourrait être amélioré ?"
- Comparer avec les métriques précédentes (.mael/metrics.json)
- Verdict : SUCCESS / PARTIAL / FAIL
```

#### Phase 3 : APPRENDRE
```
- Si SUCCESS : extraire le pattern → .mael/learnings.md
- Si FAIL : diagnostiquer → ajouter le gotcha
- Si pattern vu 2+ fois → promouvoir en règle CLAUDE.md
- Archiver les learnings obsolètes
```

#### Phase 4 : MUTER (le niveau Ouroboros)
```
- Toutes les N itérations (ex: 5) :
  - Analyser les métriques globales
  - "Est-ce que ma façon d'évaluer est bonne ?"
  - "Est-ce que mes critères d'apprentissage sont pertinents ?"
  - Muter les prompts de critique et d'évaluation
  - Logger la mutation dans .mael/mutations.md
```

### Implémentation minimale (v0)

```bash
#!/bin/bash
# mael-loop.sh — Boucle MAEL v0

ITERATIONS=0
MAX_ITERATIONS=50

while [ $ITERATIONS -lt $MAX_ITERATIONS ]; do
  ITERATIONS=$((ITERATIONS + 1))
  echo "=== MAEL Iteration $ITERATIONS ==="

  # Phase 1: AGIR
  claude --print \
    "Tu es dans la boucle MAEL, itération $ITERATIONS.
     Lis CLAUDE.md, .mael/state.json et .mael/learnings.md.
     Exécute la prochaine tâche. Commite tes changements.
     Mets à jour .mael/state.json." \
    2>&1 | tee .mael/logs/iter_${ITERATIONS}_act.log

  # Phase 2: ÉVALUER
  claude --print \
    "Phase ÉVALUER. Exécute les tests.
     Compare avec .mael/metrics.json.
     Écris le résultat dans .mael/metrics.json.
     Donne un verdict: SUCCESS/PARTIAL/FAIL." \
    2>&1 | tee .mael/logs/iter_${ITERATIONS}_eval.log

  # Phase 3: APPRENDRE
  claude --print \
    "Phase APPRENDRE. Lis le log d'évaluation.
     Extrais les learnings → .mael/learnings.md.
     Si un pattern apparaît 2+ fois, ajoute-le à CLAUDE.md.
     Mets à jour .mael/state.json." \
    2>&1 | tee .mael/logs/iter_${ITERATIONS}_learn.log

  # Phase 4: MUTER (toutes les 5 itérations)
  if [ $((ITERATIONS % 5)) -eq 0 ]; then
    claude --print \
      "Phase MUTER (méta-amélioration).
       Analyse les 5 dernières itérations dans .mael/logs/.
       Tes critères d'évaluation sont-ils pertinents ?
       Tes patterns d'apprentissage capturent-ils l'essentiel ?
       Propose des mutations. Log dans .mael/mutations.md." \
      2>&1 | tee .mael/logs/iter_${ITERATIONS}_mutate.log
  fi

  # Vérifier si toutes les tâches sont terminées
  if grep -q '"status": "all_complete"' .mael/state.json 2>/dev/null; then
    echo "=== MAEL : Toutes les tâches terminées ! ==="
    break
  fi
done

echo "=== MAEL terminé après $ITERATIONS itérations ==="
```

---

## 6. Feuille de Route

### Phase 0 — Maintenant (cette session)
- [x] Recherche et méta-analyse (11 techniques analysées)
- [x] Audit des outils disponibles (12 outils testés)
- [x] Architecture de la boucle MAEL
- [x] Créer la structure `.mael/` de base
- [x] Script `mael-loop.sh` v0.1
- [x] Templates : `CLAUDE.md`, `state.json`, `learnings.md`, etc.

### Phase 1 — Première Boucle (prochaine session)
- [ ] Remplir `state.json` avec des tâches concrètes
- [ ] Tester sur une tâche simple (ex: "crée un script Python qui...")
- [ ] Mesurer : nombre d'itérations, qualité, coût tokens
- [ ] Ajuster les prompts de phase selon les résultats

### Phase 2 — Auto-Amélioration
- [ ] Ajouter la phase MUTER
- [ ] Système de scoring automatique
- [ ] Promotion automatique learning → rule
- [ ] Dashboard de métriques

### Phase 3 — Ouroboros Complet
- [ ] Le système mute ses propres prompts de phase
- [ ] Intégration DSPy pour l'optimisation formelle
- [ ] Multi-agent (planner/worker/judge)
- [ ] Benchmarks comparatifs

---

## 7. Sources

### Papers académiques
- [APE: Automatic Prompt Engineer](https://arxiv.org/abs/2211.01910) — Zhou et al., 2023
- [OPRO: Optimization by PROmpting](https://arxiv.org/abs/2309.03409) — Yang et al. (DeepMind), 2023
- [PromptBreeder: Self-Referential Self-Improvement](https://arxiv.org/abs/2309.16797) — Fernando et al. (DeepMind), 2023
- [Self-Refine: Iterative Refinement with Self-Feedback](https://arxiv.org/abs/2303.17651) — Madaan et al., 2023
- [GEPA: Reflective Prompt Evolution](https://arxiv.org/abs/2507.19457) — Agrawal et al., 2025 **(SOTA)**
- [TextGrad: Automatic Differentiation via Text](https://arxiv.org/abs/2406.07496) — Yuksekgonul et al. (Stanford), 2024 — Publié dans *Nature* 2025
- [EvoPrompt: Evolutionary Prompt Optimization](https://arxiv.org/abs/2309.08532) — Guo et al., 2023
- [ProTeGi/APO: Automatic Prompt Optimization](https://aclanthology.org/2023.emnlp-main.494.pdf) — Pryzant et al., EMNLP 2023
- [Meta Prompting for AI Systems](https://arxiv.org/abs/2311.11482) — Suzgun & Kalai, 2023
- [STaR: Bootstrapping Reasoning With Reasoning](https://arxiv.org/abs/2203.14465) — Zelikman et al., 2022
- [RISE: Recursive Introspection](https://proceedings.neurips.cc/paper_files/paper/2024/file/639d992f819c2b40387d4d5170b8ffd7-Paper-Conference.pdf) — NeurIPS 2024
- [Efficient Prompting Methods for LLMs: A Survey](https://arxiv.org/html/2404.01077v2)

### Frameworks & outils
- [DSPy — Stanford NLP](https://github.com/stanfordnlp/dspy) — 16k+ stars, 160k downloads/mois
- [TextGrad](https://github.com/zou-group/textgrad) — Gradients textuels, API PyTorch-like
- [GEPA](https://github.com/gepa-ai/gepa) — SOTA prompt evolution via DSPy
- [EvoPrompt](https://github.com/beeevita/EvoPrompt) — Algorithmes évolutionnaires
- [AutoPrompt](https://github.com/Eladlev/AutoPrompt) — Calibration de prompts par intention
- [PromptWizard (Microsoft)](https://github.com/microsoft/PromptWizard) — Auto-évolution par feedback
- [Meta Prompting](https://github.com/meta-prompting/meta-prompting) — Templates structurels de pensée
- [Awesome LLM Prompt Optimization](https://github.com/jxzhangjhu/Awesome-LLM-Prompt-Optimization) — Liste curatée complète
- [DSPy Prompt Optimization Tutorial (2025)](https://www.pondhouse-data.com/blog/dspy-build-better-ai-systems-with-automated-prompt-optimization)
- [Compounding Engineering (DSPy Agent)](https://dev.to/dan-startegicauto/compounding-engineering-turn-your-repo-into-a-self-improving-dspy-agent-1e99)

### Implémentations pratiques Claude Code
- [Self-Improving Coding Agents — Addy Osmani](https://addyosmani.com/blog/self-improving-agents/) — Guide architectural complet
- [Ralph Claude Code](https://github.com/frankbria/ralph-claude-code) — Boucle autonome avec détection de sortie
- [Continuous Claude](https://github.com/AnandChowdhary/continuous-claude) — Boucle avec création automatique de PRs
- [Self-Improving Claude Code Bootstrap Seed](https://gist.github.com/ChristopherA/fd2985551e765a86f4fbb24080263a2f) — CC-BY-4.0
- [AutoResearch pour Claude Code](https://github.com/uditgoenka/autoresearch) — Pattern Karpathy : métrique → eval → itération
- [Recursive Self-Improvement with Claude Code](https://medium.com/@davidroliver/recursive-self-improvement-building-a-self-improving-agent-with-claude-code-d2d2ae941282)
- [Claude Code Loop: YOLO Mode](https://mfyz.com/claude-code-on-loop-autonomous-ai-coding/)

### Documentation officielle
- [How the Agent Loop Works — Claude API](https://platform.claude.com/docs/en/agent-sdk/agent-loop)
- [How Claude Code Works](https://code.claude.com/docs/en/how-claude-code-works)
