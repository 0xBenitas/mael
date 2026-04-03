# MAEL — Le Serpent Qui Se Mord La Queue

```
    ____
   /    \        MAEL = Méta-Amélioration Évolutive en Ligne
  | AGIR |
  |      |       Un programme qui s'améliore tout seul.
  | MUTER|       Il code, se note, apprend de ses erreurs,
  |      |       et change ses propres règles.
  |ÉVALUE|
   \    /
    ~~~~
  APPRENDRE
```

---

## C'est quoi MAEL ?

Imagine un stagiaire qui :
1. **Reçoit une tâche** ("crée un outil de résumé de texte")
2. **Écrit le code** tout seul
3. **Se donne une note** honnête (pas toujours bonne)
4. **Apprend de ses erreurs** et les note dans un carnet
5. **Change ses propres méthodes de travail** quand il stagne

C'est MAEL. Sauf que le stagiaire est une IA (Claude), et le carnet est un fichier `.md`.

Le twist : toutes les **5 itérations**, MAEL regarde ses notes et se demande :
> "Est-ce que ma façon de m'évaluer est bonne ? Est-ce que j'apprends les bonnes leçons ?"

Et il modifie ses propres règles. C'est la phase **Ouroboros** — le serpent se mord la queue.

---

## Comment ça marche (pour les humains)

### La boucle en 4 phases

```
┌─────────────────────────────────────────────────┐
│                                                 │
│   1. AGIR          "Je fais la tâche"           │
│      │                                          │
│      ▼                                          │
│   2. ÉVALUER       "Je me note sur 100"         │
│      │                                          │
│      ▼                                          │
│   3. APPRENDRE     "Je note ce qui a marché"    │
│      │                                          │
│      ▼                                          │
│   4. MUTER         "Je change mes règles"       │
│      │              (toutes les 5 itérations)   │
│      └──────────────────────► retour à 1.       │
│                                                 │
└─────────────────────────────────────────────────┘
```

### Exemple réel (ce qui s'est passé)

| Itération | Ce que MAEL a fait | Score | Ce qu'il a appris |
|-----------|-------------------|-------|-------------------|
| 1 | Créé summarize.py (incomplet) | 69 | "Vérifier que le code est complet avant de valider" |
| 2 | Réessayé (encore tronqué) | 55 | "Utiliser py_compile pour vérifier la syntaxe" |
| 3 | Encore raté | 55 | "Créer une checklist pré-soumission" |
| 5 | **Ouroboros** : a muté ses propres règles | - | "Mes critères étaient trop permissifs" |
| 8 | **Réussi !** (code complet + tests) | 85 | Pattern promu dans CLAUDE.md |

En 8 itérations, MAEL a :
- Écrit 236 lignes de code fonctionnel
- Accumulé 50+ règles dans sa mémoire
- Muté 3 fois ses propres critères d'évaluation

---

## Comment l'utiliser

### Pré-requis
- Python 3.11+
- Une clé API Anthropic (https://console.anthropic.com/settings/keys)

### Installation

```bash
git clone https://github.com/0xBenitas/mael.git
cd mael
pip install anthropic pytest
```

### Lancer la boucle

```bash
# 1. Mettre ta clé API dans un fichier .env (jamais sur GitHub)
echo "ANTHROPIC_API_KEY=sk-ant-ta-cle-ici" > .env

# 2. Voir l'état actuel
export $(cat .env | xargs) && python -m mael status

# 3. Lancer 10 itérations
export $(cat .env | xargs) && python -m mael run 10

# 4. Mode test (gratuit, sans API)
python -m mael run 10 --dry-run
```

### Ajouter tes propres tâches

Édite `.mael/state.json` :

```json
{
  "tasks": [
    {
      "id": 1,
      "title": "Ce que tu veux que MAEL fasse",
      "description": "Description détaillée de la tâche",
      "status": "pending",
      "acceptance": "Comment savoir si c'est réussi"
    }
  ]
}
```

Puis : `python -m mael run 20`

MAEL va essayer, échouer, apprendre, et réessayer jusqu'à réussir.

---

## Les fichiers importants

```
mael/
│
├── README.md          ← Tu es ici
├── CLAUDE.md          ← La mémoire du serpent (patterns promus)
│
├── mael/              ← Le cerveau
│   ├── engine.py      ← La boucle principale
│   ├── llm.py         ← Connexion à Claude (Haiku=pas cher, Sonnet=malin)
│   ├── prompts.py     ← Les prompts (ce que Ouroboros peut muter)
│   ├── executor.py    ← Écrit et exécute le code généré
│   ├── memory.py      ← Gère les learnings et métriques
│   ├── mutator.py     ← Le module Ouroboros
│   └── cli.py         ← Les commandes (init, run, status, reset)
│
├── .mael/             ← Les données de la boucle
│   ├── state.json     ← Les tâches et leur statut
│   ├── learnings.md   ← Ce que MAEL a appris (600+ lignes)
│   ├── metrics.json   ← Les scores de chaque itération
│   ├── mutations.md   ← Les changements de règles
│   └── logs/          ← Logs détaillés par itération
│
├── tools/             ← Code créé par MAEL
│   └── summarize.py   ← Résumeur de texte (TF-IDF)
│
└── tests/             ← 44 tests (tout passe)
```

---

## Combien ça coûte ?

| Action | Modèle | Coût |
|--------|--------|------|
| 1 itération normale | Haiku (évaluer + apprendre) | ~$0.003 |
| 1 génération de code | Sonnet (agir) | ~$0.01 |
| 1 mutation Ouroboros | Sonnet (muter) | ~$0.01 |
| **50 itérations complètes** | **Mix** | **~$0.50** |

Avec le crédit gratuit de $5 d'Anthropic, tu peux faire ~500 itérations.

---

## Le concept en une image

```
Niveau 0 : Un humain écrit du code
Niveau 1 : L'IA écrit du code
Niveau 2 : L'IA écrit du code ET s'évalue       ← Self-Refine
Niveau 3 : L'IA écrit, s'évalue ET apprend       ← MAEL
Niveau 4 : L'IA change ses propres règles         ← Ouroboros
Niveau 5 : L'IA se donne ses propres missions     ← En cours...
```

MAEL est entre le niveau 4 et 5. La prochaine étape : qu'il se donne ses propres tâches.

---

## Inspirations

- **PromptBreeder** (DeepMind) — mutation de prompts qui mutent des prompts
- **Self-Refine** — boucle generate→critique→refine
- **DSPy** (Stanford) — optimisation automatique de prompts
- **Ralph Loop** — boucle Claude Code autonome

Voir `META_ANALYSE_AUTOPROMPTING.md` pour l'analyse complète de 11 techniques.

---

## Licence

MIT — Fais ce que tu veux avec.
