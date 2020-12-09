#coding:utf-8
from Player import *

class Stats:
    #Classe qui permet d'afficher les stats d'un joueur
    
    #Const
    TIMEOUT = 10

    #Constructeur
    def __init__(self):
        self.maxLevel=1
        self.maxMise=0
        self.gainMin=0
        self.gainMax=0
        self.maxLoss=0
        # self.idPlayer = None
        self.firstTriesCount = 0

    #Setters
    def setMaxlevel(self,level):
        self.maxLevel=level

    def setMaxMise(self,maxMise):
        self.maxMise=maxMise

    def setMiseMin(self,miseMin):
        self.miseMin=miseMin

    def setGainMax(self,gainMax):
        self.gainMax=gainMax

    def setMaxLoss(self,maxLoss):
        self.maxLoss=maxLoss

    def setFirstTriesCount(self,firstTriesCount):
        self.firstTriesCount=firstTriesCount

    #Getters
    def getMaxlevel(self):
        return self.maxLevel

    def getmaxMise(self):
        return self.maxMise

    def getMiseMin(self):
        return self.miseMin

    def getGainMax(self):
        return self.gainMax

    def getMaxLoss(self):
        return self.maxLoss
    
    def getFirstTriesCount(self):
        return self.firstTriesCount

    def updateAllStats(self,maxLevel,maxMise,gainMax,firstTriesCount,gainMin,maxLoss):
        '''
        Mettre à jour toutes les stats du joueur
        '''
        self.maxLevel=maxLevel
        self.maxMise=maxMise
        self.gainMin=gainMin
        self.gainMax=gainMax
        self.maxLoss=maxLoss
        self.firstTriesCount = firstTriesCount

    def show(self) :
        '''
        Afficher les stats du joueur
        '''
        print ("""************ Vos meilleures stats ************ \n
                \t- Réponse dés le premier coup : {}!\n
                \t- Gain Maximal : {}!\n
                \t- Mise Maximale : {}!\n
                \t- Level Maximale : {}!\n
                ************ Vos Mauvaises stats ************ \n+
                \t- Gain minimal : {}!\n
                \t- Mise minimale : {}!\n
                \t- Grosse Perte : {}!\n
                """.format(
                self.firstTriesCount ,
                self.gainMax,
                self.maxMise,
                self.maxLevel,
                self.gainMin,
                self.miseMin,
                self.maxLoss
                ))