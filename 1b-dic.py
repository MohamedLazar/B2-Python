#!/usr/bin/env python3

# 1b-dic.py
# Saisie de prénom
# 15/10/2018
# Mohamed Lazar

#Initialisation de la liste et de la touche pour stopper
name=""
liste = []

#Tant qu'on appuie pas sur q, la boucle continue
while liste != "":
    print("------ Appuyer sur q pour terminer la saisie ------")
    name=input("Taper un mot : ")
    liste.append(name)
    if name == "q":
        break

#Trie par ordre alphabetique + valeur de stop enlevé
liste=liste[:-1]
liste=sorted(liste)
print(liste)

print(" Fin ") 
input("Appuyer sur ENTER pour terminer le programme. ")


