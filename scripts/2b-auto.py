#!/usr/bin/env python3

# 2b-auto.py
# Jeu du plus ou moins auto
# 23/10/2018
# Mohamed Lazar


import random
import re
import signal


#Solution
def fermeture(signal, frame):
    ecrire('La solution etait '+str(nbAleatoire)+'\nAu revoir !')
    exit()


signal.signal(signal.SIGINT, fermeture)


#Ecrit dans le fichier
def ecrire(msg):
    file = open("saisie-jeu.txt", "w")
    file.write(msg)
    file.close()


#Lit le fichier
def lire():
    file = open("saisie-jeu.txt", "r")
    msg = file.readline().strip()
    file.close()
    return msg


#Boucle du jeu
def plusOuMoins(finBoucle, min, max, nbCoup):
    while(finBoucle is False):
        nbCoup += 1
        nbOrdi = random.randint(min, max)
        ecrire(str(nbOrdi))

        saisie = lire()

        if(pattern.match(saisie)):
            saisie = int(saisie)

            if(saisie > nbAleatoire):
                max = int(saisie)
                ecrire("C'est moins")

            elif(saisie < nbAleatoire):
                min = int(saisie)
                ecrire("C'est plus")
            else:
                ecrire('Vous avez trouvez en '+str(nbCoup)+' coups.\nLa solution etait '+str(nbAleatoire)+'\nAu revoir !')
                finBoucle = True


pattern = re.compile("[0-9]+$")
min = 0
max = 100
nbCoup = 0

finBoucle = False
nbAleatoire = random.randint(0, 100)
nbOrdi = random.randint(0, 100)

ecrire('Bienvenue dans le Jeu du Plus ou Moins !')

plusOuMoins(finBoucle, min, max, nbCoup)
