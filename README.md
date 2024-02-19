Voici un exemple de README pour votre projet depuis le début des scripts :

---

# Jeu Pierre/Feuille/Ciseaux

Ce projet implémente le célèbre jeu Pierre/Feuille/Ciseaux en Python. Le jeu est disponible en deux versions : 

1. **Version Simple** : Dans cette version, un joueur peut jouer contre un autre joueur ou contre l'ordinateur.

2. **Version Multiple** : Cette version étend la version simple en ajoutant la possibilité de jouer plusieurs parties et de garder un historique des parties précédentes.

## Contenu du Projet

Le projet est organisé en plusieurs fichiers :

- `RPS_SimpleGame.py` : Contient la classe `RPS_SimpleGame` pour la version simple du jeu.
- `RPS_MultipleGame.py` : Contient la classe `RPS_MultipleGame` pour la version multiple du jeu.
- `RPS_Game.py` : Fichier de tests unitaires pour les classes `RPS_SimpleGame` et `RPS_MultipleGame`.

## Instructions d'Exécution

Pour jouer au jeu ou exécuter les tests, vous pouvez utiliser les commandes suivantes depuis votre terminal :

```bash
# Jouer à la version simple
python RPS_SimpleGame.py

# Jouer à la version multiple
python RPS_MultipleGame.py

# Exécuter les tests
export PYTHONPATH=$PYTHONPATH:'.'
python RPS_Game.py
```

## Dépendances

Ce projet ne nécessite aucune dépendance externe. Il utilise uniquement les modules standard de Python.

## Auteur

Ce projet a été réalisé par [Tinaël Delzenne Zamparutti](https://github.com/Tinael).
