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

"""
import unittest
from RPS_Tools import RPS_SimpleGame

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

if __name__ == '__main__':
    unittest.main()