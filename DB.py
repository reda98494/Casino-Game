from configparser import ConfigParser
from Player import *
from datetime import datetime as date
import pymysql.cursors
from pymysql.cursors import Cursor
from Stats import *

# Class qui permet de gérer les accés à la DB et de récuperer les données 

class DB:

    today = date.today()
    #Constructeur
    def __init__(self):
        self.player = None
        self.connection = None
        self.stats= Stats()
        self.game=None

    
    def connectDB(self):
        '''
            Se connecter à la BD
        '''
        self.connection = pymysql.connect(host="127.0.0.1",
        user="****",
        passwd="****",
        database="casino",
        charset='utf8mb4',
        
        cursorclass=pymysql.cursors.DictCursor)
        return self.connection

    def addPlayer(self,username):
        '''
            Permet d'ajouter un joueur à la BD et de créer des lignes dans les tables Game et Stats qui corresponds au joueur
        '''

        checkPlayer = self.checkRegistredPlayer(username) # Tester si le joueur exsiste dans la BD
        if(checkPlayer== None):
            '''
                initialiser les lignes dans les Tables Player, Game, Stats pour le nouveau Joueur
            '''
            try:
                with self.connection.cursor() as cursor:
                    sql = "INSERT INTO players ( name,created_at,solde ) VALUES ( %s,%s,%s )"
                    cursor.execute(sql,(username,self.today,Player.INIT_MISE))
                    self.connection.commit()
                    
                    checkPlayer = self.checkRegistredPlayer(username) 
                    sql = "INSERT INTO game (idPlayer) VALUES (%s)"
                    cursor.execute(sql,(checkPlayer['id']))
                    self.connection.commit()

                    game = self.displayGames(username)
                    checkPlayer = self.checkRegistredPlayer(username)
                    sql = "INSERT INTO stats (levelMax, miseMax, idPlayer, idGame ) VALUES (%s, %s, %s, %s)" 
                    cursor.execute(sql,(1, 0, checkPlayer['id'], game['id']))
                    self.connection.commit()

                    
                # with self.connection.cursor() as cursorStats : 
            except ValueError:
                print(ValueError)
                print("ERROR dans addPlayer")         
            finally:
                self.connection.cursor().close()  
                # self.closeConnection() 
            self.player = Player(username)
            #self.player.setStats(self.stats)
                
        else :
            '''
                Recupérer les lignes dans les Tables Player, Game, Stats pour le Joueur déja existant
            '''
            self.player =Player(username)
            self.player.setSolde(checkPlayer['solde'])
            stats = self.displayStats(checkPlayer['id'])
            print ("""Comme on se retrouve voici vos stats depuis le {} :  !\n
                                \t- Gain Maximal : {} € !\n
                                \t- Gain Minimal : {} € :(\n
                                \t- Mise Maximale : {} € !\n
                                \t- Mise Minimale : {} € :(\n
                                \t- Level Maximale : {} !\n
                                \t- Bonne pioche en un coup  : {}!\n  
                        """.format(checkPlayer['created_at'],stats['gainMax'],stats['gainMin'],stats['miseMax'],stats['miseMin'],stats['levelMax'], stats['firstTryNumber']))
            self.addNewGame(checkPlayer['id'],username)
            self.game = self.displayGames(username)
            self.addStats(username,self.game['id'])

        return self.player
    #TODO
    def checkRegistredPlayer(self,username):
        '''
            Permet de vérifier si le joueur existe dans la BD
        '''
        try:
            with self.connection.cursor() as cursor:
                
                cursor.execute("SELECT * FROM players WHERE name= %s ", (str(username,)))
                fetchAnswer= cursor.fetchone()
                return fetchAnswer
                
        except ValueError:
            # self.closeConnection()
            print(ValueError)

    def displayStats(self,idPlayer):
        '''
            Permet de récuperer les stats du joueur de la table Stats
        '''
        tabStats = {}
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT * FROM stats WHERE idPlayer = %s ",(int(idPlayer,)))
                player = cursor.fetchall()
                for row in player:
                    tabStats.update(row)
                return tabStats
        except ValueError:
            print(ValueError)
        finally:
            self.connection.cursor().close()

    def updateTable(self,table,champs, val, idPlayer, username):
        '''
            Permet de mettre un joueur les champs tables
        '''
        checkPlayer = self.checkRegistredPlayer(username)
        if(checkPlayer != None):
            try:
                with self.connection.cursor() as cursor :
                    
                    # print(cursor.execute(sql, Vall))
                    cursor.execute(("UPDATE "+table+" SET " +champs+ "=" +str(val)+ "  WHERE id = %s"),(idPlayer,))
                    self.connection.commit()
                    print(cursor.rowcount, "record(s) affected")
            except ValueError:
                print(ValueError)
                print("ERROR dans updateStats")
            finally:
                self.connection.cursor().close()
                # self.closeConnection()
        else:
            print("Player introuvable")

    def updateStats(self,champs, val, idPlayer, username, idGame):
        '''
            Permet de mettre les stats d'un joueur
        '''
        checkPlayer = self.checkRegistredPlayer(username)
        if(checkPlayer != None):
            try:
                with self.connection.cursor() as cursor :
                    cursor.execute(("UPDATE stats SET " +champs+ "=" +str(val)+ "  WHERE idPlayer = %s AND idGame= %s "),(idPlayer,idGame,))
                    self.connection.commit()
            except ValueError:
                print(ValueError)
                print("ERROR dans updateStats")
            finally:
                self.connection.cursor().close()
        else:
            print("Player introuvable")
    
    def addNewGame(self,idPlayer,username):
        '''
            Initialiser une nouvelle ligne pour une nouvelle partie du jeu
        '''
        checkPlayer = self.checkRegistredPlayer(username) #Verifier si le joueur existe
        if(checkPlayer != None):
            try:
                with self.connection.cursor() as cursor :
                    # print(cursor.execute(sql, Vall))
                    sql = "INSERT INTO game (idPlayer) VALUES (%s)"
                    cursor.execute(sql,(checkPlayer['id']))
                    self.connection.commit()
                    # print(cursor.rowcount, "record(s) affected")
            except ValueError:
                print(ValueError)
                print("ERROR dans updateStats")
            finally:
                self.connection.cursor().close()
                # self.closeConnection()
        else:
            print("Player introuvable")

    def displayGames(self,username):
        '''
            Recupérer toutes les parties d'un joueur
        '''
        checkPlayer = self.checkRegistredPlayer(username)
        try:
            with self.connection.cursor() as cursor :
                    # print(cursor.execute(sql, Vall))
                    sql = "SELECT * FROM game WHERE (idPlayer)= %s"
                    cursor.execute(sql,(checkPlayer['id']))
                    games = cursor.fetchall()
                    tabStats={}
                    for row in games:
                        tabStats.update(row)
                    return tabStats
        except ValueError:
                print(ValueError)
                print("ERROR dans displayGames")
        finally:
                self.connection.cursor().close()

    def addStats(self, username,idGame):
        '''
            Ajouter une nouvelle ligne de stats d'un joueur
        '''
        checkPlayer = self.checkRegistredPlayer(username)
        if(checkPlayer != None):
            try:
                with self.connection.cursor() as cursor:
                    sql = "INSERT INTO stats (levelMax, miseMax, idPlayer, idGame) VALUES (%s, %s, %s, %s)" 
                    cursor.execute(sql,(1, 0, checkPlayer['id'], idGame))
                    self.connection.commit()
            except ValueError:
                print(ValueError)
            finally:
                self.connection.cursor().close

    def closeConnection(self):
        self.connection.close()



db = DB()
db.connectDB()

