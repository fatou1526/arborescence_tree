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

    



    # Initialisation du dépôt Git
    subprocess.run(['git', 'init'])

    # Ajout de tous les fichiers de l'arborescence au dépôt Git
    subprocess.run(['git', 'add', '.'])

    # Commit des fichiers ajoutés
    subprocess.run(['git', 'commit', '-m', 'Initial commit'])

    # Push des fichiers créer
    subprocess.run(['git', 'push', 'origin', 'branche-1'])
    print('Arborescence du projet créée et dépôt Git initialisé.')

if __name__ == '__main__':
    generate_project_tree()