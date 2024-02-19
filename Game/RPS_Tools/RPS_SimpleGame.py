"""
Documentation pour la classe RPS_SimpleGame

Author: Tinaël Delzenne Zamparutti

Description:
------------
Ce fichier contient une classe permettant de jouer au jeu Pierre/Feuille/Ciseaux.

Liste d'importations:
---------------------
import random

Classe:
-------
RPS_SimpleGame:
    Classe pour jouer à Pierre/Feuille/Ciseaux

Méthodes:
---------
SimplegameTwoplayers(self, player1choice, player2choice):
    Méthode pour jouer à Pierre/Feuille/Ciseaux entre deux joueurs.
    
    Arguments:
    ----------
    player1choice (str): Choix du joueur 1 ('R', 'P' ou 'S')
    player2choice (str): Choix du joueur 2 ('R', 'P' ou 'S')

    Retour:
    -------
    int: 0 en cas d'égalité, 1 si le joueur 1 gagne, 2 si le joueur 2 gagne

SimplegameOneplayer(self, player1choice):
    Méthode pour jouer à Pierre/Feuille/Ciseaux contre l'ordinateur.
    
    Arguments:
    ----------
    player1choice (str): Choix du joueur ('R', 'P' ou 'S')

    Retour:
    -------
    int: 0 en cas d'égalité (même choix aléatoire fait par l'ordinateur),
         1 si le joueur gagne, 2 si l'ordinateur gagne

"""

import logging
import random

# Configuration du logging
logging.basicConfig(level=logging.INFO)

class RPS_SimpleGame:
    """
    Classe pour jouer à Pierre/Feuille/Ciseaux
    """
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def SimplegameTwoplayers(self, player1choice, player2choice):
        """
        Méthode pour jouer à Pierre/Feuille/Ciseaux entre deux joueurs

        Args:
            player1choice (str): Choix du joueur 1 ('R', 'P' ou 'S')
            player2choice (str): Choix du joueur 2 ('R', 'P' ou 'S')

        Returns:
            int: 0 en cas d'égalité, 1 si le joueur 1 gagne, 2 si le joueur 2 gagne
        """
        self.logger.info("Début de la partie entre deux joueurs.")

        # Vérification des entrées
        if player1choice not in ['R', 'P', 'S'] or player2choice not in ['R', 'P', 'S']:
            self.logger.error("Erreur : Choix invalide des joueurs.")
            return 3

        self.logger.info("Joueur 1 a choisi : %s", player1choice)
        self.logger.info("Joueur 2 a choisi : %s", player2choice)

        if player1choice == player2choice:
            self.logger.info("Partie terminée : Égalité.")
            return 0
        elif (player1choice == 'R' and player2choice == 'S') or \
             (player1choice == 'S' and player2choice == 'P') or \
             (player1choice == 'P' and player2choice == 'R'):
            self.logger.info("Partie terminée : Joueur 1 a gagné.")
            return 1
        else:
            self.logger.info("Partie terminée : Joueur 2 a gagné.")
            return 2

    def SimplegameOneplayer(self, player1choice):
        """
        Méthode pour jouer à Pierre/Feuille/Ciseaux contre l'ordinateur

        Args:
            player1choice (str): Choix du joueur ('R', 'P' ou 'S')

        Returns:
            int: 0 en cas d'égalité (même choix aléatoire fait par l'ordinateur),
                 1 si le joueur gagne, 2 si l'ordinateur gagne
        """
        self.logger.info("Début de la partie contre l'ordinateur.")

        # Vérification de l'entrée
        if player1choice not in ['R', 'P', 'S']:
            self.logger.error("Erreur : Choix invalide du joueur.")
            return 3

        self.logger.info("Joueur a choisi : %s", player1choice)

        choices = ['R', 'P', 'S']
        computer_choice = random.choice(choices)
        self.logger.info("L'ordinateur a choisi : %s", computer_choice)

        if player1choice == computer_choice:
            self.logger.info("Partie terminée : Égalité.")
            return 0
        elif (player1choice == 'R' and computer_choice == 'S') or \
             (player1choice == 'S' and computer_choice == 'P') or \
             (player1choice == 'P' and computer_choice == 'R'):
            self.logger.info("Partie terminée : Joueur a gagné.")
            return 1
        else:
            self.logger.info("Partie terminée : L'ordinateur a gagné.")
            return 2
