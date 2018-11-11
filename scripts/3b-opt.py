#!/usr/bin/env python3

# 3b-opt.py
# Sauvegarde avec options
# 10/11/2018
# Mohamed Lazar

import signal
import shutil
import gzip
import os
import sys
import subprocess
import argparse


#Ferme le programme
def fermeture(signal, frame):
    exit()

signal.signal(signal.SIGINT, fermeture)


#Choisit le chemin
def cheminSave():
    arguments = argparse.ArgumentParser()
    arguments.add_argument("-p", "--path", help="chemin où vous voulez sauvegarder")
    args = arguments.parse_args()
    if args.path:
        return args.path
    else:
        return '../scripts'


#Archive le dossier
def sauvegarde():
    os.remove(dossierSave + '/archive.tar.gz')
    shutil.move(archive + '.tar.gz', dossierSave)


#Supprime l'archive
def deleteSave():
    if os.path.exists(archive + '.tar.gz'):
        os.remove(archive + '.tar.gz')

dossierSave = os.path.expanduser(cheminSave()+'/Save/')
dossierScripts = os.path.expanduser('../scripts')
archive = os.path.expanduser('./archive')

#Crée le dossier parent de l'archive
os.makedirs(dossierSave, exist_ok=True)
sys.stdout.write('Le dossier \'Save\' vient d\'être créé.\n')

shutil.make_archive(archive, 'gztar', dossierScripts)

#Vérifie s'il y existe une Sauvegarde
if os.path.exists(dossierSave + '/archive.tar.gz'):

    with gzip.open(dossierSave + '/archive.tar.gz', 'rb') as f:
        exist_save = f.read()

    with gzip.open(archive + '.tar.gz', 'rb') as f:
        new_save = f.read()

    if exist_save != new_save:
        sauvegarde()
        sys.stdout.write('La sauvegarde a été archivé dans le dossier \'Save\'.\n')

    else:
        deleteSave()
        sys.stdout.write('Une erreur s\'est produite lors de la sauvegarde.\n')

else:
    shutil.move(archive + '.tar.gz', dossierSave)
    sys.stdout.write('La sauvegarde a été archivé dans le dossier \'Save\'.\n')

