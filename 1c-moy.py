#!/usr/bin/env python3

# 1c-moy.py
# Saisie de prénom associé a une note et calcul de moyenne avec tableau recapitulatif
# 23/10/2018
# Mohamed Lazar


#Initialisation des variables
table = []
i = 0
moy = 0

#Début de la boucle
while 1 :
	def reverse_numeric(x, y):
        	return y - x
	#Saisie du prénom et de la note
	prenom = input("Saisissez un prénom : ")
	note = int(input("Saisissez une note : "))
	namenote = "[{}, {}.]".format(prenom, note)
	try:
		num = int(note)
		print(namenote)
	except ValueError:
		print("Erreur : La note saisie doit être un nombre.")
		break
	#On ajoute la note dans la table
	table.insert(i, namenote)
	moy += int(note)
	i += 1
	#On demande si on quitte ou si on continu
	print("Continuer ou quitter la saisie ?[c/q]")
	keypress = input()
    	#On fais la moyenne et on arrete du programme
	if keypress == "q":
		print("Saisie quittée.")
		print(table)
		moy = moy/i
		print("La moyenne est de {}/20.".format(moy))
		break
