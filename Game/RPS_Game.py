"""
Espace Test pour le jeu Pierre/Feuille/Ciseaux

Author : Tinaël Delzenne Zamparutti

Liste d'importations : unittest, RPS_SimpleGame from Game.RPS_Tools

Méthodes de test :
------------------
test_SimplegameTwoplayers():
    Teste la méthode SimplegameTwoplayers de la classe RPS_SimpleGame.
    Vérifie les résultats attendus pour différents scénarios de jeu entre deux joueurs.

test_SimplegameOneplayer():
    Teste la méthode SimplegameOneplayer de la classe RPS_SimpleGame.
    Vérifie les résultats attendus pour différents scénarios de jeu entre un joueur et l'ordinateur.

test_RPS_MultipleGame():
    Teste les fonctionnalités de la classe RPS_MultipleGame.
    Vérifie la gestion de l'historique et les résultats du jeu.
"""
import unittest
from RPS_Tools import RPS_SimpleGame, RPS_MultipleGame

class TestRPS(unittest.TestCase):
    """
    Classe de tests pour la classe RPS_SimpleGame
    """

    def test_SimplegameTwoplayers(self):
        """Méthode de test pour la méthode SimplegameTwoplayers de la classe RPS_SimpleGame"""

        game = RPS_SimpleGame.RPS_SimpleGame()

        # Vérification des résultats attendus pour différents scénarios de jeu
        self.assertEqual(game.SimplegameTwoplayers('R', 'S'), 1)  # Joueur 1 gagne avec R contre S
        self.assertEqual(game.SimplegameTwoplayers('test', 'P'), 3)  # Erreur entrée invalide
        self.assertEqual(game.SimplegameTwoplayers('S', 'R'), 2)  # Joueur 2 gagne avec R contre S
        self.assertEqual(game.SimplegameTwoplayers('S', 'S'), 0)  # Égalité avec S contre S

    def test_SimplegameOneplayer(self):
        """Méthode de test pour la méthode SimplegameOneplayer de la classe RPS_SimpleGame"""

        game = RPS_SimpleGame.RPS_SimpleGame()
        # Vérification des résultats attendus pour différents scénarios de jeu
        self.assertIn(game.SimplegameOneplayer('R'), [0, 1, 2])  # Résultat possible de SimplegameOneplayer avec R
        self.assertEqual(game.SimplegameOneplayer('test'),3)  # Erreur entrée invalide

    def test_RPS_MultipleGame(self):
        """Méthode de test pour la classe RPS_MultipleGame"""

        multiple_game = RPS_MultipleGame.RPS_MultipleGame()

        # Test de la méthode play
        self.assertIn(multiple_game.play('R'), [0, 1, 2])  # Résultat possible de la partie avec choix 'R'
        self.assertEqual(multiple_game.play('test'),3)  # Erreur entrée invalide

        # Test de l'historique
        history = multiple_game.get_history()
        self.assertIsInstance(history, list)  # Vérifie que l'historique est une liste

if __name__ == '__main__':
    unittest.main()
