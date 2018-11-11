#!/usr/bin/env python3

# 2a-mol.py
# Jeu du plus ou moins à partir d'un fichier
# 23/10/2018
# Mohamed Lazar

import signal
import random
import re

# Pas d'erreur au ctrlC

def stop_ctrlC(sig, frame):
    fin()
signal.signal(signal.SIGINT, stop_ctrlC)


# Fonction de fin de jeu
def fin():
    print("\b\bBye")
    exit()


# Avec r on autorise le droit de lecture sur le fichier
def read_file():
    file = open("devine.txt", "r")
    msg = file.read()
    file.close()
    return msg

# Avec w on autorise le droit d'écriture sur le fichier
def write_file(msg):
    file = open("devine.txt", "w")
    file.write(msg)
    file.close()

# on créé les variables nécessaires
reg = re.compile('^[0-9]+')
solution = random.randint(0, 100)
end = False

write_file("Veuillez entrez un chiffre entre 0 et 100")
print(solution)

# Condition de trop grand trop petit 
while end is False:
    # On va lire dans le file
    saisi = read_file()
    # On vérifie la saisie utilisateur
    if reg.match(saisi):
        saisi = int(saisi)
        if saisi > solution:
            write_file("Trop grand !")
        elif saisi < solution:
            write_file("Trop petit !")
        # Fin du jeu et fin de la boucle
        else:
            write_file("Bingo !")
            end = True
            fin()
