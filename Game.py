#coding:utf-8
from Player import *
from Levels_list import *
from Stats import *
# from DB import *
import time
from threading import Timer
from DB import *
import sys

class Game:
    # Class qui représente une partie de jeu

    #Const
    TIMEOUT = 10
    
    #Constructeur
    def __init__(self ,levels_list):
        self.db = DB()
        self.db.connectDB()
        self.levels_list=levels_list
        self.levels = levels_list.getLevels()
        self.player = None
        self.dotation = None
        self.stats= None
        self.nb_python = 0
        self.mise=0
        self.currentLevel = self.levels[0]
        self.nb_coup= 0
        self.level=1
        self.gameEnded= False
        self.gain=0
        self.maxLevel=0
        self.maxMise=0
        self.miseMin=0
        self.gainMin=0
        self.idPlayer = None
        self.cmpFirst = 0
        self.maxLoss=0

    #Setters
    def setPlayer(self, player):
        self.player=player

    def setLevel(self, level):
        self.level=level

    def setStats(self, stats):
        self.stats=stats
    
    def setNbPython(self, nb_python):
        self.nb_python=nb_python

    def setMise(self, mise):
        self.mise=mise

    def setDotation(self, dotation):
        self.dotation=dotation

    def play(self):
        '''
            Permet de lancer le jeu
        '''
        while True:
            name_user = input("Je suis Python. Quel est votre pseudo ? ")
            if not name_user :
                print("Pseudo non valide")
            else:
                print("Pseudo valide !")
                self.player=self.db.addPlayer(name_user)
                self.dotation=self.player.getSolde()
                break
        #Ask the player if he wants to know the rules of the game
        answer = self.askRules()
        if(answer == True):
            self.showRules()

        #Initialisation
        self.miseMin=self.player.getSolde()
        self.gainMin=self.player.getSolde()
        playQuestion = self.askPlayer()
        while(self.dotation != 0 and playQuestion == True):
            while True:
                # Demander au joueur de miser
                print ("### current level : "+ self.currentLevel.ToString())
                print('Entrer une mise inférieure ou égale à {} € : ?'.format(self.dotation ))
                self.mise = input()
                try:
                    self.mise = int(self.mise)
                except:
                    print('Entrez un nombre.')
                    continue
                if self.mise < 1:
                    print('Entrez a nombre postif.')
                    continue
                if self.mise > self.dotation :
                    print('Erreur, votre mise est plus elevé que votre solde.: '+str(self.dotation ))
                    continue
                
                self.idPlayer = self.db.checkRegistredPlayer(name_user)['id']
                self.idGame = self.db.displayGames(name_user)
                self.miseMin=self.getMin(self.miseMin,self.mise)
                self.maxMise=self.getMax(self.mise,self.maxMise)
                #Mettre à jour les valeurs dans la BD
                self.db.updateStats('miseMin',self.miseMin,self.idPlayer,name_user,self.idGame['id'])
                self.db.updateStats('miseMax',self.maxMise,self.idPlayer,name_user,self.idGame['id'])
                break
            # Generer un nombre random
            self.nb_python = self.currentLevel.getRandomNumber(self.currentLevel.getRange1(),self.currentLevel.getRange2())
            print("#### nb_python "+str(self.nb_python))
            while (self.nb_coup < self.currentLevel.getCount() ) :
                # self.nb_coup+= 1
                # Demander au joueur de saisir un nombre qui correspond au nombre tiré par hasard
                while True :
                    timeout = time.time() + self.TIMEOUT
                    self.nb_user = input ("Entrez SVP votre nombre ? ")
                    try:
                        self.nb_user = int(self.nb_user)
                    except:
                        print('Please use numeric digits.')
                        continue
                    if self.nb_user < 1:
                        print('Entrez a positive number.')
                        continue
                    if time.time() > timeout:
                        # Verifier que le délai de 10 sec n'a pas été franchis
                        temp = self.nb_coup+1
                        triesLeft = (self.currentLevel.getCount() - temp)
                        print("Vous avez dépassé le délai de 10 secondes ! Vous perdez l'essai courant\n\t\t\t et il vous reste {} essai(s) !" .format(triesLeft))
                        # self.nb_coup+= 1
                        if(self.nb_coup < self.currentLevel.getCount()):
                            self.nb_coup+=1
                            
                        else:
                            return 
                        continue
                    self.nb_coup+=1
                    break
                
                    
                
                #Verifier la réponse du joueur
                if self.nb_user > self.nb_python :
                    
                    print ('Votre nbre est trop grand')
                elif self.nb_user < self.nb_python :
                    
                    print ('Votre nbre est trop petit')
                else :
                    
                    print ("Bingo ! Vous avez gagné en {} coup(s) !".format(self.nb_coup))
                    
                    cote=self.currentLevel.getCote()
                    cote=cote[self.nb_coup-1]
                    if(self.nb_coup == 1):
                        self.cmpFirst +=1
                        self.db.updateStats('firstTryNumber', self.cmpFirst, self.idPlayer, name_user,self.idGame['id'])
                    # Calculer le gain, le nouveau solde, mise minimal, etc
                    self.dotation = (self.player.getSolde()-self.mise)+(self.mise*cote)
                    self.gain += (self.mise*cote)-self.mise
                    self.gainMin=self.getMin(self.gainMin,self.gain)
                    self.player.setSolde(self.dotation)
                    self.maxLevel=self.getMax(self.level,self.maxLevel)
                    # Mettre à jour les champs dans la BD
                    self.db.updateStats('gainMin', self.gainMin,self.idPlayer,name_user,self.idGame['id'])
                    self.db.updateStats('gainMax', self.gain, self.idPlayer,name_user,self.idGame['id'])
                    self.db.updateStats('levelMax', self.level, self.idPlayer, name_user,self.idGame['id'])
                    self.db.updateTable('players','solde', self.dotation, self.idPlayer, name_user)
                    
                    # Aller au niveau suivant aprés un succés
                    self.level+=1
                    if(self.level > self.levels_list.getNumberLevels()):
                        # Si le joueur arrive au dernier niveau 
                        self.gameEnded=True
                        self.askPlayer()
                    else :
                        print ("Super ! Vous passez au Level: {}!\n".format(self.level))
                        self.currentLevel = self.levels_list.getLevel(self.level-1)
                        self.nb_coup=0
                        self.askPlayer()
                    break
            
            if (self.nb_user!=self.nb_python) :
                print ("Vous avez perdu, mon nombre choisi est :"+ str(self.nb_python))
                self.dotation-=self.mise
                self.player.setSolde(self.dotation)
                self.maxLoss=self.getMax(self.mise,self.maxLoss)
                # Si le joueur perd il retourne au niveau précédent
                if(self.level == 0):
                    self.currentLevel = self.levels_list.getLevel(0)
                else:
                    self.currentLevel = self.levels_list.getLevel(self.level-1)
                self.nb_coup=0
                self.askPlayer()
            if(self.dotation == 0) :
                print ("Vous avez perdu, vous n'avez plus de solde €:"+ str(self.dotation))
                self.show()
                self.gameEnded = True
                sys.exit()
                break
        playQuestion = self.askPlayer()
        
    def askPlayer(self):
        '''
        Demander au joueur s'il veut rejoueur
        Réponse yes, y, no or n
        No case sensitivity in the answer. yes, YeS, y, Y, nO . . . 
        '''
        while(True):
            if(self.gameEnded ==True):
                answer = input("Vous possedez € " + str(self.player.getSolde()) +" Voulez vous encore jouer ? (Y/N)")
                answer = answer.lower()
                if(answer == "yes" or answer == "y"):
                    self.currentLevel = self.levels_list.getLevel(0)
                    self.level=1
                    self.nb_coup=0
                    return True
                elif(answer == "no" or answer == "n"):
                    print("Vous avez terminé votre partie avec €" + str(self.player.getSolde()) + " de solde.")
                    self.show()
                    sys.exit()
                else:
                    print("wrong input!")

            else :
                answer = input("Bonjour "+ self.player.getUserName() +". Vous possedez €" + str(self.player.getSolde()) + ". Voulez vous jouer(Y/N)? ")
                answer = answer.lower()
                if(answer == "yes" or answer == "y"):
                    return True
                elif(answer == "no" or answer == "n"):
                    print("Vous avez terminé votre partie avec €" + str(self.player.getSolde()) + " de solde.")
                    self.show()
                    sys.exit()
                else:
                    print("wrong input!")

    def askRules(self):
        '''
        Demander au joueur s'il veut voir les régles du jeu
        Réponse yes, y, no or n
        No case sensitivity in the answer. yes, YeS, y, Y, nO . . . 
        '''
        while(True):
            answer = input("Bonjour voulez vous connaitre les régles (Y/N) ? ")
            answer = answer.lower()
            if(answer == "yes" or answer == "y"):
                return True
            elif(answer == "no" or answer == "n"):
                print("Bonne Partie !.")
                return False
            else:
                print("wrong input!")

    def getMax(self,elem1,elem2):
        if(elem1>=elem2):
            return elem1
        else :
            return elem2

    def getMin(self,elem1,elem2):
        if(elem1<=elem2):
            return elem1
        else :
            return elem2

        
    def showRules(self):
        '''
        Afficher les régles du jeu
        '''
        print(""" 
                    *  *  *  *  *  *  *  *  *  *  * Bienvenue *  *  *  *  *  *  *  *  *\n
                    Le jeu comporte 3 levels avec la possibilié que le joueur choissise son level (si ce n'est pas sa 1è fois dans le Casino).
                    En d'autres termes, tout nouveau joueur doit passer par le 1è level. Suite à la 1è partie, il a le droit de choisir son level en lui rappelant / proposant le dernier niveau atteint\n.
                    Lors de chaque niveau, Python tire un nombre : level 1 (entre 1 et 10),
                    level2 (1 et 20), level3 (1 et 30). C'est à vous de deviner le nombre mystérieux avec 3 essais (en tout) lors du 1è 
                    level, 5 au 2è level et 7 au 3è level. Chaque essai ne durera pas plus de 10 secondes. Au-delà, 
                    vous perdez votre essai. Att : si vous perdez un level, vous rejouez le level précédent.
                    Quand vous souhaitez quitter le jeu, un compteur de 10 secondes est mis en place. 
                    En absence de validation de la décision, le jeu est terminé.
                    *  *  *  *  *  *  *  *  *  *  * Régles *  *  *  *  *  *  *  *  *\n
                    vous avez le droit à trois essais !\n
                    \t- Si vous devinez mon nombre dès le premier coup, vous gagnez le double de votre mise !\n
                    \t- Si vous le devinez au 2è coup, vous gagnez exactement votre mise !\n
                    \t- Si vous le devinez au 3è coup, vous gagnez la moitiè votre mise !\n    
                    \t- Si vous ne le devinez pas au 3è coup, vous perdez votre mise et
                    \tvous avez le droit : 
                    \t\t- de retenter votre chance avec l'argent qu'il vous reste pour reconquérir le level perdu.
                    \t\t- de quitter le jeu.\n
                    \t- Dès que vous devinez mon nombre : vous avez le droit de quitter le jeu et de partir avec vos gains OU \n\t\tde continuer le jeu en passant au level supérieur.\n     
                    """)

    def show(self) :
        '''
        Afficher les stats du joueur de la partie terminée
        '''
        print ("""\t************ Vos meilleures stats ************ \n
                \t- Réponse dés le premier coup : {}!\n
                \t- Gain Maximal : {} € !\n
                \t- Mise Maximale : {}€ !\n
                \t- Level Maximale : {} !\n
                ************ Vos Mauvaises stats ************ \n
                \t- Gain minimal : {} € :(\n
                \t- Mise minimale : {} € :(\n
                \t- Grosse Perte : {} € :(\n
                """.format(
                self.cmpFirst ,
                self.gain,
                self.maxMise,
                self.maxLevel,
                self.gainMin,
                self.miseMin,
                self.maxLoss
                ))