# MAEL — Log des Mutations

> Journal des mutations méta-niveau : quand la boucle modifie
> ses propres prompts, critères d'évaluation, ou stratégies.

---

## Format

```
### Mutation #N — Iteration X — [TYPE]
**Cible** : quel prompt/critère a été muté
**Avant** : version précédente
**Après** : nouvelle version
**Raison** : pourquoi cette mutation
**Résultat** : impact observé (rempli après évaluation)
```

---

*Aucune mutation pour l'instant. La phase MUTER s'active toutes les 5 itérations.*

### Mutation #2 — Iteration 5 — prompt
**Cible** : ÉVALUER prompt
**Avant** : Évaluation générique sans contexte historique ni critères adaptatifs
**Après** : Phase ÉVALUER — Itération {iteration}

Tu évalues la solution de MAEL avec CONTEXTE HISTORIQUE.

## Historique des 3 dernières itérations
{recent_history}

## Tâche évaluée
ID: {task_id}
Titre: {task_title}
Critères: {criteria}

## Solution à évaluer
{solution}

## Instructions
1. Compare avec les patterns de réussite/échec passés
2. Évalue la cohérence avec l'apprentissage précédent
3. Score sur 100 avec justification détaillée
4. Identifie les points d'amélioration spécifiques

Réponds en JSON: {"score": X, "verdict": "SUCCESS|PARTIAL|FAIL", "reasoning": "...", "improvements": ["..."], "consistency_check": "..."
**Raison** : L'évaluateur manque de contexte historique, causant des scores incohérents
**Résultat** : *(en attente d'évaluation)*

### Mutation #3 — Iteration 5 — criteria
**Cible** : Seuils de verdict
**Avant** : Seuils fixes probablement inadaptés aux types de tâches
**Après** : SUCCESS: ≥80 (solution complète et robuste), PARTIAL: 50-79 (solution fonctionnelle avec lacunes), FAIL: <50 (solution non-fonctionnelle ou hors-sujet)
**Raison** : Les seuils actuels semblent trop permissifs, causant des verdicts PARTIAL fréquents
**Résultat** : *(en attente d'évaluation)*

### Mutation #4 — Iteration 5 — heuristic
**Cible** : Règle d'apprentissage
**Avant** : Apprentissage sans pondération par performance récente
**Après** : Pondérer les leçons par: score de l'itération (poids 0.4) + tendance sur 3 itérations (poids 0.3) + cohérence avec succès passés (poids 0.3). Ignorer les leçons d'itérations <40 points.
**Raison** : L'apprentissage actuel ne discrimine pas assez entre succès et échecs
**Résultat** : *(en attente d'évaluation)*

### Mutation #5 — Iteration 10 — heuristic
**Cible** : Règle d'apprentissage
**Avant** : Pondération complexe par score + tendance + cohérence, ignorant les leçons <40 points
**Après** : Apprentissage simple: garder uniquement les leçons des 3 dernières itérations SUCCESS (score ≥80). Si aucune SUCCESS récente, utiliser la dernière leçon PARTIAL (score ≥50). Reset complet si 3 FAIL consécutifs.
**Raison** : La pondération complexe crée une spirale négative. Retour à un apprentissage simple et stable.
**Résultat** : *(en attente d'évaluation)*

### Mutation #6 — Iteration 10 — prompt
**Cible** : Phase AGIR
**Avant** : Prompt standard sans garde-fou contre l'instabilité
**Après** : Phase AGIR — Itération {iteration} — Mode STABILISATION

Tu es MAEL en mode de récupération. IGNORE les leçons contradictoires. Concentre-toi sur:
1. Comprendre précisément la tâche
2. Appliquer une solution simple et directe
3. Vérifier ta logique avant de répondre

Si incertain, privilégie la simplicité sur la sophistication.
**Raison** : Le système a besoin d'un mode de récupération pour sortir de la spirale d'échec
**Résultat** : *(en attente d'évaluation)*
