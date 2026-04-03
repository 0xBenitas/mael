"""Phase prompts for the MAEL loop.

These prompts ARE the targets of Ouroboros mutation.
The mutator phase can rewrite them to improve the loop itself.
"""

SYSTEM_MAEL = """Tu es MAEL (Méta-Amélioration Évolutive en Ligne), un système auto-améliorant.
Tu travailles dans un dépôt Git. Tu es rigoureux, concis, et orienté résultat.
Langue : français pour les explications, anglais pour le code."""


PHASE_ACT = """Phase AGIR — Itération {iteration}

## Tâche courante
ID: {task_id}
Titre: {task_title}
Description: {task_description}
Critères d'acceptation: {task_acceptance}

## Contexte du projet
{claude_md}

## Learnings accumulés
{learnings}

## Instructions
1. Analyse la tâche et ses critères d'acceptation
2. Propose une implémentation CONCRÈTE (code Python complet, prêt à écrire dans un fichier)
3. Structure ta réponse ainsi :

### Analyse
(brève analyse de la tâche)

### Fichiers à créer/modifier
Pour chaque fichier, donne le chemin et le contenu complet :
```path: chemin/du/fichier.py
contenu complet du fichier
```

### Commande de validation
(une commande pour vérifier que ça marche, ex: python -m pytest tests/)
"""


PHASE_EVALUATE = """Phase ÉVALUER — Itération {iteration}

## Tâche évaluée
ID: {task_id}
Titre: {task_title}
Critères d'acceptation: {task_acceptance}

## Résultat de la phase AGIR
{act_result}

## Résultat des tests (si exécutés)
{test_output}

## Métriques précédentes
Score moyen: {avg_score}
Tendance: {trend}

## Instructions
Évalue le résultat sur 5 dimensions (chacune sur 20 points, total 100) :
1. **Correctness** : Le code fait-il ce qui est demandé ?
2. **Completeness** : Tous les critères d'acceptation sont-ils couverts ?
3. **Quality** : Le code est-il propre, idiomatique, bien structuré ?
4. **Testability** : Le code est-il facilement testable ?
5. **Learning** : La solution apporte-t-elle des insights réutilisables ?

Réponds en JSON strict :
{{
  "scores": {{"correctness": N, "completeness": N, "quality": N, "testability": N, "learning": N}},
  "total": N,
  "verdict": "SUCCESS|PARTIAL|FAIL",
  "critique": "analyse détaillée",
  "suggestion": "amélioration concrète si PARTIAL ou FAIL"
}}
"""


PHASE_LEARN = """Phase APPRENDRE — Itération {iteration}

## Résumé de l'itération
Tâche: {task_title}
Verdict: {verdict}
Score: {score}/100
Critique: {critique}

## Learnings existants
{learnings}

## Instructions
Extrais les learnings de cette itération. Pour chaque learning :
- Il doit être **actionnable** et **réutilisable**
- Il doit aider les itérations futures à mieux performer

Réponds en JSON strict :
{{
  "learnings": [
    {{
      "category": "success_pattern|failure_analysis|optimization|gotcha",
      "learning": "description concise et actionnable",
      "confidence": "haute|moyenne|basse",
      "reusable_for": "dans quel contexte ce learning est utile"
    }}
  ],
  "patterns_seen_again": ["learning existant vu à nouveau, texte exact"],
  "promote_to_claude_md": ["learning assez solide pour être promu"]
}}
"""


PHASE_MUTATE = """Phase MUTER — Itération {iteration} — Le serpent se mord la queue 🐍

Tu es le méta-évaluateur de MAEL. Tu améliores le PROCESSUS, pas les tâches.

## Métriques des {n_last} dernières itérations
{metrics_summary}

## Tendance
{trend}

## Mutations passées
{past_mutations}

## Prompts actuels des phases
- AGIR : {act_prompt_preview}
- ÉVALUER : {eval_prompt_preview}
- APPRENDRE : {learn_prompt_preview}

## Instructions
Analyse le processus et propose des mutations. Types possibles :
1. **prompt** : Modifier un prompt de phase pour de meilleurs résultats
2. **criteria** : Changer les critères d'évaluation
3. **heuristic** : Modifier une règle de décision du système
4. **structure** : Changer l'architecture du processus

Réponds en JSON strict :
{{
  "analysis": "diagnostic du processus actuel",
  "health": "healthy|degrading|critical",
  "mutations": [
    {{
      "type": "prompt|criteria|heuristic|structure",
      "target": "ce qui est muté",
      "before_summary": "résumé de l'état actuel",
      "after": "la nouvelle version concrète",
      "reason": "pourquoi cette mutation",
      "expected_impact": "quel impact attendu",
      "confidence": 0.0
    }}
  ]
}}
"""
