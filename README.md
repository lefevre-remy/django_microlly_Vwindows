# django_microlly_Vwindows
Version windows du projet microlly

# Prérequis

il est nécessaire d'avoir installer :
- python 3
- virtualenv (via la commande : pip install virtualenv)
- pillow (via la commande : pip install Pillow)


# Mise en place de l'environnement sur windows

executer les commandes suivantes dans le dossier où vous souhaiter avoir votre site :

- virtualenv microlly_env
- cd microlly_env/Scripts
- activate.bat

# Récuperation et lancement du projet microlly

une fois votre envirronnement lancé vous allez pouvoir récupérer le projet.

- cd ..
- mkdir microlly
- git clone https://github.com/lefevre-remy/django_microlly_Vwindows.git microlly
- cd microlly
- pip install -r requirements.txt
- python manage.py runserver

