class Player:
  #Classe qui represente un joueur
  # Constants:
  INIT_MISE = 10
  
  #Constructeur
  def __init__(self, name_user):
    self.name_user = name_user
    self.solde = self.INIT_MISE
    self.stats=None

  #Setters
  def setSolde(self,sold):
    self.solde = sold
  
  def setStats(self, stats):
    self.stats=stats

  def getStats(self):
    return self.stats

  #Getters

  def getUserName(self):
    return self.name_user

  def getSolde(self):
    return self.solde

  def showPlayerStats(self) :
    '''
    Afficher les stats d'un joueur
    '''
    return self.stats.show()

