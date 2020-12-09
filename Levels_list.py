from Level import *
class Levels_list :
     # Classe qui représente une liste des niveaux de jeu
    levels=[]
    nbLevel = 0

    #Constructeur
    def __init__(self):
        level1= Level(3,1,11)
        level1.setCote([2,1,0.5])
        self.levels.append(level1)
        self.nbLevel+=1
        level2= Level(5,1,20)
        level2.setCote([2,1,0.75,0.5,0.25])
        self.levels.append(level2)
        self.nbLevel+=1
        level3= Level(7,1,30)
        level3.setCote([2.5,2,1.5,1,0.75,0.5,0.25])
        self.levels.append(level3)
        self.nbLevel+=1

    def getLevels(self):
        # Recuperer tous les niveaux
        return self.levels

    def getNumberLevels(self):
        # Recuperer le nombres des niveaux
        return self.nbLevel

    def getLevel(self,index):
        # Recuperer un niveau selon l'index
        return self.levels[index]
