############################
# importation des librairie
############################

import tkinter as tk
import os,random
import turtle



############################
# Constantes
############################

nb_lignes = 6
nb_colonnes = 7





################################
# Creation de la grille
################################
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
def qui_commence():
    global joueur_courant
    s=""
    while not s in ["1","2"]:
        s=input("Quel joueur commence ? Entrez 1 pour ROUGE ou 2 pour BLEU :")
    joueur_courant=int(s)


#################################################
#La Fonction afficher_grille renvoie une grille standard
def afficher_grille () :
    for i in range (6) :
        print (grille[i])


#################################################
# Fonctions de sauvegarde et chargement de partie
#################################################
def sauv () :
    """sauvegarde la configuration du jeu dans un fichier sauvegarde"""
    fic = open ("sauvegarde","w")
    fic.write ()

def load () :
    
