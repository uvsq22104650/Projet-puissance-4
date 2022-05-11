############################
# importation des librairie
############################

import tkinter as tk
import os,random
import turtle
from turtle import *

############################
# Constantes
############################

nb_lignes = 6
nb_colonnes = 7

################################
# Creation de la grille
################################
#Source du code http://fractale.gecif.net/python/puissance_4/
"""un 0 indique une case vide, un 1 un pion ROUGE et un 2 un BLEU"""
grille=[7*[0], 7*[0], 7*[0], 7*[0], 7*[0], 7*[0]]
"""nbr_colonnes mémorise le nombre de pions dans la colonne"""
nbr_colonne=7*[0]
"""joueur_tour donne le prochain joueur qui va jouer 1 pour ROUGE et un 2 un BLEU"""
joueur_tour = 1
################################
# Fonctions de choix des joueurs
#################################

# La fonction qui_commence() demande à l'utilisateur le joueur qui commence (ROUGE ou BLEU)
#Source du code http://fractale.gecif.net/python/puissance_4/
def qui_commence():
    global joueur_courant
    s=""
    while not s in ["1","2"]:
        s=input("Quel joueur commence ? Entrez 1 pour ROUGE ou 2 pour BLEU :")
    joueur_courant=int(s)


#################################################
#La Fonction afficher_grille renvoie une grille standard
#Source du code http://fractale.gecif.net/python/puissance_4/
def afficher_grille () :
    for i in range (6) :
        print (grille[i])
         # affiche le repère des colonnes sous la grille :
    print('\n 0  1  2  3  4  5  6')
# La Fonction Grille_pleine 
def grille_pleine():
    b_plein=True
    for i in range(6):
        for j in range(7):
            if grille[i][j]==0:
                b_plein=False
    return b_plein
#################################################
# Fonctions de sauvegarde et chargement de partie
#################################################
def sauv () :
    """sauvegarde la configuration du jeu dans un fichier sauvegarde"""
    fic = open ("sauvegarde","w")
    fic.write ()

def load () :
    """Charge la dernière partie enregistré"""
    fic = open ("sauvegarde","r")
    config = 
    ligne = fic.readline()
    n = int(ligne)
    if n != N:
        fic.close()
        return config
    i = j = 1
    for ligne in fic:
        config[i][j] = int(ligne)
        j += 1
        if j == N + 1:
            j = 1
            i += 1
    fic.close()
    return config
    return    
##################################################
# Fonction d'annulation de coup
#################################################
def cancel(self,row) :
    """Annule le dernier coup qui a été joué"""
    rank = 1
    while self.grid[rank][row] != 0:
            rank += 1/    rank = rank - 1
    self.grid[rank][row] = 0

#################################################
# Fonction dessiner grille 
#Source du code http://fractale.gecif.net/python/puissance_4/
#################################################
def dessiner_grille () :
    turtle.up()
    turtle.goto(x_base,y_base)
    turtle.down()
    # traits horizontaux :
    for i in range(8):
        turtle.fd(7*largeur)
        turtle.up()
        turtle.goto(x_base,y_base+i*largeur)
        turtle.down()
    # traits verticaux :
    turtle.up()
    turtle.goto(x_base,y_base)
    turtle.setheading(90)
    turtle.down()
    for i in range(9):
        turtle.forward(6*largeur)
        turtle.up()
        turtle.goto(x_base+i*largeur,y_base)
        turtle.down()
    # affiche le numéro des colonnes sous la grille :
    for i in range(7):
        turtle.up()
        turtle.goto(x_base+i*largeur+largeur//2,y_base-largeur//2)
        turtle.down()
        turtle.write(str(i))
        # La fonction pions_alignes() teste si 4 pions de même couleur sont alignés dans la grille
#Source du code http://fractale.gecif.net/python/puissance_4/
def pions_alignes():
    trouve=0

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # teste 4 pions alignés horizontalement en alanysant chacune des 6 lignes :
    for i in range(6):
        rouge=0
        bleu=0
        for j in range(7):
            if grille[i][j]==1:
                rouge+=1
                bleu=0
                if rouge>=4:
                    trouve=1
                    return trouve
            elif grille[i][j]==2:
                rouge=0
                bleu+=1
                if bleu>=4:
                    trouve=2
                    return trouve
            else:
                rouge=0
                bleu=0

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # teste 4 pions alignés verticalement en analysant chacune des 7 colonnes :
    #Source du code http://fractale.gecif.net/python/puissance_4/
    for j in range(7):
        rouge=0
        bleu=0
        for i in range(6):
            if grille[i][j]==1:
                rouge+=1
                bleu=0
                if rouge>=4:
                    trouve=1
                    return trouve
            elif grille[i][j]==2:
                rouge=0
                bleu+=1
                if bleu>=4:
                    trouve=2
                    return trouve
            else:
                rouge=0
                bleu=0
# ############################################################################
# La fonction dessiner_grille() dessine une grille vide dans la fenêtre de la tortue
def dessiner_grille():
    turtle.up()
    turtle.goto(x_base,y_base)
    turtle.down()
    # traits horizontaux :
    for i in range(8):
        turtle.forward(7*largeur)
        turtle.up()
        turtle.goto(x_base,y_base+i*largeur)
        turtle.down()
    # traits verticaux :
    turtle.up()
    turtle.goto(x_base,y_base)
    turtle.setheading(90)
    turtle.down()
    for i in range(9):
        turtle.forward(6*largeur)
        turtle.up()
        turtle.goto(x_base+i*largeur,y_base)
        turtle.down()
    # affiche le numéro des colonnes sous la grille :
    for i in range(7):
        turtle.up()
        turtle.goto(x_base+i*largeur+largeur//2,y_base-largeur//2)
        turtle.down()
        turtle.write(str(i))
        # ############################################################################
# La fonction dessiner_pion(x,y,couleur) ajoute un pion dans la case (x,y)
def dessiner_pion(x,y,couleur):
    # x de 0 à 6 et y de 0 à 5
    turtle.up()
    turtle.goto(x_base+(x+1)*largeur-largeur//8,y_base+(y+1)*largeur-largeur//2)
    turtle.down()
    if couleur==1:
        # pion ROUGE si couleur=1 :
        turtle.color('red')
    else:
        # pion BLEU si couleur=2 :
        turtle.color('blue')
    turtle.begin_fill()
    turtle.circle(largeur/2.5)
    turtle.end_fill()
############################################################
# Programme principal
###########################################################
largeur=60
x_base=-220
y_base=-150
turtle.setup(7*largeur+30, 430, 0, 0)
turtle.speed(0)
turtle.hideturtle()
dessiner_grille()

