#!/usr/bin/env python3

# 1d-mol.py
# Jeu du plus ou moins
# 23/10/2018
# Mohamed Lazar


import signal
import random
import re

#Initialisation des variables et de la regex
reg = re.compile('^[0-9]+')
solution = random.randint(0, 100)
rep = -1

#Fonction des saisie de nombre et du calcul de ce dernier si c'est trop grand ou trop petit
while rep != str(solution):
    print('Veuillez saisir un nombre')
    rep = input()
    if rep == 'q':
        au_revoir()
    elif reg.match(rep):
        if int(rep) > solution:
             print('Le nombre est trop grand')
        elif int(rep) < solution:
            print("Le nombre est trop petit")
    else:
        print("Veuillez entrer un chiffre svp")

#On créér la fonction lorsque la personne trouve la solution
def au_revoir():
    print("\b\bBravo la bonne réponse était",solution)
    exit()

#On empeche le CTRL+C
def fin(sig, frame):
   au_revoir()
signal.signal(signal.SIGINT, fin)

au_revoir()
