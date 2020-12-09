from Levels_list import *
from Game import *

# from DB import *

class CasinoGame :
    # Main class qui permet de lancer le jeu
    levels_list = Levels_list()
    game= Game(levels_list)
    game.play()


