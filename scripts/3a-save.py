#!/usr/bin/env python3

# 3a-save.py
# Sauvegarde
# 10/11/2018
# Mohamed Lazar

import signal
import shutil
import gzip
import os
import sys
import subprocess


#Ferme le programme
def fermeture(signal, frame):
    exit()

signal.signal(signal.SIGINT, fermeture)


#Archive le dossier
def Save():
    os.remove(dossierSave + '/archive.tar.gz')
    shutil.move(archive + '.tar.gz', dossierSave)


#Supprime l'archive
def deleteSave():
    if os.path.exists(archive + '.tar.gz'):
        os.remove(archive + '.tar.gz')

dossierSave = os.path.expanduser('./Save/')
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
        Save()
        sys.stdout.write('La sauvegarde a été archivé dans le dossier \'Save\'.\n')

    else:
        deleteSave()
        sys.stdout.write('Une erreur s\'est produite lors de la sauvegarde.\n')

else:
    shutil.move(archive + '.tar.gz', dossierSave)
    sys.stdout.write('La sauvegarde a été archivé dans le dossier \'Save\'.\n')
