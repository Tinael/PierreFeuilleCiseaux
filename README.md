# Jeu Pierre/Feuille/Ciseaux

Ce projet implémente le célèbre jeu Pierre/Feuille/Ciseaux en Python. Il propose deux versions du jeu : une version simple où un joueur peut jouer contre un autre joueur ou contre l'ordinateur, et une version multiple qui permet de jouer plusieurs parties en conservant un historique des parties précédentes.

## Contenu du Projet
Voici l'arborescence simplifiée du projet :
    
    Pierre-Feuille-Ciseaux/
    ├── Game
    │   ├── RPS_Tools
    │   │   ├── __init__.py
    │   │   ├── RPS_SimpleGame.py
    │   │   └── RPS_SimpleGame.py
    │   └── RPS_Game.py
    ├── RPS_MultipleGame.log
    ├── RPS_SimpleGame.log
    └── README.md

Le projet est organisé en plusieurs fichiers :

- `RPS_SimpleGame.py` : Contient la classe `RPS_SimpleGame` pour la version simple du jeu.
- `RPS_MultipleGame.py` : Contient la classe `RPS_MultipleGame` pour la version multiple du jeu.
- `RPS_Tools` : Contient des outils et fonctions utilisés par les classes principales.
- `RPS_Game.py` : Fichier de tests unitaires pour les classes `RPS_SimpleGame` et `RPS_MultipleGame`.

## Version Simple

La classe `RPS_SimpleGame` permet de jouer au jeu Pierre/Feuille/Ciseaux dans sa version simple. Elle propose deux méthodes principales :

- `SimplegameTwoplayers(self, player1choice, player2choice)`: Cette méthode permet à deux joueurs humains de jouer entre eux.
- `SimplegameOneplayer(self, player1choice)`: Cette méthode permet à un joueur humain de jouer contre l'ordinateur.

## Version Multiple

La classe `RPS_MultipleGame` étend les fonctionnalités de la version simple en ajoutant la possibilité de jouer plusieurs parties en conservant un historique. Les principales méthodes de cette classe sont :

- `play(self, player_choice)`: Cette méthode permet à un joueur humain de jouer contre l'ordinateur et enregistre le résultat dans l'historique.
- `get_history(self)`: Cette méthode renvoie l'historique des parties jouées.
- `clear_history(self)`: Cette méthode efface l'historique des parties.

## Tests Unitaires

Le fichier `RPS_Game.py` contient des tests unitaires pour les classes `RPS_SimpleGame` et `RPS_MultipleGame`. Ces tests vérifient le bon fonctionnement des méthodes et la gestion des erreurs.

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

## Auteur

Ce projet a été réalisé par [Tinaël Delzenne Zamparutti](https://github.com/Tinael).
