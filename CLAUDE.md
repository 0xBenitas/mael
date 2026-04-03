# CLAUDE.md — Mémoire Persistante du Projet MAEL

> Ce fichier est la mémoire sémantique du projet.
> Il est lu au début de chaque itération de la boucle MAEL.
> Les patterns confirmés (2+ utilisations) y sont promus depuis .mael/learnings.md.

---

## Projet

**MAEL** = Méta-Amélioration Évolutive en Ligne

Objectif : Créer une boucle auto-améliorante où Claude Code :
1. Exécute des tâches
2. Évalue ses résultats
3. Apprend de ses erreurs et succès
4. Mute ses propres processus d'évaluation et d'apprentissage

## Conventions

- Langue : Français pour la documentation, anglais pour le code
- Fichiers de la boucle dans `.mael/`
- Logs dans `.mael/logs/`
- Règles promues dans `.mael/rules/`

## Patterns Confirmés

- **[2026-04-03]** Structure modulaire (state/memory/selfrefine/mutator/engine) permet les tests isolés
- **[2026-04-03]** 18 tests unitaires avant intégration = zéro bug à l'exécution du moteur
- **[2026-04-03]** Fichiers JSON pour l'état + Markdown pour la mémoire humaine = bon compromis

## Gotchas Connus

- **[2026-04-03]** L'évaluation v0 est heuristique (score fixe 75.0) — doit être remplacée par de vrais tests
- **[2026-04-03]** La boucle engine.py tourne localement sans appeler Claude — la v1 doit intégrer l'API

## Architecture

```
mael/
├── __init__.py      # Package marker
├── state.py         # Gestion d'état (.mael/state.json)
├── memory.py        # Mémoire persistante (learnings, metrics, mutations)
├── selfrefine.py    # Module Self-Refine (generate→critique→refine)
├── mutator.py       # Module Ouroboros (analyse→propose→applique mutations)
└── engine.py        # Orchestrateur principal (AGIR→ÉVALUER→APPRENDRE→MUTER)
```

Voir `META_ANALYSE_AUTOPROMPTING.md` pour l'analyse complète.
La boucle suit le cycle : AGIR → ÉVALUER → APPRENDRE → MUTER
