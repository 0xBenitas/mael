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
- **[2026-04-03]** Post-generation validation: Count `def test_*`, verify function closures, run `ast.parse()` on generated file before commit. Detects silent truncation and syntax errors.
- **[2026-04-03]** Incremental test generation: Generate tests in blocks of 5-8, execute immediately after each block, validate syntax and imports before continuing. Prevents truncation and mass errors.
- **[2026-04-03]** Import validation step: Always create and execute a minimal test file (import only) before generating full test suite. Detects path/structure errors early.
- **[2026-04-03]** Toujours vérifier la complétude du fichier généré : compter les def test_*, vérifier la fermeture des fonctions, valider la syntaxe avec ast.parse() avant commit.
- **[2026-04-03]** Générer par blocs de 5-8 tests, exécuter immédiatement, valider la syntaxe et l'import, puis continuer. Évite les fichiers tronqués et les erreurs de masse.
- **[2026-04-03]** ModuleNotFoundError sur import = signal d'arrêt immédiat. Avant d'écrire des tests, valider que le module source existe et est importable. Ajouter une étape 'Import validation' : créer un fichier test minimal qui importe uniquement le module, l'exécuter, puis procéder aux tests complets.
- **[2026-04-03]** Profiling de performance (temps + mémoire) sur 3 tailles d'input = validation obligatoire avant production
- **[2026-04-03]** Cas limites explicites + assertions loggées = prévention de bugs en production
- **[2026-04-03]** Architecture modulaire + validation intégrée + tests complets = pattern de succès pour utilitaires robustes
- **[2026-04-03]** Gestion des cas limites explicite : texte vide, une phrase, très long texte. Chaque cas doit afficher assertion + résultat réel.
- **[2026-04-03]** Composants isolés d'abord : tester split_sentences(), score_sentence(), summarize() séparément avec input→output complet avant intégration.
- **[2026-04-03]** Validation intermédiaire obligatoire post-création : 5 étapes (fichier existe, syntaxe valide, import réussit, fonction simple exécute, cas limites testés). Chaque étape loggée explicitement.
- **[2026-04-03]** Consulter et appliquer les learnings existants AVANT phase AGIR. Mapper chacun à une action concrète et tracer l'application dans la soumission.
- **[2026-04-03]** Ajouter une étape obligatoire post-création : (1) Vérifier fichier existe, (2) Compiler/parser, (3) Importer, (4) Exécuter simple, (5) Exécuter limites. Chaque étape loggée avec succès/échec explicite.
- **[2026-04-03]** Implémenter une vérification stricte de complétude : chaque étape critique doit produire un marqueur de fin explicite et vérifier que les fichiers générés sont complets via wc -l ou hash de contenu.
- **[2026-04-03]** Consultation obligatoire et tracée des learnings existants AVANT de commencer le code : lister explicitement lesquels s'appliquent et les intégrer dans la checklist.
- **[2026-04-03]** Isoler et tester le cœur métier (étapes critiques) comme fonctions séparées AVANT intégration pour détecter les troncatures et valider chaque étape indépendamment.
- **[2026-04-03]** Checklist pré-soumission multi-niveaux : (1) Syntaxe, (2) Import, (3) Exécution simple, (4) Exécution complète avec tous les cas limites, (5) Vérification de non-troncature (variables assignées, sortie complète). Chaque niveau doit passer avant le suivant.
- **[2026-04-03]** Signal composite de code cassé : variable déclarée sans assignation + docstring complète + exécution partielle = implémentation tronquée. Ne pas ignorer les signaux multiples convergents.
- **[2026-04-03]** Checklist de validation multi-niveaux : (1) Syntaxe, (2) Import, (3) Exécution simple, (4) Exécution complète avec tous les cas limites, (5) Vérification de non-troncature de sortie. Appliquer avant chaque soumission.
- **[2026-04-03]** Défaut systémique détecté : répétition de patterns d'erreur sur 4 itérations consécutives malgré documentation de learnings. Implémenter une étape de révision OBLIGATOIRE qui consulte les learnings existants avant chaque itération, avec trace écrite.
- **[2026-04-03]** L'itération 3 a répété l'erreur des itérations 1 et 2 malgré 4 learnings documentés. Implémenter une étape de révision explicite qui consulte les learnings avant de coder pour briser le cycle de répétition d'erreurs.
- **[2026-04-03]** Créer une checklist pré-soumission basée sur les learnings des itérations précédentes : (1) Syntaxe valide, (2) Import sans erreur, (3) Exécution complète avec données réelles, (4) Sortie non-tronquée, (5) Gestion d'erreurs pour cas limites. Appliquer cette checklist avant chaque soumission.
- **[2026-04-03]** Checklist pré-exécution obligatoire : (1) Pas de code tronqué, (2) Import réussit, (3) Sortie complète (pas de troncature), (4) Gestion d'erreurs pour cas limites.
- **[2026-04-03]** Syntaxe valide ≠ implémentation complète. Valider avec `python -m py_compile` ET exécution réelle avant acceptation.
- **[2026-04-03]** L'absence de gestion d'erreurs (cas limites : texte vide, None, texte sans phrases) rend une fonction partiellement fonctionnelle. Implémenter les guards et validations d'entrée dès le départ.
- **[2026-04-03]** Les fonctions déclarées mais non implémentées (corps vide) passent la validation syntaxique mais causent des défaillances silencieuses à l'exécution. Toujours vérifier que chaque fonction a un corps complet avant de considérer la tâche terminée.

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
