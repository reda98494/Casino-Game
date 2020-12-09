import random

class Level :
    # Classe qui représente un niveau de jeu

    #Constructeur
    def __init__(self, count, range1,range2):
        self.count = count
        self.range1=range1
        self.range2=range2
        self.cote = None

    #Setters
    def setCount(self,count):
        self.count=count

    def setRange1(self,range1):
        self.range1=range1

    def setRange2(self,range2):
        self.range2=range2

    def setCote(self,cote):
        self.cote = cote

    #Getters   
    def getRange1(self):
        return self.range1

    def getRange2(self):
        return self.range2

    def getCount(self):
        return self.count

    def getCote(self):
        return self.cote

    def getRandomNumber(self,range1,range2):
        '''
        returns a random item
        '''
        return random.randint(range1, range2+1)

    def ToString(self):
        return str([self.count,self.range1,self.range2])

    

    

    