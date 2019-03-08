# MacGyver-Game


First Project with OpenClassRoom Python Developper Cursus

Création d'un jeu de logique (labyrinthe) en Python 3, dont le but est d'emmener le héros (MacGyver) à quitter le labyrinthe avec succès. Afin de terrasser le terrible gardien de la porte, le héros devra rassembler trois objets disséminés aléatoirement dans le labyrinthe : une aiguille, un tuyau en PVC et une bouteille d'éther. 

<h2>Pré - Requis </h2>

Python 3 et la librairie Pygame sont indispensable au bon fonctionnement du programme. 

Vous pouvez installer <code>python3</code> à l'adresse suivante : https://www.python.org/downloads/

Pour le module Pygame, vous devez déjà avoir <code>pip</code> installé sur votre machine. 
Lancez l'installation de pygame avec cette commande dans votre terminal : 

<code>python3 -m pip install -U pygame --user</code>

<h2> Lancement du jeu </h2>

Après avoir installé python 3 et pygame, vous devez lancer le jeu depuis votre terminal avec la commande suivante : 

<code>python3 main.py</code>

<h2> Gameplay</h2>

Le personnage se déplace à l'aide des flèches directionnelles du clavier et uniquement des fléches (pour l'instant, aucune autre combinaison de touche ou l'utilisation de la souris ne sont implémantés). 

Votre héros devra se frayer un chemin sur un chemin, entouré de hauts murs infranchissables. A vous donc de le faire se mouvoir, sans pouvoir franchir les murs, trop hauts pour lui. 

Afin d'endormir le gardien, votre héros devra absolument rassembler trois objets indispensables : une aiguille, un tuyau en PVC et une bouteille d'éther. Gare à vous si vous vous retrouvez devant votre ennemi sans ses trois objets : vous péririez dans d'atroces souffrances ! 

Un compteur est situé en haut à droite de l'écran pour vous aider à voir combien d'objets vous avez déjà ramassé. 

<h2> Touches utiles </h2>

+ Flèches directionnelles : déplacement du personnage
+ 'Q' : quitter le jeu
+ 'ALT' + 'F4' : fermeture de la fenêtre
