# SENE Ndeye Fatou Master 2 Data Science

import os
import subprocess
import requests

def generate_project_tree():

    # Création des fichiers README.md, LICENSE et requirements.txt
    with open('README.md', 'w') as readme:
        readme.write('# Mon Projet d\'Analyse de Données\n\nDescription de mon projet.')

    with open('LICENSE', 'w') as license_file:
        license_file.write('License')

    # Téléchargement du modèle de fichier .gitignore pour Python depuis GitHub
    gitignore_url = 'https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore'
    gitignore_content = requests.get(gitignore_url).text

    # Création du fichier .gitignore et écriture du contenu du modèle
    with open('.gitignore', 'w') as gitignore:
        gitignore.write(gitignore_content)

    """
    # Création de l'arborescence du projet
    os.makedirs('data/cleaned')
    os.makedirs('data/processed')
    os.makedirs('data/raw')
    os.makedirs('docs')
    os.makedirs('models')
    os.makedirs('notebooks')
    os.makedirs('reports')
    os.makedirs('src')
    
    with open('Makefile', 'w') as makefile:
        makefile.write('Makefile')

    with open('requirements.txt', 'w') as requirements:
        requirements.write('numpy\npandas\nmatplotlib\nscikit-learn\njupyter\n')
    

    # Création du fichier main_notebook.ipynb
    with open('notebooks/main.ipynb', 'w') as notebook:
        notebook.write('{ "cells": [], "metadata": {}, "nbformat": 4, "nbformat_minor": 2 }')

    
    """
    # Création du fichier train.py
    with open('src/train.py', 'w') as training:
        training.write(' """Contient entrainement du modele."""\n\n')
        training.write('def training():\n')
        training.write('    pass\n')

    # Initialisation du dépôt Git
    subprocess.run(['git', 'init'])

    # Ajout de tous les fichiers de l'arborescence au dépôt Git
    subprocess.run(['git', 'add', '.'])

    # Commit des fichiers ajoutés
    subprocess.run(['git', 'commit', '-m', 'Add the training script to src'])

    # Push des fichiers créer
    subprocess.run(['git', 'push', 'origin', 'branche-1'])
    print('Arborescence du projet créée et dépôt Git initialisé.')

if __name__ == '__main__':
    generate_project_tree()