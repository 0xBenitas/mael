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
- **[2026-04-03]** Fixture sans assertion interne = contrat non validé. Pattern : `def fixture(): obj = load(); assert obj.attr; return obj`
- **[2026-04-03]** Code tronqué détecté par grep/tail = abandon de tâche. Checkpoint obligatoire avant validation : vérifier que toutes les fonctions/fixtures ont un `return` ou `assert` visible.
- **[2026-04-03]** Assertion explicite sur attribut concret obligatoire dans fixture de chargement d'état, pas juste retour de l'objet.
- **[2026-04-03]** Fixture incomplète = déconnexion code/exécution. Valider intégrité du fichier source avant succès.
- **[2026-04-03]** Utiliser conftest.py comme source unique de vérité pour les fixtures réutilisables cross-file plutôt que de les redéfinir dans chaque test.
- **[2026-04-03]** Le pattern stub_with_fallback (sys.path.insert + try/except ImportError) est robuste pour tester avant que les modules réels existent. Valider avec pytest --collect-only.
- **[2026-04-03]** Réutiliser les fixtures du conftest.py est une architecture éprouvée pour les suites de tests cohérentes et maintenables.
- **[2026-04-03]** Le pattern robust_import_with_stub est universellement applicable et garantit la robustesse des suites de tests multi-fichiers. Documenter comme best practice.
- **[2026-04-03]** Fixtures pytest bien nommées et documentées sont plus maintenables que setup/teardown. Déclarer dans conftest.py pour réutilisation multi-fichiers.
- **[2026-04-03]** Pattern de stub avec fallback est maintenant validé sur 2 fichiers (test_engine.py, test_autonomy.py). Promouvoir en pattern standard pour tous les tests futurs.
- **[2026-04-03]** Fixtures pytest bien nommées et documentées sont plus maintenables que des setup/teardown et réutilisables entre fichiers de test si déclarées dans conftest.py.
- **[2026-04-03]** Utiliser une classe stub avec docstring explicite plutôt qu'une simple pass. Cela documente l'intention et facilite le debugging.
- **[2026-04-03]** Stratégie robuste pour tests avec dépendances manquantes : (1) ajouter src/ à sys.path, (2) try/except ImportError avec classe stub, (3) fixtures pytest réutilisables, (4) tests couvrant cas nominal + fallback. Cela permet aux tests de s'exécuter même si le module source n'existe pas encore.
- **[2026-04-03]** Exécutabilité > Couverture > Sophistication. Un test non-exécutable = 0 points, peu importe la qualité du code.
- **[2026-04-03]** Ordre d'exécution critique pour créer une structure test exécutable : (1) créer src/summarizer.py avec fonction stub, (2) conftest.py avec import explicite, (3) test_*.py avec assert True, (4) pytest --collect-only, (5) pytest, (6) assertions métier. Ne jamais sauter l'étape 1.
- **[2026-04-03]** L'exécutabilité est le critère #1 avant la couverture, la sophistication ou la qualité du code. Ne jamais sacrifier 'ça marche' pour 'c'est beau'.
- **[2026-04-03]** Ordre d'exécution strict pour 'créer tests qui passent' : (1) conftest.py avec import du module, (2) test_*.py avec 1 test trivial (assert True), (3) 'pytest --collect-only' doit retourner N items, (4) 'pytest' doit passer, (5) ajouter assertions métier. Valider l'exécutabilité à chaque étape avant d'ajouter de la complexité.
- **[2026-04-03]** Ordre d'exécution pour tests: (1) conftest.py + import trivial, (2) test_*.py avec assert True, (3) vérifier collection, (4) assertions métier. Cela prévient 90% des ModuleNotFoundError.
- **[2026-04-03]** pytest infrastructure: utiliser conftest.py avec pytest_configure ou setup.py/pyproject.toml au lieu de sys.path.insert(). Valider avec 'pytest --collect-only' avant d'écrire les assertions.
- **[2026-04-03]** Avant d'implémenter un algorithme, spécifier par écrit : langue, ressources, cas limites, test de régression. Valider avec test unitaire avant logique métier.
- **[2026-04-03]** Prioriser complétude et exécutabilité avant sophistication. Un code simple qui marche > code conceptuellement bon mais incomplet. Découper en étapes : (1) interface, (2) cas trivial, (3) cas complexe.
- **[2026-04-03]** Extraire l'interface attendue d'un module AVANT modification : lister imports, signatures, retours via grep/ast.parse(). Générer en respectant strictement cette interface pour prévenir ImportError et ruptures de contrats.
- **[2026-04-03]** Avant d'implémenter un algorithme (TF-IDF, scoring, etc.), définir explicitement : langue, ressources linguistiques, cas limites, et test de régression. Cela force la clarté et prévient les implémentations incomplètes.
- **[2026-04-03]** Remplacer les tests manuels (print statements) par des assertions ou des tests unitaires avec des cas d'entrée/sortie connus. Un test manuel qui passe ne prouve pas que l'algorithme fonctionne.
- **[2026-04-03]** Extraire l'interface attendue (imports, signatures) via ast.parse() avant de générer du code qui modifie un module existant. Cela prévient les ImportError et les ruptures de contrats.
- **[2026-04-03]** Ajouter des tests spécifiques pour chaque amélioration algorithmique avant de déclarer une tâche complète — valide que l'amélioration produit un résultat mesurable
- **[2026-04-03]** Intégrer un facteur de position (ex: +20% pour phrases 0-2 et dernière phrase) dans le scoring TF-IDF pour améliorer la qualité des résumés
- **[2026-04-03]** Toujours ajouter un test d'intégration end-to-end qui appelle la fonction principale et valide sa sortie complète (type, longueur, contenu non-vide) — détecte les fonctions tronquées
- **[2026-04-03]** Après génération, exécuter un test d'intégration minimal (ex: summarize(sample_text)) pour vérifier que toutes les dépendances internes sont présentes et complètes.
- **[2026-04-03]** Extraire les signatures des tests existants (grep 'from module import') et générer EXACTEMENT les fonctions attendues avec les bons noms et visibilité avant de coder la logique.
- **[2026-04-03]** Avant soumission de code Python multi-fonction, exécuter 'python -m py_compile' et vérifier que parenthèses/accolades sont équilibrées. Cela détecte les fichiers tronqués.
- **[2026-04-03]** Pour l'intégration avec des suites de tests existantes, extraire d'abord la signature des imports et des appels de fonction attendus, puis générer EXACTEMENT ces interfaces avant d'implémenter la logique.
- **[2026-04-03]** Avant soumission de code généré, exécuter un test de complétude syntaxique : vérifier que le fichier n'est pas tronqué (parenthèses équilibrées, pas de fonction inachevée) et que toutes les fonctions attendues par les tests existants sont présentes et exportées.
- **[2026-04-03]** Chercher systématiquement les patterns ['# TODO', '# FIXME', 'pass', '...'] dans le code généré comme RED FLAGS d'implémentation incomplète.
- **[2026-04-03]** Tests passants ne garantissent pas la complétude : vérifier que les tests exercent TOUS les chemins critiques de la fonction principale, pas seulement l'import et la signature.
- **[2026-04-03]** Complétude prime sur qualité partielle : générer toujours jusqu'au bout, même avec stubs, plutôt que laisser fichier tronqué
- **[2026-04-03]** Baseline testing avant/après : exécuter pytest sur l'état initial, puis après génération, pour détecter régressions d'imports
- **[2026-04-03]** Validation post-génération en deux étapes : py_compile + import check pour détecter troncatures et fonctions manquantes
- **[2026-04-03]** La complétude du code prime sur la qualité partielle. Un fichier tronqué avec bon algorithme échoue les critères d'acceptation. Toujours générer jusqu'au bout.
- **[2026-04-03]** Avant de générer du code complétant une implémentation, vérifier l'état des imports et des fonctions manquantes. Cela évite de générer du code qui ne sera jamais testé.
- **[2026-04-03]** Pour les suites de test, utiliser le pattern : classes organisées par cas d'usage (Empty, Short, Long, EdgeCases), chacune avec 2-3 assertions ciblées. Ce pattern est réutilisable et maintenable.
- **[2026-04-03]** Valider la complétude des fichiers générés avec trois vérifications : (1) tail -5 pour vérifier la dernière ligne, (2) python -m py_compile pour la syntaxe, (3) python -c 'import <module>' pour l'importabilité. Ces trois étapes prennent <5s et préviennent 90% des échecs d'exécution.
- **[2026-04-03]** Avant toute génération de tests, exécuter un diagnostic d'importabilité du module cible. Cela économise du temps en détectant les problèmes d'environnement avant la génération complète.
- **[2026-04-03]** Vérifier la complétude des fichiers générés avec 'tail -20 <file>' ET 'python -m py_compile <file>' immédiatement après génération. Un fichier syntaxiquement valide mais tronqué peut passer la compilation mais échouer à l'import.
- **[2026-04-03]** Validation post-génération obligatoire en trois étapes : (1) syntaxe Python valide, (2) imports résolus, (3) exécution réelle. Échouer à l'étape 2 signifie que le chemin d'import ne correspond pas à la structure réelle du projet.
- **[2026-04-03]** Avant de générer des tests, valider que le module à tester existe et est importable via 'python -c "import <module>"'. Cela évite de générer des tests corrects mais inutilisables.
- **[2026-04-03]** Implémenter une validation post-génération obligatoire en trois étapes (syntaxe → collection → exécution) avec diagnostic détaillé en cas d'échec
- **[2026-04-03]** Vérifier la complétude des fichiers générés immédiatement après écriture avec 'tail' et 'wc -l' pour détecter les troncatures
- **[2026-04-03]** Valider la structure du projet et les chemins d'import avant de générer des tests : utiliser 'find' et 'python -c import' pour garantir la cohérence
- **[2026-04-03]** Assertions fortes (vérifier contenu exact, structure, cas limites) plutôt que faibles (len >= 1). Générer avec assertions fortes dès le départ.
- **[2026-04-03]** Vérifier que le module cible existe et est importable AVANT de générer ses tests: 'python -c "import tools.summarize"'
- **[2026-04-03]** Validation post-génération en trois étapes (py_compile + collect-only + pytest -v) est obligatoire pour tout fichier test généré. Arrêter et diagnostiquer si l'une échoue.
- **[2026-04-03]** Validation post-génération obligatoire pour tout fichier test: (1) py_compile pour syntaxe, (2) pytest --collect-only pour vérifier N > 0 tests collectés, (3) pytest -v avec timeout. Arrêter si collecte échoue.
- **[2026-04-03]** ModuleNotFoundError lors de pytest indique un problème de PYTHONPATH ou de structure du projet. Diagnostic: (1) vérifier sys.path, (2) confirmer structure (tools/ au même niveau que tests/), (3) exécuter 'python -m pytest --collect-only' avant l'exécution.
- **[2026-04-03]** Utiliser 'pytest --collect-only' comme signal d'arrêt : si collected == 0, diagnostiquer avant itération suivante.
- **[2026-04-03]** Après génération de fichiers test, exécuter immédiatement 'python -m py_compile test_*.py' pour détecter les fichiers tronqués avant pytest.
- **[2026-04-03]** Avant de générer des tests, valider que le module source est importable : 'python -c "import tools.summarize"'. Cela économise une itération entière.
- **[2026-04-03]** Un fichier test avec import incorrect dans la même suite peut bloquer la collecte de TOUS les tests. Avant de générer, nettoyer les imports cassés existants avec grep -r 'from summarize' tests/ et corriger ou supprimer.
- **[2026-04-03]** Après un score < 50 avec 'collected 0 items', diagnostic systématique : (1) vérifier la syntaxe du fichier généré avec ast.parse(), (2) exécuter pytest -v --tb=short pour identifier les erreurs de collecte, (3) nettoyer les fichiers test cassés existants, (4) générer 3-4 tests seulement et valider avant d'itérer.
- **[2026-04-03]** Après un score < 50, basculer en mode itératif : générer 3-4 tests, exécuter avec pytest, corriger, continuer. Ne pas tenter de génération monolithique si la structure du projet n'est pas validée.
- **[2026-04-03]** Valider la structure du projet (existence de répertoires, __init__.py, accessibilité des imports) AVANT de générer des tests. Exécuter un import de vérification minimal avec pytest pour détecter les erreurs de chemin sans investir dans la génération complète.
- **[2026-04-03]** Pour modules <200 LOC, générer 8-12 tests en 2-3 blocs de 4-5 tests avec exécution et correction après chaque bloc plutôt que monolithique.
- **[2026-04-03]** Implémenter une vérification post-génération pour tout fichier >100 LOC : ast.parse() pour syntaxe, compter les 'def test_' vs planifié, vérifier fermeture des fonctions.
- **[2026-04-03]** Valider l'importabilité du module source AVANT toute génération de tests via un fichier test minimal (3-5 lignes) contenant uniquement l'import, exécuté avec pytest.
- **[2026-04-03]** Valider la complétude syntaxique via ast.parse() et comptage des def test_* avant commit
- **[2026-04-03]** Générer les tests par blocs de 5-8 avec exécution immédiate après chaque bloc pour prévenir les fichiers tronqués
- **[2026-04-03]** Valider l'importabilité du module source AVANT toute génération de tests via un fichier test minimal contenant uniquement l'import
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
