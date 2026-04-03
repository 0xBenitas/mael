#!/bin/bash
# =============================================================================
# MAEL Loop v0.1 — Méta-Amélioration Évolutive en Ligne
# =============================================================================
# Boucle auto-améliorante pour Claude Code
# Usage: ./mael-loop.sh [max_iterations]
# =============================================================================

set -euo pipefail

MAX_ITERATIONS=${1:-50}
ITERATIONS=0
MAEL_DIR=".mael"
LOG_DIR="$MAEL_DIR/logs"

# Couleurs
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

log() { echo -e "${BLUE}[MAEL]${NC} $1"; }
success() { echo -e "${GREEN}[MAEL ✓]${NC} $1"; }
warn() { echo -e "${YELLOW}[MAEL !]${NC} $1"; }
error() { echo -e "${RED}[MAEL ✗]${NC} $1"; }

# Vérifier la structure
if [ ! -d "$MAEL_DIR" ]; then
  error "Structure .mael/ non trouvée. Initialisez d'abord le projet."
  exit 1
fi

mkdir -p "$LOG_DIR"

log "Démarrage de la boucle MAEL (max: $MAX_ITERATIONS itérations)"
echo "================================================================="

while [ $ITERATIONS -lt $MAX_ITERATIONS ]; do
  ITERATIONS=$((ITERATIONS + 1))
  TIMESTAMP=$(date +%Y%m%d_%H%M%S)

  echo ""
  echo "================================================================="
  log "ITÉRATION $ITERATIONS / $MAX_ITERATIONS — $TIMESTAMP"
  echo "================================================================="

  # ── Phase 1 : AGIR ──────────────────────────────────────────────
  log "Phase 1/4 : AGIR"
  claude --print \
    "Tu es dans la boucle MAEL, itération $ITERATIONS.

     INSTRUCTIONS :
     1. Lis CLAUDE.md pour le contexte du projet
     2. Lis .mael/state.json pour la tâche courante
     3. Lis .mael/learnings.md pour les apprentissages passés
     4. Exécute la prochaine tâche non-complétée
     5. Git add + commit tes changements
     6. Mets à jour .mael/state.json (marque la tâche comme done)

     Si toutes les tâches sont terminées, écris ALL_TASKS_COMPLETE dans ta réponse." \
    2>&1 | tee "$LOG_DIR/iter_${ITERATIONS}_1_act.log"

  # Vérifier si terminé
  if grep -q "ALL_TASKS_COMPLETE" "$LOG_DIR/iter_${ITERATIONS}_1_act.log" 2>/dev/null; then
    success "Toutes les tâches sont terminées !"
    break
  fi

  # ── Phase 2 : ÉVALUER ──────────────────────────────────────────
  log "Phase 2/4 : ÉVALUER"
  claude --print \
    "Phase ÉVALUER — Itération $ITERATIONS de la boucle MAEL.

     INSTRUCTIONS :
     1. Lis le log de la phase AGIR : $LOG_DIR/iter_${ITERATIONS}_1_act.log
     2. Vérifie les changements : git diff HEAD~1 (si commit existe)
     3. Exécute les tests si disponibles
     4. Compare avec les métriques précédentes : .mael/metrics.json
     5. Donne un VERDICT : SUCCESS / PARTIAL / FAIL
     6. Attribue un SCORE de 0 à 100
     7. Ajoute l'entrée dans .mael/metrics.json" \
    2>&1 | tee "$LOG_DIR/iter_${ITERATIONS}_2_eval.log"

  # ── Phase 3 : APPRENDRE ────────────────────────────────────────
  log "Phase 3/4 : APPRENDRE"
  claude --print \
    "Phase APPRENDRE — Itération $ITERATIONS de la boucle MAEL.

     INSTRUCTIONS :
     1. Lis les logs des phases AGIR et ÉVALUER de cette itération
     2. Identifie les patterns : qu'est-ce qui a bien marché ? mal marché ?
     3. Ajoute les nouveaux learnings à .mael/learnings.md avec le format :
        ### [date] Iteration $ITERATIONS — [Catégorie]
        **Contexte** : ...
        **Learning** : ...
        **Confiance** : haute/moyenne/basse
        **Utilisations** : 0
     4. Vérifie si un learning existant a été réutilisé → incrémente son compteur
     5. Si un learning atteint 2+ utilisations → ajoute-le à CLAUDE.md
     6. Mets à jour .mael/state.json" \
    2>&1 | tee "$LOG_DIR/iter_${ITERATIONS}_3_learn.log"

  # ── Phase 4 : MUTER (toutes les 5 itérations) ──────────────────
  if [ $((ITERATIONS % 5)) -eq 0 ]; then
    warn "Phase 4/4 : MUTER (méta-amélioration)"
    claude --print \
      "Phase MUTER — Méta-amélioration, itération $ITERATIONS.

       C'est la phase OUROBOROS : tu améliores le processus lui-même.

       INSTRUCTIONS :
       1. Lis les 5 derniers logs dans .mael/logs/
       2. Lis .mael/metrics.json pour les tendances
       3. Analyse :
          - Les critères d'évaluation sont-ils pertinents ?
          - Les patterns d'apprentissage capturent-ils l'essentiel ?
          - Y a-t-il des angles morts dans le processus ?
       4. Propose des MUTATIONS concrètes :
          - Nouveaux critères d'évaluation
          - Meilleurs prompts pour les phases
          - Nouvelles heuristiques d'apprentissage
       5. Log chaque mutation dans .mael/mutations.md avec le format :
          ### Mutation #N — Iteration $ITERATIONS — [TYPE]
          **Cible** : ...
          **Avant** : ...
          **Après** : ...
          **Raison** : ...
       6. Applique les mutations approuvées" \
      2>&1 | tee "$LOG_DIR/iter_${ITERATIONS}_4_mutate.log"
  fi

  success "Itération $ITERATIONS terminée"
done

echo ""
echo "================================================================="
success "Boucle MAEL terminée après $ITERATIONS itérations"
echo "================================================================="
echo ""
log "Résumé disponible dans :"
log "  - Métriques : .mael/metrics.json"
log "  - Learnings : .mael/learnings.md"
log "  - Mutations : .mael/mutations.md"
log "  - Logs      : .mael/logs/"
