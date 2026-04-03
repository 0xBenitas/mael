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
**Utilisations** : 0

### [2026-04-03] Iteration 10 — gotcha
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : Générer des tests par blocs de 5-8 avec exécution immédiate après chaque bloc. Évite les fichiers tronqués, les erreurs de syntaxe massives, et permet de corriger les erreurs d'import avant de continuer. La génération monolithique de 34 tests sans validation = risque critique.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 10 — failure_analysis
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : Valider la complétude du fichier généré : compter les `def test_*`, vérifier la fermeture des fonctions, exécuter `ast.parse()` sur le fichier avant commit. Détecte les troncatures et les erreurs de syntaxe silencieuses.
**Confiance** : haute
**Utilisations** : 0

### [2026-04-03] Iteration 10 — optimization
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : Pour un module <200 LOC, 8-12 tests bien ciblés suffisent. Avant de générer 34 tests, justifier le nombre : documenter le ratio tests/LOC et l'intention de chaque test. Évite la sur-ingénierie et réduit le temps de maintenance.
**Confiance** : moyenne
**Utilisations** : 0

### [2026-04-03] Iteration 10 — success_pattern
**Contexte** : Task: Écrire les tests pour l'utilitaire de résumé
**Learning** : Structure pytest bien intentionnée (logging, isolation) ne suffit pas sans exécution. Pattern obligatoire : (1) générer structure, (2) exécuter immédiatement, (3) corriger erreurs, (4) valider couverture. L'ordre est critique.
**Confiance** : haute
**Utilisations** : 0
