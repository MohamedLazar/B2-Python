#!/usr/bin/env python3

# 2a-mol.py
# Jeu du plus ou moins à partir d'un fichier
# 23/10/2018
# Mohamed Lazar


import signal
import random
import re

#Initialisation des variables et de la regex
reg = re.compile('^[0-9]+')
solution = random.randint(0, 100)
end = False
print(solution)

#On met le r pour read dans le fichier
def read_file():
  file = open("jeu_plus_ou_moins.txt", "r")
  msg = file.read()
  file.close()
  return msg

#On met le w pour write dans le fichier
def write_file(msg):
  file = open("jeu_plus_ou_moins.txt", "w")
  file.write(msg)
  file.close()

write_file("Veuillez saisir un chiffre entre 0 et 100 : ")

#On créer la saisie dans le fichier avec la regex et on verifie si c'est plus grand ou plus petit
while end is False :
    #On lis dans le fichier la saisie de l'utilisateur
    saisi = read_file()
    if re.match("^[0-9]+$", saisi):
        saisi = int(saisi)
        if saisi > 100:
            continue          
        if saisi > solution :
            write_file('Le nombre est trop grand !')       
        elif saisi < solution :
            write_file('Le nombre est trop petit !')
        #On affiche un message de réussite 
        else :
            write_file('Gagné !')
            end = True
            fin()

#La fonction de la fin
def fin():
    print("Merci d'avoir jouer")
    exit()
