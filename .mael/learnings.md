# MAEL — Learnings

> Apprentissages accumulés par la boucle auto-améliorante.
> Les patterns vus 2+ fois sont promus dans CLAUDE.md.

---

## Format

```
### [YYYY-MM-DD] Iteration N — Catégorie
**Contexte** : ...
**Learning** : ...
**Confiance** : haute/moyenne/basse
**Utilisations** : 0
```

---

*Aucun learning pour l'instant. La boucle n'a pas encore tourné.*

### [2026-04-03] Iteration 1 — success_pattern
**Contexte** : Task: Créer le moteur Python de la boucle MAEL
**Learning** : Approach worked for task type: Créer le moteur Python de la boucle MAEL
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 2 — success_pattern
**Contexte** : Task: Implémenter le module Self-Refine pour MAEL
**Learning** : Approach worked for task type: Implémenter le module Self-Refine pour MAEL
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 3 — success_pattern
**Contexte** : Task: Créer le système de mémoire persistante
**Learning** : Approach worked for task type: Créer le système de mémoire persistante
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 4 — success_pattern
**Contexte** : Task: Ajouter le module de mutation Ouroboros
**Learning** : Approach worked for task type: Ajouter le module de mutation Ouroboros
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 5 — success_pattern
**Contexte** : Task: Tests unitaires et intégration
**Learning** : Approach worked for task type: Tests unitaires et intégration
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 1 — success_pattern
**Contexte** : Task: Tests unitaires et intégration v0.2
**Learning** : Task scored 75/100
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 1 — success_pattern
**Contexte** : Task: Créer un utilitaire de résumé de texte
**Learning** : Task scored 75/100
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 2 — success_pattern
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : Task scored 75/100
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 3 — success_pattern
**Contexte** : Task: Améliorer le résumé avec un scoring TF-IDF simplifié
**Learning** : Task scored 75/100
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 1 — failure_analysis
**Contexte** : Task: Créer un utilitaire de résumé de texte
**Learning** : Les fonctions déclarées mais non implémentées (corps vide) passent la validation syntaxique mais causent des défaillances silencieuses à l'exécution. Toujours vérifier que chaque fonction a un corps complet avant de considérer la tâche terminée.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 1 — failure_analysis
**Contexte** : Task: Créer un utilitaire de résumé de texte
**Learning** : L'absence de gestion d'erreurs (cas limites : texte vide, None, texte sans phrases) rend une fonction partiellement fonctionnelle. Implémenter les guards et validations d'entrée dès le départ, pas en itération suivante.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 1 — gotcha
**Contexte** : Task: Créer un utilitaire de résumé de texte
**Learning** : Une sortie tronquée dans les tests stdout ('Machine learni...') indique une exécution défaillante non diagnostiquée. Toujours exécuter le code complet et vérifier que la sortie n'est pas coupée avant de valider.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 1 — optimization
**Contexte** : Task: Créer un utilitaire de résumé de texte
**Learning** : Un score de 69/100 avec implémentation incomplète suggère que les critères d'acceptation étaient trop permissifs. Durcir les critères : exiger une exécution sans erreur + tests passants + gestion d'erreurs minimale.
**Confiance** : moyenne
**Utilisations** : 0

