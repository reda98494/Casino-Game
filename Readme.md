# Casino Game :

[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)](#table-of-contents)

## Table of Contents
* [Présentation](#intro)
* [Structure : Les classes](#structure)
* [Démarrage du Jeu](#demarrage)
* [Requirements du Project](#requirements)
* [Améliorations](#amelioration)
* [Groupe](#groupe) 

[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)](#intro)

## Présentation
* Le jeu a été developpé en Python. Il comporte 3 levels avec la possibilié que le joueur choissise son level (si ce n'est pas sa 1è fois dans le Casino).
* En d'autres termes, tout nouveau joueur doit passer par le 1è level. Suite à la 1è partie, il a le droit de choisir son level en lui rappelant / proposant le dernier niveau atteint\n.
* Les régles Lors de chaque niveau, Python tire un nombre : level 1 (entre 1 et 10) , level2 (1 et 20), level3 (1 et 30).C'est à vous de deviner le nombre mystérieux avec 3 essais(en tout) lors du 1è level, 3 au 2è level et 7 au 3è level.Chaque essai ne durera pas plus de 10 secondes. vous perdez votre essai.Att: si vous perdez un level, vous rejouez le level précédent.A player may not undo the most recent completed turn.

[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)](#structure)

## Structure : Les classes 
* Game : Class qui représente une partie de jeu
* Level : Classe qui représente un niveau de jeu
* Player: Classe qui represente un joueur
* Stats: Classe qui permet d'afficher les stats d'un joueur
* Levels_list : Classe qui représente une liste des niveaux de jeu
* CasinoGame : Main class qui permet de lancer le jeu
* DB: Class qui permet de gérer les accés à la DB et de récuperer les données 

[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)](#demarrage)

## Démarrage du Jeu
Si vous avez Python installé, lancez:
```bash
python CasinoGame.py
```

[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)](#requirements)

## Requirements du Project
Les requirements du project sont :
* backcall==0.2.0
* click==7.1.2
* colorama==0.4.4
* decorator==4.4.2
* Flask==1.1.2
* ipykernel==5.3.4
* ipython==7.19.0
* ipython-genutils==0.2.0
* itsdangerous==1.1.0
* jedi==0.17.2
* Jinja2==2.11.2
* jupyter-client==6.1.7
* jupyter-core==4.6.3
* MarkupSafe==1.1.1
* parso==0.7.1
* pickleshare==0.7.5
* prompt-toolkit==3.0.8
* Pygments==2.7.2
* PyMySQL==0.10.1
* python-dateutil==2.8.1
* pywin32==300
* PyYAML==5.3.1
* pyzmq==20.0.0
* six==1.15.0
* tornado==6.1
* traitlets==5.0.5
* wcwidth==0.2.5
* Werkzeug==1.0.1

[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)](#dependencies)

## Améliorations
* Refractorer le code
* Créer une application Web en utilisant Flask

[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)](#dependencies)

## Le team :
* Abderrafii RABAH
* Reda BENYOUB
* Louison DONNE
* Antinia AMELLAL
* Thinhinane TEZKRATT
* Mohand Said MAHDI

Nous reste plus qu'à vous souhaiter une bonne partie.



