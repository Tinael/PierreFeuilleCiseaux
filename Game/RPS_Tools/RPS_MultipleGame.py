"""
Documentation pour la classe RPS_MultipleGame

Author: Tinaël Delzenne Zamparutti

Description:
------------
Ce fichier contient une classe permettant de jouer au jeu Pierre/Feuille/Ciseaux.

Liste d'importations:
---------------------
import random

"""
import random
import logging
from RPS_Tools import RPS_SimpleGame

logging.basicConfig(filename='RPS_MultipleGame.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RPS_MultipleGame:
    """
    Classe pour jouer à Pierre/Feuille/Ciseaux avec historique des parties
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.history = []

    def play(self, player_choice):
        """
        Méthode pour jouer à Pierre/Feuille/Ciseaux contre l'ordinateur

        Args:
            player_choice (str): Choix du joueur ('R', 'P' ou 'S')

        Returns:
            int: 0 en cas d'égalité (même choix aléatoire fait par l'ordinateur),
                 1 si le joueur gagne, 2 si l'ordinateur gagne
        """
        self.logger.info("Début de la partie.")
        self.logger.info("Joueur a choisi : %s", player_choice)

        computer_choice = RPS_MultipleGame.rand(self)

        self.logger.info("L'ordinateur a choisi : %s", computer_choice)

        game = RPS_SimpleGame.RPS_SimpleGame()

        game_result = game.SimplegameTwoplayers(player_choice,computer_choice)

        # Enregistrer la partie dans l'historique
        self.history.append((player_choice,computer_choice, game_result))

        return game_result

    def get_history(self):
        """Méthode pour obtenir l'historique des parties"""
        return self.history

    def clear_history(self):
        """Méthode pour effacer l'historique des parties"""
        self.history = []

    def last_choice(self):
        """
        Méthode pour obtenir les derniers choix et résultat de jeu

        Returns:
            tuple: (dernier choix du joueur, dernier choix de l'ordinateur, résultat du dernier jeu)
        """

        if self.history:
            return self.history[-1]
        else:
            return None

    def rand(self):
        """méthode pour exécuter une stratégies aléatoires de l'ordinateur"""


        choices = ['R', 'P', 'S']
        computer_choice = random.choice(choices)
        return computer_choice

    def stratégies1(self):
        """stratégies qui prend si la partie d'avant est un défaite le contraire du choix du joueur """

        data = RPS_MultipleGame.last_choice(self)

        last_player= data[0]
        last_result= data[2]

        if last_result == 1:
            if last_player == 'S':
                return 'R'
            elif last_player == 'P':
                return 'S'
            elif last_player == 'R':
                return 'P'