### [2026-04-03] Iteration 1 — failure_analysis
**Contexte** : Task: Créer un utilitaire de résumé de texte
**Learning** : L'approche heuristique simple peut être fonctionnelle mais nécessite une implémentation complète. Ne pas confondre 'approche valide' avec 'implémentation terminée'.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 2 — failure_analysis
**Contexte** : Task: Créer un utilitaire de résumé de texte
**Learning** : Une fonction tronquée au milieu de sa logique (ex: 'if not s' sans suite) crée une syntaxe invalide qui échoue silencieusement à l'import. Toujours valider la syntaxe Python avec `python -m py_compile` avant de considérer le code complet.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 2 — gotcha
**Contexte** : Task: Créer un utilitaire de résumé de texte
**Learning** : Une sortie tronquée dans stdout ('Machine learning is a...') est un signal d'alerte d'exécution défaillante. Vérifier systématiquement que la sortie complète est produite, pas juste que le programme s'exécute.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 2 — failure_analysis
**Contexte** : Task: Créer un utilitaire de résumé de texte
**Learning** : Déclarer une fonction avec docstring et type hints mais sans implémentation complète crée une fausse impression de complétude. Exiger que chaque fonction ait un corps exécutable (pas juste `pass` ou code tronqué) avant validation.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 2 — optimization
**Contexte** : Task: Créer un utilitaire de résumé de texte
**Learning** : Les critères d'acceptation doivent inclure explicitement : (1) Syntaxe valide vérifiée, (2) Import sans erreur, (3) Exécution complète sans troncature, (4) Gestion d'erreurs pour cas limites. Un score de 55/100 avec code cassé indique que ces critères n'étaient pas appliqués.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 2 — failure_analysis
**Contexte** : Task: Créer un utilitaire de résumé de texte
**Learning** : L'itération 2 a répété l'erreur de l'itération 1 (implémentation incomplète) malgré les learnings documentés. Cela indique que les learnings n'ont pas été appliqués activement. Implémenter une checklist pré-exécution basée sur les learnings précédents.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 3 — failure_analysis
**Contexte** : Task: Créer un utilitaire de résumé de texte
**Learning** : Une docstring tronquée (s'arrêtant au milieu d'une phrase comme 'Raises: ValueError: If max_sentences is less than') est un indicateur fiable que le fichier a été écrit partiellement ou corrompu. Toujours vérifier que les docstrings sont complètes avant de considérer une implémentation valide.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 3 — gotcha
**Contexte** : Task: Créer un utilitaire de résumé de texte
**Learning** : Une fonction avec signature, docstring et type hints mais sans corps exécutable (ou avec corps tronqué) passe les vérifications syntaxiques basiques mais échoue à l'exécution. Exiger une exécution réelle avec données de test, pas juste une vérification d'import.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 3 — optimization
**Contexte** : Task: Créer un utilitaire de résumé de texte
**Learning** : Créer une checklist pré-soumission basée sur les learnings des itérations précédentes : (1) Syntaxe valide, (2) Import sans erreur, (3) Exécution complète avec données réelles, (4) Sortie non-tronquée, (5) Gestion d'erreurs pour cas limites. Appliquer cette checklist avant chaque soumission.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 3 — failure_analysis
**Contexte** : Task: Créer un utilitaire de résumé de texte
**Learning** : L'itération 3 a répété l'erreur des itérations 1 et 2 (implémentation incomplète) malgré 4 learnings documentés. Cela indique un défaut systémique : les learnings existent mais ne sont pas appliqués activement. Implémenter une étape de révision explicite qui consulte les learnings avant de coder.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 3 — gotcha
**Contexte** : Task: Créer un utilitaire de résumé de texte
**Learning** : Une sortie tronquée ('It enables system' au lieu d'une phrase complète) combinée à une docstring tronquée est un signal composite très fort d'implémentation cassée. Ne pas ignorer les signaux multiples convergents.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 4 — failure_analysis
**Contexte** : Task: Créer un utilitaire de résumé de texte
**Learning** : Une variable déclarée mais non assignée (raw_sentences sans valeur) dans une docstring complète indique une troncature du corps de fonction, pas une erreur de syntaxe. Vérifier que TOUTES les variables utilisées dans la logique sont effectivement assignées avant utilisation.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 4 — gotcha
**Contexte** : Task: Créer un utilitaire de résumé de texte
**Learning** : Une exécution partielle (tests 1-3 passent, test 4 coupé) combinée à une docstring complète mais un corps incomplet = signature valide masquant une implémentation cassée. Toujours exécuter TOUS les cas de test jusqu'à complétion, pas juste vérifier que certains passent.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 4 — optimization
**Contexte** : Task: Créer un utilitaire de résumé de texte
**Learning** : Les learnings des itérations 1-3 (checklist pré-soumission, exécution réelle, révision explicite) n'ont pas été appliqués à l'itération 4. Implémenter une étape OBLIGATOIRE de consultation des learnings existants AVANT de commencer le code, avec trace écrite de cette consultation.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 4 — success_pattern
**Contexte** : Task: Créer un utilitaire de résumé de texte
**Learning** : La structure générale (validation d'entrée, docstring, gestion d'erreurs) était correcte. Isoler et tester le cœur métier (split → scoring → extraction) séparément avant intégration pour détecter les troncatures dans les sections critiques.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 4 — gotcha
**Contexte** : Task: Créer un utilitaire de résumé de texte
**Learning** : Un fichier importable mais non-exécutable (import réussit, exécution échoue) crée une fausse confiance. La checklist doit distinguer : (1) Import, (2) Exécution simple, (3) Exécution avec tous les cas limites, (4) Vérification de non-troncature de sortie.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 5 — failure_analysis
**Contexte** : Task: Créer un utilitaire de résumé de texte
**Learning** : Une fonction avec docstring complète mais corps tronqué (variable déclarée sans assignation, logique inachevée) passe la vérification syntaxique mais échoue à l'exécution. Diagnostic : vérifier que CHAQUE variable utilisée dans le corps a une assignation explicite AVANT sa première utilisation, pas seulement dans la docstring.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 5 — gotcha
**Contexte** : Task: Créer un utilitaire de résumé de texte
**Learning** : L'exécution partielle de tests (TEST 1-3 complets, TEST 4 coupé en plein texte) crée une fausse confiance. Implémenter une vérification stricte : tous les tests doivent produire une sortie COMPLÈTE et TERMINÉE, pas juste 'partiellement exécutés'. Ajouter un marqueur de fin explicite (ex: '=== ALL TESTS COMPLETED ===') pour détecter les troncatures.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 5 — optimization
**Contexte** : Task: Créer un utilitaire de résumé de texte
**Learning** : La consultation des learnings existants (itérations 1-4) n'a pas été appliquée avant l'itération 5. Créer une étape OBLIGATOIRE et tracée : (1) Lire les learnings pertinents, (2) Lister explicitement lesquels s'appliquent à la tâche actuelle, (3) Intégrer chacun dans la checklist pré-soumission. Cela aurait évité la répétition du pattern 'troncature masquée par docstring'.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 5 — success_pattern
**Contexte** : Task: Créer un utilitaire de résumé de texte
**Learning** : Isoler et tester le cœur métier (split phrases → scoring → extraction) comme fonctions séparées AVANT intégration dans la fonction principale. Cela permet de détecter les troncatures dans les sections critiques et de valider chaque étape indépendamment.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 5 — gotcha
**Contexte** : Task: Créer un utilitaire de résumé de texte
**Learning** : La checklist pré-soumission doit être multi-niveaux et strictement ordonnée : (1) Syntaxe (python -m py_compile), (2) Import (import du module), (3) Exécution simple (appel basique), (4) Exécution complète (tous les cas limites), (5) Vérification de non-troncature (sortie complète, pas de variables non-assignées). Sauter une étape masque les erreurs.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 6 — gotcha
**Contexte** : Task: Créer un utilitaire de résumé de texte
**Learning** : Les troncatures d'exécution se cachent souvent dans les docstrings ou les sorties partielles de tests. Implémenter une vérification stricte : chaque étape critique doit produire un marqueur de fin explicite (ex: '=== STEP_NAME COMPLETED ===') et vérifier que le fichier généré est complet via `wc -l` ou hash de contenu attendu.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 6 — failure_analysis
**Contexte** : Task: Créer un utilitaire de résumé de texte
**Learning** : L'absence de validation intermédiaire entre création et test masque les défaillances. Ajouter une étape obligatoire post-création : (1) Vérifier le fichier existe et n'est pas vide, (2) Compiler/parser le code, (3) Importer le module, (4) Exécuter une fonction simple, (5) Exécuter les cas limites. Chaque étape doit être loggée avec succès/échec explicite.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 6 — optimization
**Contexte** : Task: Créer un utilitaire de résumé de texte
**Learning** : Consulter et appliquer les learnings existants AVANT de commencer la phase AGIR. Créer une étape tracée : (1) Lister les learnings pertinents, (2) Mapper chacun à une action concrète dans la checklist, (3) Ajouter une ligne 'Learning X appliqué : [description]' dans la soumission. Cela évite les répétitions de patterns d'erreur.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 6 — success_pattern
**Contexte** : Task: Créer un utilitaire de résumé de texte
**Learning** : Tester les composants critiques isolément avant intégration. Pour un résumé de texte : (1) Tester split_sentences() sur 5 cas (vide, une phrase, ponctuation mixte, etc.), (2) Tester score_sentence() sur phrases isolées, (3) Tester summarize() sur textes complets. Chaque test doit afficher input → output complet, pas juste 'OK'.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 6 — gotcha
**Contexte** : Task: Créer un utilitaire de résumé de texte
**Learning** : Les sorties tronquées au milieu d'une chaîne (ex: 'This is a shor') indiquent souvent un dépassement de limite de tokens ou une exception non capturée. Ajouter un try-except global avec logging du traceback complet, et limiter les outputs de test à des tailles prévisibles (max 500 chars par test).
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 7 — failure_analysis
**Contexte** : Task: Créer un utilitaire de résumé de texte
**Learning** : Les troncatures de sortie mid-word (ex: 'Machine learn' au lieu d'un résumé complet) indiquent une erreur d'écriture fichier ou une exception silencieuse. Ajouter une validation post-écriture : (1) Vérifier que le fichier n'est pas vide, (2) Lire et afficher les 100 premiers et 100 derniers caractères, (3) Valider que les fonctions critiques sont complètes (chercher 'return' dans chaque fonction).
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 7 — success_pattern
**Contexte** : Task: Créer un utilitaire de résumé de texte
**Learning** : Tester chaque composant isolément AVANT intégration, avec affichage complet input→output. Pour summarize.py : (1) split_sentences() sur 5 cas (vide, 1 phrase, ponctuation mixte, nombres, guillemets), (2) score_sentence() sur 3 phrases isolées avec scores attendus, (3) summarize() sur 2 textes courts (< 200 chars) avec output complet visible. Chaque test doit logguer le type et la longueur de l'input.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 7 — gotcha
**Contexte** : Task: Créer un utilitaire de résumé de texte
**Learning** : Les cas limites (texte vide, une phrase, très long texte) doivent être testés EXPLICITEMENT et loggués. Ajouter une étape 'Edge cases validation' : (1) Texte vide → résumé vide, (2) Une phrase → résumé = phrase, (3) Texte > 1000 chars → résumé < 50% original. Chaque cas doit afficher assertion + résultat réel.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 7 — optimization
**Contexte** : Task: Créer un utilitaire de résumé de texte
**Learning** : Appliquer les learnings existants AVANT AGIR : créer une checklist tracée qui mappe chaque learning à une action. Exemple : 'Learning validation_intermédiaire appliqué : 5 étapes de validation post-création exécutées et loggées'. Cela force la réutilisation et crée une trace d'audit.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 7 — failure_analysis
**Contexte** : Task: Créer un utilitaire de résumé de texte
**Learning** : Les logs incomplets (étapes 4-5 manquantes) indiquent une troncature de sortie ou un crash non capturé. Ajouter un wrapper try-except global autour de chaque étape de validation avec logging du traceback complet. Limiter chaque log à 1000 chars max pour éviter les dépassements de tokens.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 8 — success_pattern
**Contexte** : Task: Créer un utilitaire de résumé de texte
**Learning** : Une architecture modulaire avec fonctions isolées (split_sentences, score_sentence, summarize) + suite de validation intégrée (5 étapes tracées) + tests pytest complets (34 tests) = score 85/100. Pattern : décomposer, valider chaque composant, puis intégrer avec logs explicites.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 8 — gotcha
**Contexte** : Task: Créer un utilitaire de résumé de texte
**Learning** : Les cas limites testés explicitement (texte vide, 1 phrase, >1000 chars) avec assertions loggées préviennent les bugs en production. Ajouter systématiquement une étape 'Edge cases validation' AVANT de déclarer une tâche complète.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 8 — optimization
**Contexte** : Task: Créer un utilitaire de résumé de texte
**Learning** : La heuristique de scoring basique (longueur + densité mots-clés) fonctionne mais TF-IDF améliorerait la qualité. Pour itérations futures : commencer simple, mesurer, puis sophistiquer. Documenter le seuil de complexité où l'amélioration justifie le coût.
**Confiance** : moyenne
**Utilisations** : 0

### [2026-04-03] Iteration 8 — failure_analysis
**Contexte** : Task: Créer un utilitaire de résumé de texte
**Learning** : Absence de gestion explicite des doublons de phrases dans le résumé = bug potentiel sur textes répétitifs. Ajouter une étape de déduplication post-sélection. Tester avec textes contenant phrases identiques ou très similaires.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 8 — optimization
**Contexte** : Task: Créer un utilitaire de résumé de texte
**Learning** : Absence de benchmarks de performance sur textes volumineux (>10k chars) = risque de dégradation en production. Ajouter une étape de profiling : mesurer temps d'exécution et mémoire sur 3 tailles (100, 1000, 10000 chars).
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 8 — success_pattern
**Contexte** : Task: Créer un utilitaire de résumé de texte
**Learning** : Logs explicites avec type + longueur d'input pour chaque composant testé isolément = traçabilité complète. Pattern : logguer (1) input type/size, (2) processing step, (3) output type/size, (4) assertion result.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 9 — failure_analysis
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : ModuleNotFoundError sur import = signal d'arrêt immédiat. Avant d'écrire des tests, valider que le module source existe et est importable. Ajouter une étape 'Import validation' : créer un fichier test minimal qui importe uniquement le module, l'exécuter, puis procéder aux tests complets.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 9 — gotcha
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : Générer 34 tests sans exécution préalable = risque de fichier incomplet ou mal formé. Pattern sûr : générer par blocs de 5-8 tests, exécuter immédiatement, valider la syntaxe et l'import, puis continuer. Évite les fichiers tronqués et les erreurs de masse.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 9 — failure_analysis
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : Fichier test coupé au milieu de test_empty_text indique une génération interrompue ou un buffer overflow. Toujours vérifier la complétude du fichier généré : compter les def test_*, vérifier la fermeture des fonctions, valider la syntaxe avec ast.parse() avant commit.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 9 — success_pattern
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : Structure pytest visible (logging explicite, isolation des composants) = bonne intention. Mais structure seule ne suffit pas sans exécution. Pattern : (1) générer structure, (2) exécuter immédiatement, (3) corriger erreurs, (4) valider couverture. Ordre critique.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 9 — optimization
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : Couverture de 34 tests sur un utilitaire simple = sur-ingénierie probable. Évaluer le ratio : pour un module <200 LOC, 8-12 tests bien ciblés suffisent. Ajouter une étape 'Test count justification' : documenter pourquoi chaque test existe.
**Confiance** : moyenne
**Utilisations** : 0

### [2026-04-03] Iteration 10 — failure_analysis
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : Avant de générer des tests, valider que le module source existe et est importable. Créer un fichier test minimal (import uniquement) et l'exécuter d'abord. Cela détecte les erreurs de chemin ou de structure avant d'investir dans la génération complète.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 10 — gotcha
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : Générer des tests par blocs de 5-8 avec exécution immédiate après chaque bloc. Évite les fichiers tronqués, les erreurs de syntaxe massives, et permet de corriger les erreurs d'import avant de continuer. La génération monolithique de 34 tests sans validation = risque critique.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 10 — failure_analysis
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : Valider la complétude du fichier généré : compter les `def test_*`, vérifier la fermeture des fonctions, exécuter `ast.parse()` sur le fichier avant commit. Détecte les troncatures et les erreurs de syntaxe silencieuses.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 10 — optimization
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : Pour un module <200 LOC, 8-12 tests bien ciblés suffisent. Avant de générer 34 tests, justifier le nombre : documenter le ratio tests/LOC et l'intention de chaque test. Évite la sur-ingénierie et réduit le temps de maintenance.
**Confiance** : moyenne
**Utilisations** : 0

### [2026-04-03] Iteration 10 — success_pattern
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : Structure pytest bien intentionnée (logging, isolation) ne suffit pas sans exécution. Pattern obligatoire : (1) générer structure, (2) exécuter immédiatement, (3) corriger erreurs, (4) valider couverture. L'ordre est critique.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 1 — failure_analysis
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : Valider l'importabilité du module source AVANT toute génération de tests. Créer un fichier test minimal contenant uniquement l'import et l'exécuter. Cela détecte les erreurs de chemin (ex: 'from summarize' vs 'from tools.summarize') sans investir dans la génération complète.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 1 — gotcha
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : Ne pas générer de fichiers tests monolithiques sans points de validation intermédiaires. Générer par blocs de 5-8 tests, exécuter immédiatement après chaque bloc avec pytest, corriger les erreurs avant de continuer. Cela prévient les fichiers tronqués et les erreurs de syntaxe massives.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 1 — success_pattern
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : Valider la complétude syntaxique du fichier généré avant commit : (1) compter les 'def test_*' vs le nombre planifié, (2) vérifier la fermeture de toutes les fonctions, (3) exécuter ast.parse() sur le fichier. Cela détecte les troncatures silencieuses.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 1 — optimization
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : Pour un module <200 LOC, 8-12 tests bien ciblés suffisent. Avant de générer 34 tests, documenter le ratio tests/LOC et l'intention de chaque test. Évite la sur-ingénierie et réduit le temps de maintenance.
**Confiance** : moyenne
**Utilisations** : 0

### [2026-04-03] Iteration 1 — failure_analysis
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : Un score déclinant (64.8 → 20) sans ajustement de stratégie indique une escalade d'erreurs. Implémenter un seuil d'alerte : si score < 50, arrêter la génération monolithique et basculer immédiatement en mode itératif par blocs.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 2 — gotcha
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : Valider l'importabilité du module source AVANT toute génération de tests. Créer un fichier test minimal (3-5 lignes) contenant uniquement l'import et l'exécuter avec pytest. Cela détecte les erreurs de chemin sans investir dans la génération complète.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 2 — failure_analysis
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : Un fichier généré tronqué (code cassé, fonction incomplète) indique un dépassement de limite de tokens ou une interruption du modèle. Implémenter une vérification post-génération : (1) ast.parse() pour valider la syntaxe, (2) compter les 'def test_' vs le nombre planifié, (3) vérifier la fermeture de la dernière fonction. Rejeter et régénérer par blocs si validation échoue.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 2 — optimization
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : Pour un module <200 LOC, générer 8-12 tests ciblés en 2-3 blocs de 4-5 tests chacun, exécuter après chaque bloc. Cela prévient les fichiers monolithiques tronqués et permet de corriger les erreurs d'import/syntaxe avant d'investir dans la suite complète.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 2 — failure_analysis
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : Un score déclinant (64.8 → 30) sans ajustement de stratégie indique une escalade d'erreurs. Seuil d'alerte : si score < 50 après une itération, arrêter immédiatement la génération monolithique et basculer en mode itératif par blocs avec validation intermédiaire.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 2 — gotcha
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : Ne pas générer de fichiers tests sans points de validation intermédiaires. Générer par blocs de 4-5 tests, exécuter immédiatement avec pytest, corriger les erreurs avant de continuer. Cela prévient les fichiers tronqués et les erreurs de syntaxe massives.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 3 — failure_analysis
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : Un score de 20/100 avec erreur 'No module named summarize' indique que la validation de structure du projet (existence de tools/, __init__.py, chemin d'import correct) doit précéder la génération de tests. Avant d'écrire un test, exécuter un import de vérification minimal : créer un stub test qui importe uniquement le module cible, le lancer avec pytest, et valider que l'import réussit.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 3 — gotcha
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : Un fichier test tronqué (ligne 'ass' incomplète, fonction non fermée) combiné à 'collected 0 items' signale que la génération s'est arrêtée avant la fin. Toujours valider la syntaxe avec ast.parse() immédiatement après génération. Si la validation échoue, régénérer par blocs de 3-4 tests max, exécuter après chaque bloc, et fusionner seulement après succès.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 3 — optimization
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : Après un score < 50, basculer immédiatement en mode itératif : générer 3-4 tests, exécuter avec pytest, corriger les erreurs d'import/syntaxe, puis continuer. Ne pas tenter de générer 8-12 tests d'un coup si la structure du projet n'est pas validée. Cela réduit le risque de fichiers cassés et permet de détecter les problèmes de chemin d'import avant d'investir dans la suite.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 3 — failure_analysis
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : L'absence de vérification préalable de la structure du projet (répertoire tools/, __init__.py, accessibilité du module) a causé une génération de tests inutilisables. Créer une checklist pré-génération : (1) ls -la tools/, (2) cat tools/__init__.py, (3) python -c 'import tools.summarize' pour valider l'import. Échouer fast si la structure est manquante.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 4 — failure_analysis
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : Un fichier test tronqué (dernière assertion non fermée) combiné à un conflit d'import dans un autre fichier test crée un INTERNALERROR pytest qui empêche la collecte complète. Toujours valider la syntaxe avec ast.parse() ET exécuter pytest en mode verbose (pytest -v --tb=short) pour identifier les erreurs de collecte avant d'itérer.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 4 — gotcha
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : Un fichier test_import_validation.py avec un import incorrect (from summarize au lieu de from tools.summarize) peut bloquer la collecte de TOUS les tests du répertoire, même ceux syntaxiquement corrects. Avant de générer de nouveaux tests, nettoyer ou corriger les fichiers test existants qui pourraient avoir des imports cassés.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 4 — optimization
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : Après un score < 50 avec 'collected 0 items', ne pas régénérer le même fichier en entier. À la place : (1) identifier le fichier tronqué avec wc -l et tail, (2) corriger ou supprimer les fichiers test cassés existants, (3) générer 3-4 tests seulement, (4) valider syntaxe + exécution avant d'ajouter plus.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 4 — failure_analysis
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : La critique mentionne 'couverture des cas limites est conceptuellement bonne mais reste théorique' : cela signifie que les tests ont été générés mais jamais exécutés. Valider que pytest peut au minimum collecter et exécuter un test vide (def test_placeholder(): pass) avant de générer la suite complète.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 4 — success_pattern
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : La structure du code test (classes, docstrings, assertions claires) était correcte : le problème était purement technique (syntaxe tronquée + import cassé). Cela confirme que la stratégie de génération est bonne ; il faut juste ajouter une étape de validation post-génération avant de déclarer succès.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 5 — failure_analysis
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : Quand pytest retourne 'collected 0 items' + 'No module named X', vérifier d'abord l'existence du module source avant de blâmer le test. Utiliser 'python -c "import tools.summarize"' pour valider l'import avant de générer des tests.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 5 — gotcha
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : Un fichier test tronqué (dernière méthode incomplète : 'def test_split_empty_string(self): """Test s') dans le même répertoire peut être silencieusement ignoré par pytest lors de la collecte, masquant le vrai problème. Toujours vérifier 'tail -20 test_*.py' après génération.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 5 — optimization
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : Avant de régénérer un fichier test complet après un échec, exécuter : (1) 'ls -la tests/' pour lister les fichiers, (2) 'wc -l test_*.py' pour détecter les fichiers tronqués, (3) 'python -m py_compile test_*.py' pour valider la syntaxe. Supprimer ou corriger les fichiers cassés AVANT nouvelle génération.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 5 — success_pattern
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : La structure logique des tests (classes, docstrings, assertions) était correcte en itération 4 : le problème était purement technique (fichier tronqué + import cassé). Réutiliser la même structure de génération mais ajouter une étape de validation post-génération : exécuter 'pytest --collect-only' et vérifier que le nombre de tests collectés > 0.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 5 — optimization
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : Après génération, exécuter immédiatement 'pytest tests/test_*.py -v --tb=short' avec un timeout court (5s). Si 'collected 0 items', arrêter et diagnostiquer avant itération suivante. Ne pas ajouter plus de tests tant que la collecte échoue.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 6 — failure_analysis
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : ModuleNotFoundError lors de pytest indique un problème de PYTHONPATH ou de structure du projet, pas une erreur de test. Avant de régénérer des tests, exécuter: (1) 'python -c "import sys; print(sys.path)"' pour vérifier le chemin, (2) 'ls -la' pour confirmer la structure (tools/ doit être au même niveau que tests/), (3) 'python -m pytest --collect-only tests/' pour diagnostiquer l'import avant l'exécution.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 6 — gotcha
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : Un fichier test tronqué (dernière méthode incomplète) peut coexister avec un nouveau fichier généré. Avant de générer tests/test_summarize.py, exécuter: 'rm -f tests/test_summarize.py' ou 'git status tests/' pour détecter les fichiers partiels. Vérifier 'tail -5 tests/test_summarize.py' après génération pour confirmer que le fichier se termine par une ligne complète (pas de 'def test_' orphelin).
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 6 — optimization
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : Ajouter une étape de validation post-génération obligatoire: (1) 'python -m py_compile tests/test_summarize.py' pour valider la syntaxe, (2) 'pytest tests/test_summarize.py --collect-only -q' pour vérifier que N tests sont collectés (N > 0), (3) 'pytest tests/test_summarize.py -v --tb=line' avec timeout 10s. Si collecte = 0 ou import échoue, arrêter et diagnostiquer AVANT itération suivante.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 6 — success_pattern
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : La structure logique des tests (classes TestSummarize, TestSplitSentences avec docstrings et assertions) était correcte. Le problème était technique (import + fichier tronqué). Réutiliser la même structure de génération mais ajouter la validation post-génération. Ne pas modifier la logique des tests, corriger l'environnement d'exécution.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 6 — optimization
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : Avant de générer un nouveau fichier test, exécuter: 'git diff tests/test_summarize.py' ou 'git status tests/' pour voir si le fichier existe et son état. Si le fichier est partiellement commité ou tronqué, faire 'git checkout tests/test_summarize.py' ou 'rm tests/test_summarize.py' pour repartir de zéro.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 7 — failure_analysis
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : Les tests bien structurés (classes, docstrings, assertions) ne suffisent pas si le module importé n'existe pas ou n'est pas accessible. Avant de générer des tests, vérifier que le module cible existe: 'python -c "import tools.summarize; print(tools.summarize.__file__)"'. Si import échoue, diagnostiquer et corriger le module AVANT d'écrire les tests.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 7 — gotcha
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : Une race condition peut survenir si un fichier test est supprimé (rm) juste avant la compilation/validation. Le fichier peut être en cours d'écriture ou partiellement supprimé. Solution: utiliser 'git clean -fd tests/' ou 'git checkout tests/' pour nettoyer de manière atomique, plutôt que 'rm -f' suivi d'une génération.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 7 — optimization
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : Les assertions faibles ('assert len(result) >= 1') masquent les bugs. Remplacer par des assertions spécifiques: vérifier le contenu exact, la structure, les cas limites (texte très long, max_sentences=1, caractères spéciaux). Générer des tests avec assertions fortes dès le départ plutôt que de les renforcer après.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 7 — optimization
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : Après génération d'un fichier test, exécuter une validation en trois étapes: (1) 'python -m py_compile' pour syntaxe, (2) 'pytest --collect-only -q' pour vérifier N > 0 tests collectés, (3) 'pytest -v --tb=line' avec timeout. Si l'une échoue, arrêter et diagnostiquer AVANT de continuer. Cela détecte les imports cassés et les fichiers tronqués immédiatement.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 7 — success_pattern
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : La structure logique des tests (classes par fonctionnalité, docstrings claires, assertions organisées) était correcte. Le problème était environnemental (import + fichier tronqué). Réutiliser la même structure de génération mais ajouter la validation post-génération obligatoire. Ne pas modifier la logique, corriger l'exécution.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 8 — failure_analysis
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : Les erreurs d'import (ImportError, INTERNALERROR) indiquent une désynchronisation entre la structure du projet et les chemins d'import dans les tests. Avant de générer des tests, valider la structure réelle du projet avec 'find . -name "*.py" -type f' et 'python -c "import sys; print(sys.path)"' pour garantir que les imports correspondent à la réalité.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 8 — gotcha
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : Les fichiers test tronqués (assertion coupée à 'assert len') peuvent résulter d'une interruption lors de l'écriture ou d'une limite de buffer. Toujours vérifier la complétude du fichier généré avec 'tail -5 <file>' et 'wc -l <file>' immédiatement après génération, avant validation.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 8 — optimization
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : La validation post-génération en trois étapes (syntaxe → collection → exécution) doit être obligatoire et atomique. Si une étape échoue, générer un rapport diagnostic détaillé (erreur exacte, ligne, contexte) AVANT de relancer la génération. Cela réduit les cycles d'itération.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 8 — success_pattern
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : La structure logique des tests (classes par fonctionnalité, docstrings, assertions organisées) était correcte. Les problèmes étaient environnementaux (import + fichier tronqué). Séparer la validation de la logique : réutiliser la même structure de génération mais ajouter une étape de diagnostic d'environnement préalable.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 8 — failure_analysis
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : Un score partiel (45/100) avec tests collectés mais non exécutables indique que la génération a réussi mais l'intégration a échoué. Distinguer clairement : (1) génération correcte, (2) intégration cassée. Cela permet de cibler le diagnostic (code vs environnement).
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 9 — failure_analysis
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : Un score partiel (45/100) avec tests syntaxiquement valides mais non exécutables révèle une séparation claire entre génération de code et intégration environnementale. Toujours diagnostiquer en trois étapes : (1) syntaxe Python valide, (2) imports résolus, (3) exécution réelle. Échouer à l'étape 2 signifie que le chemin d'import ne correspond pas à la structure réelle du projet.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 9 — gotcha
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : Les fichiers tronqués (ici 'def test_max_' incomplet) peuvent masquer des problèmes d'import qui ne se manifestent qu'à l'exécution. Vérifier la complétude avec 'tail -20 <file>' ET 'python -m py_compile <file>' immédiatement après génération. Un fichier syntaxiquement valide mais tronqué peut passer la compilation mais échouer à l'import.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 9 — optimization
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : Avant de générer des tests, valider que le module à tester existe et est importable. Ajouter une étape de diagnostic préalable : 'python -c "import tools.summarize; print(dir(tools.summarize))"'. Cela évite de générer 7 cas de test corrects mais inutilisables.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 9 — success_pattern
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : La structure logique des tests (4 classes, docstrings, assertions organisées) était correcte et réutilisable. Le problème n'était pas la conception mais l'environnement. Conserver cette structure pour les itérations futures : elle démontre une bonne compréhension de la couverture de test (cas vides, texte court/long, paramètres limites).
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 9 — failure_analysis
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : Un fichier tronqué à 'def test_max_' suggère une interruption lors de l'écriture ou une limite de buffer. Cela n'a pas été détecté car la validation s'est arrêtée à la syntaxe (fichier valide jusqu'à la troncature). Ajouter une vérification de cohérence : tous les 'def' doivent avoir un corps complet, pas de 'def' sans 'assert' ou 'pass'.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 10 — failure_analysis
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : Les fichiers tronqués (dernière ligne incomplète) passent la validation syntaxique jusqu'au point de troncature mais échouent à l'exécution. Vérifier systématiquement la complétude avec 'tail -5 <file>' ET 'python -m py_compile <file>' ET une exécution partielle (import + inspection) immédiatement après génération.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 10 — gotcha
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : Une incohérence entre le nombre de tests collectés (11) et le nombre final (13) indique soit une duplication, soit une génération partielle non détectée. Toujours comparer 'pytest --collect-only' avant et après génération pour valider la cohérence.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 10 — optimization
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : Avant de générer des tests, valider l'importabilité du module cible avec 'python -c "import <module>; print(dir(<module>))"'. Cela évite de générer une suite de tests complète mais inutilisable faute de module accessible.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 10 — success_pattern
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : La structure logique des tests (classes organisées par cas d'usage, docstrings explicites, assertions claires) était correcte conceptuellement. Réutiliser ce pattern : 4 classes (Empty, Short, Long, EdgeCases), chacune avec 2-3 assertions ciblées. Le problème était l'exécution, pas la conception.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 10 — failure_analysis
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : L'absence de rapport de couverture de code (critère d'acceptation non satisfait) indique que les tests n'ont jamais été exécutés avec succès. Ajouter une étape de validation : 'pytest --cov=<module> --cov-report=term-missing' doit produire un rapport avant de considérer la tâche complète.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 10 — gotcha
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : Un fichier peut être importable mais non exécutable si une fonction est tronquée (ex: 'def test_max_' sans corps). La compilation Python ne détecte pas cela. Ajouter une vérification : tous les 'def' doivent être suivis d'au moins une ligne indentée (assertion, pass, ou docstring).
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 1 — failure_analysis
**Contexte** : Task: Améliorer le résumé avec un scoring TF-IDF simplifié
**Learning** : Un fichier généré peut être syntaxiquement valide mais fonctionnellement incomplet si une fonction est tronquée au milieu. Valider la complétude en exécutant 'python -m py_compile <file>' puis 'python -c "import <module>; [getattr(<module>, name) for name in dir(<module>) if not name.startswith(\"_\")]"' pour vérifier que toutes les fonctions attendues existent et sont appelables.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 1 — gotcha
**Contexte** : Task: Améliorer le résumé avec un scoring TF-IDF simplifié
**Learning** : Les critères d'acceptation 'les tests existants passent toujours' doivent être vérifiés AVANT de générer du code nouveau. Exécuter 'pytest --collect-only' et 'pytest' sur l'état initial, puis comparer après génération. Une rupture d'imports (fonctions manquantes) invalide immédiatement la solution même si le code nouveau est de bonne qualité.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 1 — optimization
**Contexte** : Task: Améliorer le résumé avec un scoring TF-IDF simplifié
**Learning** : Avant de générer du code complétant une implémentation, vérifier l'état des imports avec 'grep -n "^from\|^import" <test_file>' et croiser avec 'python -c "import <module>; print([x for x in dir(<module>) if not x.startswith(\"_\")])"'. Cela identifie les fonctions manquantes et évite de générer du code qui ne sera jamais testé.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 1 — failure_analysis
**Contexte** : Task: Améliorer le résumé avec un scoring TF-IDF simplifié
**Learning** : La qualité algorithmique du code (TF-IDF correct, logique valide) ne compense pas une implémentation inachevée. Un score de 42/100 avec 'code écrit est bon' mais 'implémentation inachevée' indique que la complétude prime sur la qualité partielle. Toujours générer jusqu'au bout, même si cela signifie ajouter des stubs ou des pass.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 2 — failure_analysis
**Contexte** : Task: Améliorer le résumé avec un scoring TF-IDF simplifié
**Learning** : Un fichier Python peut passer la validation syntaxique (py_compile) mais rester non-importable si une fonction est tronquée au milieu de sa définition. Toujours exécuter 'python -c "import <module>; print([x for x in dir(<module>) if not x.startswith(\"_\")])"' après génération pour vérifier que toutes les fonctions attendues sont présentes et complètes, pas seulement syntaxiquement valides.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 2 — gotcha
**Contexte** : Task: Améliorer le résumé avec un scoring TF-IDF simplifié
**Learning** : Les tests importent des fonctions helper (split_sentences, score_sentence) qui doivent exister dans le module cible. Une rupture d'imports invalide immédiatement la solution même si le code nouveau est algorithmiquement correct. Vérifier systématiquement 'grep "from.*import\|import" <test_file>' et croiser avec les exports du module AVANT de déclarer la tâche complète.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 2 — optimization
**Contexte** : Task: Améliorer le résumé avec un scoring TF-IDF simplifié
**Learning** : Lors de l'amélioration d'un module existant, exécuter d'abord 'pytest --collect-only' et 'pytest' sur l'état initial pour établir une baseline. Après génération, re-exécuter les mêmes tests et comparer. Cela détecte immédiatement les régressions d'imports ou de signatures de fonction.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 2 — failure_analysis
**Contexte** : Task: Améliorer le résumé avec un scoring TF-IDF simplifié
**Learning** : Une implémentation inachevée (fichier coupé au milieu) est un FAIL critique même si le code visible est de bonne qualité. La complétude prime sur la qualité partielle. Générer toujours jusqu'au bout : ajouter des stubs, des pass, ou des ellipsis plutôt que de laisser une fonction tronquée.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 2 — optimization
**Contexte** : Task: Améliorer le résumé avec un scoring TF-IDF simplifié
**Learning** : Après génération d'un fichier Python, valider en deux étapes : (1) 'python -m py_compile <file>' pour la syntaxe, (2) 'python -c "import <module>; [getattr(<module>, name) for name in [\"split_sentences\", \"score_sentence\", ...]]"' pour vérifier que les fonctions attendues sont présentes et appelables. Cela prend <1s et élimine les faux positifs.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 3 — failure_analysis
**Contexte** : Task: Améliorer le résumé avec un scoring TF-IDF simplifié
**Learning** : Un code avec tests passants (44/44) mais verdict PARTIAL indique que les tests ne couvrent PAS la logique complète. Avant de déclarer succès, vérifier que les tests exercent TOUS les chemins critiques de la fonction principale. Ajouter des assertions sur les outputs réels (ex: vérifier que summarize() retourne effectivement un résumé, pas juste une liste vide ou un stub).
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 3 — optimization
**Contexte** : Task: Améliorer le résumé avec un scoring TF-IDF simplifié
**Learning** : Après génération d'une fonction multi-étapes (ex: summarize avec tri + sélection + réassemblage), valider la complétude en exécutant un test manuel simple : appeler la fonction avec un input connu et vérifier que l'output a la forme attendue (ex: len(output) > 0, type(output) == str). Cela détecte les implémentations tronquées avant soumission.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 3 — gotcha
**Contexte** : Task: Améliorer le résumé avec un scoring TF-IDF simplifié
**Learning** : Un commentaire 'TODO' ou 'Select top sentences...' dans le code généré est un RED FLAG : il signale une intention non implémentée. Lors de la relecture du code généré, chercher systématiquement les patterns ['# TODO', '# FIXME', 'pass', '...'] et les traiter comme des blockers avant soumission.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 3 — optimization
**Contexte** : Task: Améliorer le résumé avec un scoring TF-IDF simplifié
**Learning** : Pour une tâche d'amélioration algorithmique (ex: TF-IDF), générer d'abord une version COMPLÈTE et BASIQUE (même si naïve), puis itérer sur la qualité (normalisation, stop-words, etc.). Ne pas sacrifier la complétude pour la sophistication. Une implémentation basique complète > une implémentation sophistiquée tronquée.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 4 — failure_analysis
**Contexte** : Task: Améliorer le résumé avec un scoring TF-IDF simplifié
**Learning** : Un fichier généré incomplet (coupé au milieu d'une fonction) passe la validation manuelle mais échoue les tests existants. Avant soumission, vérifier que le fichier est complet : compter les parenthèses/accolades ouvertes/fermées, vérifier qu'aucune fonction n'est tronquée, et exécuter au minimum un import test (try: from module import *) pour détecter les erreurs de syntaxe.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 4 — failure_analysis
**Contexte** : Task: Améliorer le résumé avec un scoring TF-IDF simplifié
**Learning** : Une rupture entre l'interface attendue (tests qui importent split_sentences, score_sentence) et l'implémentation (fonctions non exportées ou manquantes) bloque l'exécution. Avant de coder, extraire la signature des tests existants et générer EXACTEMENT les fonctions attendues avec les bons noms et visibilité (public vs private).
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 4 — gotcha
**Contexte** : Task: Améliorer le résumé avec un scoring TF-IDF simplifié
**Learning** : Un code 'fonctionnellement correct' (validation manuelle OK) mais 'structurellement incomplet' (fichier tronqué) reçoit un score FAIL. La validation manuelle ne suffit pas : elle doit être complétée par (1) vérification de complétude syntaxique, (2) exécution des tests existants, (3) vérification que toutes les fonctions helper attendues sont présentes et exportées.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 4 — optimization
**Contexte** : Task: Améliorer le résumé avec un scoring TF-IDF simplifié
**Learning** : Après génération d'un algorithme complexe (TF-IDF), ajouter une étape de vérification : (1) lister toutes les fonctions appelées dans la fonction principale, (2) vérifier que chacune est définie et complète, (3) exécuter un test d'intégration simple (ex: summarize(sample_text) retourne str non-vide). Cela détecte les dépendances manquantes avant soumission.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 5 — gotcha
**Contexte** : Task: Améliorer le résumé avec un scoring TF-IDF simplifié
**Learning** : Un fichier Python tronqué (fonction incomplète) peut passer la validation manuelle mais échouer les tests. Avant soumission, vérifier la complétude syntaxique : (1) compter parenthèses/accolades ouvertes vs fermées, (2) vérifier que chaque fonction a un corps complet (pas de ligne 'word_freq = ...' sans suite), (3) exécuter 'python -m py_compile' pour détecter les erreurs de syntaxe.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 5 — failure_analysis
**Contexte** : Task: Améliorer le résumé avec un scoring TF-IDF simplifié
**Learning** : Un self-test rapporté comme 'OK' est non-fiable si le code généré est incomplet. Le test peut avoir été exécuté sur une version antérieure ou partielle. Toujours re-exécuter les tests APRÈS génération finale, et vérifier que tous les items collectés passent (ne pas se fier au nombre de items collectés seul).
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 5 — optimization
**Contexte** : Task: Améliorer le résumé avec un scoring TF-IDF simplifié
**Learning** : Après génération d'une fonction principale complexe, ajouter une étape de vérification de dépendances : (1) lister toutes les fonctions appelées (split_sentences, score_sentence, get_word_frequencies, etc.), (2) vérifier que chacune est définie ET complète, (3) exécuter un test d'intégration minimal (ex: summarize(sample_text) retourne str non-vide et len > 0). Cela détecte les appels à des fonctions manquantes ou tronquées.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 5 — failure_analysis
**Contexte** : Task: Améliorer le résumé avec un scoring TF-IDF simplifié
**Learning** : La rupture entre interface attendue (tests qui importent split_sentences, score_sentence) et implémentation (fonctions non exportées ou tronquées) bloque l'exécution. Avant de coder, extraire les signatures des tests existants (grep 'from tools.summarize import' ou 'import tools.summarize') et générer EXACTEMENT les fonctions attendues avec les bons noms et visibilité (public vs private).
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 5 — gotcha
**Contexte** : Task: Améliorer le résumé avec un scoring TF-IDF simplifié
**Learning** : Un rapport de test tronqué (pytest rapporte '44 items collectés' mais résultat coupé) masque les vrais résultats. Toujours vérifier que le rapport de test est complet : chercher la ligne 'passed/failed/error' finale. Si elle manque, le test n'a pas terminé correctement et le code est suspect.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 1 — failure_analysis
**Contexte** : Task: Améliorer le résumé avec un scoring TF-IDF simplifié
**Learning** : Une fonction principale incomplète (qui s'arrête sans retourner) passe les tests existants si ceux-ci ne vérifient que les fonctions auxiliaires. Toujours ajouter un test d'intégration end-to-end qui appelle la fonction principale et valide sa sortie complète (type, longueur, contenu non-vide).
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 1 — gotcha
**Contexte** : Task: Améliorer le résumé avec un scoring TF-IDF simplifié
**Learning** : Un scoring TF-IDF sans pondération positionnelle (début/fin du texte) produit des résumés sous-optimaux. Les phrases d'introduction et de conclusion ont une valeur informationnelle intrinsèque indépendante de la fréquence des mots. Intégrer un facteur de position (ex: +20% pour phrases 0-2 et dernière phrase) dans le scoring.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 1 — failure_analysis
**Contexte** : Task: Améliorer le résumé avec un scoring TF-IDF simplifié
**Learning** : Une liste de stop words en anglais dans un projet français réduit la qualité du scoring TF-IDF (mots français courants non filtrés). Avant d'implémenter un scoring, vérifier la langue du corpus et utiliser des ressources linguistiques appropriées (NLTK French stopwords, ou liste custom).
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 1 — optimization
**Contexte** : Task: Améliorer le résumé avec un scoring TF-IDF simplifié
**Learning** : Ajouter des tests spécifiques pour chaque amélioration algorithmique (ex: test_tfidf_scoring_vs_baseline) avant de déclarer une tâche complète. Cela valide que l'amélioration produit effectivement un résultat mesurable (résumé plus pertinent, score plus élevé) et pas seulement du code qui compile.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 1 — gotcha
**Contexte** : Task: Améliorer le résumé avec un scoring TF-IDF simplifié
**Learning** : Les cas limites (texte vide, une seule phrase, texte très court) ne sont pas testés par défaut. Ajouter des tests explicites pour ces cas avant de finaliser. Cela prévient les crashes en production et force à définir le comportement attendu.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 1 — failure_analysis
**Contexte** : Task: Améliorer le résumé avec un scoring TF-IDF simplifié
**Learning** : Une interface attendue (signatures de fonctions importées par les tests) doit être extraite AVANT la génération. Utiliser grep/ast pour lister exactement ce qui est importé, puis générer les fonctions avec les bons noms, visibilité et signatures. Cela prévient les ruptures import/export.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 2 — failure_analysis
**Contexte** : Task: Améliorer le résumé avec un scoring TF-IDF simplifié
**Learning** : Une fonction incomplète (qui s'arrête sans return) passe la compilation mais casse l'exécution. Toujours valider que chaque fonction a un chemin de retour explicite pour tous les cas, et exécuter le code avant de le committer. Utiliser un linter (pylint, flake8) configuré pour détecter les fonctions sans return.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 2 — failure_analysis
**Contexte** : Task: Améliorer le résumé avec un scoring TF-IDF simplifié
**Learning** : Quand on modifie un module existant, extraire d'abord l'interface attendue (imports, signatures) via ast.parse() ou grep, puis générer le code en respectant cette interface. Cela prévient les ImportError et les ruptures de contrats.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 2 — gotcha
**Contexte** : Task: Améliorer le résumé avec un scoring TF-IDF simplifié
**Learning** : Les tests manuels affichés (print statements) ne valident rien. Remplacer par des assertions ou des tests unitaires avec des cas d'entrée/sortie connus. Un test manuel qui passe ne prouve pas que l'algorithme fonctionne.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 2 — optimization
**Contexte** : Task: Améliorer le résumé avec un scoring TF-IDF simplifié
**Learning** : Avant d'implémenter un scoring TF-IDF, définir explicitement : (1) la langue du corpus, (2) la liste de stop words à utiliser, (3) les cas limites (texte vide, 1 phrase, très court), (4) le test de régression (baseline vs nouvelle implémentation). Cela force la clarté et prévient les implémentations incomplètes.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 2 — gotcha
**Contexte** : Task: Améliorer le résumé avec un scoring TF-IDF simplifié
**Learning** : Un code 'bien pensé' (ex: stop words français) mais incomplet (logique TF-IDF non finalisée) est pire qu'un code simple qui marche. Prioriser la complétude et l'exécutabilité avant la sophistication.
**Confiance** : haute
**Utilisations** : 1

### [2026-04-03] Iteration 3 — failure_analysis
**Contexte** : Task: Améliorer le résumé avec un scoring TF-IDF simplifié
**Learning** : Un fichier tronqué au milieu d'une fonction (ex: 'sentence.low' inachevée) passe la validation syntaxique du parser mais casse l'exécution. Toujours exécuter le code complet après écriture avant de committer. Ajouter une étape de validation : importer le module, appeler chaque fonction exportée avec un cas trivial, vérifier qu'aucune exception n'est levée.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 3 — gotcha
**Contexte** : Task: Améliorer le résumé avec un scoring TF-IDF simplifié
**Learning** : Extraire l'interface attendue d'un module AVANT de le modifier : lister les imports, signatures de fonction, et valeurs de retour via grep ou ast.parse(). Générer le code en respectant strictement cette interface. Cela prévient les ImportError et les ruptures de contrats qui cassent les tests.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 3 — gotcha
**Contexte** : Task: Améliorer le résumé avec un scoring TF-IDF simplifié
**Learning** : Un code 'conceptuellement bon' (ex: stop words français, Counter, scoring par phrase) mais incomplet (logique non finalisée, pas de return) est pire qu'un code simple qui marche. Prioriser la complétude et l'exécutabilité avant la sophistication. Découper la tâche en étapes : (1) interface, (2) cas trivial, (3) cas complexe.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 3 — optimization
**Contexte** : Task: Améliorer le résumé avec un scoring TF-IDF simplifié
**Learning** : Avant d'implémenter un algorithme (ex: TF-IDF), définir explicitement par écrit : (1) langue du corpus, (2) ressources (stop words, tokenizer), (3) cas limites (texte vide, 1 phrase, très court), (4) test de régression (baseline vs nouvelle implémentation). Valider cette spécification avec un test unitaire avant d'écrire la logique métier.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 3 — failure_analysis
**Contexte** : Task: Améliorer le résumé avec un scoring TF-IDF simplifié
**Learning** : Les tests manuels (print statements) ne valident rien. Remplacer par des assertions ou des tests unitaires avec des cas d'entrée/sortie connus et vérifiables. Un test manuel qui passe ne prouve pas que l'algorithme fonctionne; il prouve juste que le code s'exécute sans erreur.
**Confiance** : haute
**Utilisations** : 0
