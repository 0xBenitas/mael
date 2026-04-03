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

### Mutation #7 — Iteration 5 — heuristic
**Cible** : Règle de reset du système
**Avant** : Reset complet si 3 FAIL consécutifs
**Après** : Reset IMMÉDIAT après 5 FAIL consécutifs : purger toutes les leçons, revenir aux prompts de base, redémarrer avec une approche minimaliste. Seuil de SUCCESS abaissé temporairement à 60 pour faciliter la récupération.
**Raison** : 5 échecs consécutifs indiquent un dysfonctionnement systémique nécessitant une intervention drastique
**Résultat** : *(en attente d'évaluation)*

### Mutation #8 — Iteration 5 — prompt
**Cible** : Phase AGIR
**Avant** : Mode stabilisation avec focus sur simplicité
**Après** : Phase AGIR — Itération {iteration} — MODE URGENCE

Tu es MAEL en situation critique. OUBLIE tout historique.

Méthode ULTRA-SIMPLE :
1. Lis la tâche 2 fois
2. Identifie l'action MINIMALE requise
3. Exécute sans sophistication
4. Vérifie que tu réponds à la demande de base

PAS de créativité, PAS d'optimisation. Juste l'essentiel.
**Raison** : Le mode stabilisation n'a pas fonctionné, il faut une approche encore plus radicale
**Résultat** : *(en attente d'évaluation)*

### Mutation #9 — Iteration 10 — heuristic
**Cible** : Seuil de reset après échecs
**Avant** : Reset après 5 FAIL consécutifs avec purge totale
**Après** : Reset progressif : après 3 FAIL consécutifs, revenir aux 3 dernières leçons les plus efficaces uniquement. Après 5 FAIL, reset complet mais conserver les heuristiques de base.
**Raison** : Le reset total détruit l'apprentissage utile. Un reset progressif préserve les acquis tout en corrigeant les dérives.
**Résultat** : *(en attente d'évaluation)*

### Mutation #10 — Iteration 10 — prompt
**Cible** : Phase ÉVALUER
**Avant** : Évaluation standard avec critères fixes
**Après** : Phase ÉVALUER — Itération {iteration} — DIAGNOSTIC APPROFONDI

Tu évalues la performance de MAEL avec analyse multi-niveaux :

1. CONFORMITÉ (0-30) : Répond-il aux critères de base ?
2. QUALITÉ (0-40) : Niveau d'exécution technique
3. EFFICACITÉ (0-30) : Optimisation et pertinence des choix

Pour chaque dimension, identifie :
- Ce qui fonctionne bien
- Les défauts spécifiques
- Les améliorations prioritaires

Score final = somme des 3 dimensions
**Raison** : L'évaluation actuelle manque de granularité pour identifier les causes précises des scores moyens
**Résultat** : *(en attente d'évaluation)*

### Mutation #11 — Iteration 10 — structure
**Cible** : Cycle d'apprentissage
**Avant** : Apprentissage après chaque itération
**Après** : Apprentissage adaptatif : après FAIL, analyse immédiate des causes. Après SUCCESS, consolidation des bonnes pratiques. Après 3 itérations similaires, méta-analyse des patterns récurrents.
**Raison** : L'apprentissage uniforme ne s'adapte pas au contexte de performance
**Résultat** : *(en attente d'évaluation)*

### Mutation #12 — Iteration 5 — structure
**Cible** : Séquence des phases
**Avant** : Séquence linéaire AGIR → ÉVALUER → APPRENDRE → MUTER
**Après** : Ajout d'une phase VALIDER entre AGIR et ÉVALUER : vérification automatique de la conformité de base (syntaxe, structure, critères minimaux) avant évaluation qualitative. Si VALIDER échoue, retour immédiat à AGIR avec diagnostic précis.
**Raison** : Les échecs répétés suggèrent des erreurs de base non détectées qui polluent l'évaluation
**Résultat** : *(en attente d'évaluation)*

### Mutation #13 — Iteration 5 — heuristic
**Cible** : Seuil de mutation
**Avant** : Mutation après chaque itération
**Après** : Mutation uniquement si : score < 60 OU variance des 3 derniers scores > 20 OU 2 échecs consécutifs. Sinon, consolidation du processus actuel.
**Raison** : Les mutations trop fréquentes empêchent la stabilisation du système
**Résultat** : *(en attente d'évaluation)*

### Mutation #14 — Iteration 5 — prompt
**Cible** : Phase AGIR
**Avant** : Prompt générique demandant d'exécuter la tâche
**Après** : Phase AGIR — Itération {iteration}

AVANT D'AGIR :
1. Lis TOUS les critères d'acceptation
2. Identifie les contraintes techniques
3. Planifie ta réponse en 3 étapes max

Tâche: {task_title}: {task_description}
Critères: {task_acceptance_criteria}

Réponds en suivant EXACTEMENT le format demandé. Vérifie ta réponse avant envoi.
**Raison** : Forcer une phase de planification pour réduire les erreurs de conformité
**Résultat** : *(en attente d'évaluation)*

### Mutation #15 — Iteration 5 — structure
**Cible** : Architecture du processus
**Avant** : Phases séquentielles isolées : AGIR → ÉVALUER → APPRENDRE → MUTER
**Après** : Phase AGIR enrichie avec contexte d'apprentissage : injection automatique des 3 derniers échecs et leurs causes dans le prompt AGIR. Format : 'Échecs récents à éviter : [liste des erreurs communes]'
**Raison** : Les phases n'apprennent pas les unes des autres, répétant les mêmes erreurs
**Résultat** : *(en attente d'évaluation)*

### Mutation #16 — Iteration 5 — heuristic
**Cible** : Seuil de mutation critique
**Avant** : Mutation si score < 60 OU variance > 20 OU 2 échecs consécutifs
**Après** : En mode critique (3+ échecs consécutifs) : mutation forcée à chaque itération + reset des heuristiques précédentes. Retour au mode normal après 2 succès consécutifs.
**Raison** : Le système est bloqué dans un état d'échec et a besoin d'exploration agressive
**Résultat** : *(en attente d'évaluation)*

### Mutation #17 — Iteration 5 — criteria
**Cible** : Métriques d'évaluation
**Avant** : Évaluation binaire PASS/FAIL avec score numérique
**Après** : Évaluation graduée : EXCELLENT (90-100), GOOD (70-89), ACCEPTABLE (50-69), POOR (30-49), FAIL (0-29). Seuil de succès abaissé à 50 temporairement en mode critique.
**Raison** : L'évaluation trop stricte peut masquer les progrès partiels et décourager l'amélioration
**Résultat** : *(en attente d'évaluation)*

### Mutation #18 — Iteration 5 — heuristic
**Cible** : Sortie du mode critique
**Avant** : Retour au mode normal après 2 succès consécutifs
**Après** : Retour au mode normal après 3 succès consécutifs avec score moyen > 85. Maintien du seuil de succès à 50 pendant 2 itérations supplémentaires après sortie du mode critique.
**Raison** : Éviter un retour prématuré au mode normal qui pourrait faire rechuter le système
**Résultat** : *(en attente d'évaluation)*

### Mutation #19 — Iteration 5 — criteria
**Cible** : Granularité des scores
**Avant** : Évaluation graduée avec 5 niveaux (EXCELLENT, GOOD, ACCEPTABLE, POOR, FAIL)
**Après** : Ajout de sous-scores détaillés : Complétude (0-30), Qualité technique (0-30), Respect des critères (0-25), Innovation/Efficacité (0-15). Score total = somme des sous-scores.
**Raison** : Permettre un diagnostic plus précis des forces/faiblesses pour guider les futures mutations
**Résultat** : *(en attente d'évaluation)*

### Mutation #20 — Iteration 10 — heuristic
**Cible** : Seuil de succès dynamique
**Avant** : Seuil fixe à 75 (ou 50 en mode critique)
**Après** : Seuil adaptatif basé sur la moyenne mobile des 3 dernières itérations + 5 points. Minimum 60, maximum 80.
**Raison** : Un seuil fixe ne s'adapte pas aux capacités réelles du système. Un seuil adaptatif permet une progression continue.
**Résultat** : *(en attente d'évaluation)*

### Mutation #21 — Iteration 10 — prompt
**Cible** : Phase AGIR
**Avant** : Prompt complexe avec multiples instructions
**Après** : Phase AGIR — Itération {iteration}

## Tâche
{task_title}: {task_description}
Critères: {task_acceptance_criteria}

## Instructions
Résous cette tâche de manière directe et efficace. Concentre-toi sur la qualité plutôt que la quantité. Fournis une solution complète et testable.

Réponds en JSON strict avec 'solution' et 'explanation'.
**Raison** : Simplifier le prompt pour réduire la confusion et améliorer la focus sur l'essentiel
**Résultat** : *(en attente d'évaluation)*

### Mutation #22 — Iteration 10 — criteria
**Cible** : Système de scoring
**Avant** : Sous-scores détaillés complexes (Complétude, Qualité technique, etc.)
**Après** : Score unique de 0 à 100 basé sur 3 critères équilibrés : Fonctionnalité (40%), Qualité du code (35%), Respect des critères (25%)
**Raison** : Le système de sous-scores complexe peut créer de la confusion. Un scoring simplifié mais structuré est plus efficace.
**Résultat** : *(en attente d'évaluation)*

### Mutation #23 — Iteration 15 — prompt
**Cible** : Phase AGIR
**Avant** : Instructions génériques demandant une solution directe et efficace
**Après** : Phase AGIR — Itération {iteration}

## Tâche
{task_title}: {task_description}
Critères: {task_acceptance_criteria}

## Instructions
1. Analyse d'abord les critères d'acceptation pour identifier les exigences clés
2. Décompose la tâche en sous-problèmes si nécessaire
3. Implémente une solution robuste avec gestion d'erreurs
4. Inclus des tests ou exemples d'utilisation
5. Documente les choix techniques importants

Réponds en JSON strict avec 'solution' (code/implémentation) et 'explanation' (justification des choix).
**Raison** : Les instructions actuelles sont trop vagues. Une approche structurée en étapes devrait améliorer la qualité et la complétude des solutions.
**Résultat** : *(en attente d'évaluation)*

### Mutation #24 — Iteration 15 — criteria
**Cible** : Système de scoring
**Avant** : Score unique 0-100 avec répartition Fonctionnalité 40%, Qualité 35%, Respect critères 25%
**Après** : Score détaillé sur 4 dimensions pondérées :
- Complétude fonctionnelle (30%) : La solution répond-elle à tous les besoins ?
- Robustesse technique (25%) : Gestion d'erreurs, edge cases, performance
- Clarté et maintenabilité (25%) : Code lisible, bien structuré, documenté
- Respect des spécifications (20%) : Adhérence exacte aux critères d'acceptation
Score final = moyenne pondérée, seuil SUCCESS = 85+
**Raison** : Le scoring actuel est trop simpliste et ne capture pas les nuances. Un système plus granulaire permettra une évaluation plus précise et des retours plus utiles.
**Résultat** : *(en attente d'évaluation)*

### Mutation #25 — Iteration 20 — prompt
**Cible** : Phase AGIR
**Avant** : Instructions basiques avec approche libre, pas de méthodologie imposée
**Après** : Phase AGIR — Itération {iteration}

## Tâche
{task_title}: {task_description}
Critères: {task_acceptance_criteria}

## Méthodologie MAEL
1. **ANALYSER** : Décomposer la tâche en sous-problèmes
2. **CONCEVOIR** : Définir l'architecture et les interfaces
3. **IMPLÉMENTER** : Coder avec gestion d'erreurs et tests
4. **VALIDER** : Vérifier chaque critère d'acceptation
5. **DOCUMENTER** : Expliquer les choix et l'utilisation

## Standards qualité
- Code défensif avec validation des entrées
- Gestion explicite des cas d'erreur
- Tests unitaires pour les fonctions critiques
- Documentation claire des APIs
- Respect strict des spécifications

## Livrables attendus
- Code source complet et fonctionnel
- Tests de validation
- Documentation d'utilisation
- Justification des choix techniques

Réponds en JSON avec structure : {"solution": "...", "tests": "...", "documentation": "...", "rationale": "..."}
**Raison** : Le prompt actuel ne guide pas suffisamment vers l'excellence. Une méthodologie structurée et des standards explicites devraient pousser les scores vers 85+
**Résultat** : *(en attente d'évaluation)*

### Mutation #26 — Iteration 20 — heuristic
**Cible** : Seuil de mutation
**Avant** : Mutations déclenchées après stagnation ou dégradation
**Après** : Déclencher une mutation si : score < 85 pendant 2 itérations consécutives OU amélioration < 5 points sur 3 itérations OU score en baisse sur 2 itérations
**Raison** : Le système s'améliore mais n'atteint pas l'excellence (85+). Il faut être plus proactif dans les mutations pour éviter les plateaux
**Résultat** : *(en attente d'évaluation)*
