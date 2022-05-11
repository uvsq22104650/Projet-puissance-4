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

"""joueur_tour donne le prochain joueur qui va jouer 1 pour ROUGE et un 2 un BLEU"""
joueur_tour = 1
################################
# Fonctions de choix des joueurs
#################################

# tab_colonne mémorise le nombre de pions dans chacune des colonnes
tab_colonne=7*[0]
# joueur_courant indique le prochain joueur qui doit jouer : 1 pour ROUGE et 2 pour BLEU
joueur_courant=1
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

# La fonction pions_alignes() teste si 4 pions de même couleur sont alignés dans la grille
#Source du code http://fractale.gecif.net/python/puissance_4/

def pions_alignes():
    trouve=0

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # teste 4 pions alignés horizontalement en analysant chacune des 6 lignes :
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
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # teste les 6 diagonales croissantes :
     # test des 2 diagonales croissantes à 4 cases :
     #Source du code http://fractale.gecif.net/python/puissance_4/
    rouge=[0,0]
    bleu=[0,0]

    for j in range(4):
        i=3-j
        k=i+2
        l=j+3
        if grille[i][j]==1:
            rouge[0]+=1
            bleu[0]=0
            if rouge[0]>=4:
                trouve=1
                return trouve
        elif grille[i][j]==2:
            rouge[0]=0
            bleu[0]+=1
            if bleu[0]>=4:
                trouve=2
                return trouve
        else:
            rouge[0]=0
            bleu[0]=0

        if grille[k][l]==1:
            rouge[1]+=1
            bleu[1]=0
            if rouge[1]>=4:
                trouve=1
                return trouve
        elif grille[k][l]==2:
            rouge[1]=0
            bleu[1]+=1
            if bleu[1]>=4:
                trouve=2
                return trouve
        else:
            rouge[1]=0
            bleu[1]=0

    # test des 2 diagonales croissantes à 5 cases :
    #Source du code http://fractale.gecif.net/python/puissance_4/
    rouge=[0,0]
    bleu=[0,0]

    for j in range(5):
        i=4-j
        k=i+1
        l=j+2
        if grille[i][j]==1:
            rouge[0]+=1
            bleu[0]=0
            if rouge[0]>=4:
                trouve=1
                return trouve
        elif grille[i][j]==2:
            rouge[0]=0
            bleu[0]+=1
            if bleu[0]>=4:
                trouve=2
                return trouve
        else:
            rouge[0]=0
            bleu[0]=0

        if grille[k][l]==1:
            rouge[1]+=1
            bleu[1]=0
            if rouge[1]>=4:
                trouve=1
                return trouve
        elif grille[k][l]==2:
            rouge[1]=0
            bleu[1]+=1
            if bleu[1]>=4:
                trouve=2
                return trouve
        else:
            rouge[1]=0
            bleu[1]=0

    # test des 2 diagonales croissantes à 6 cases :
    #Source du code http://fractale.gecif.net/python/puissance_4/
    rouge=[0,0]
    bleu=[0,0]

    for j in range(6):
        i=5-j
        k=i
        l=j+1
        if grille[i][j]==1:
            rouge[0]+=1
            bleu[0]=0
            if rouge[0]>=4:
                trouve=1
                return trouve
        elif grille[i][j]==2:
            rouge[0]=0
            bleu[0]+=1
            if bleu[0]>=4:
                trouve=2
                return trouve
        else:
            rouge[0]=0
            bleu[0]=0

        if grille[k][l]==1:
            rouge[1]+=1
            bleu[1]=0
            if rouge[1]>=4:
                trouve=1
                return trouve
        elif grille[k][l]==2:
            rouge[1]=0
            bleu[1]+=1
            if bleu[1]>=4:
                trouve=2
                return trouve
        else:
            rouge[1]=0
            bleu[1]=0
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # teste les 6 diagonales décroissantes :
     # test des 2 diagonales décroissantes à 4 cases :
     #Source du code http://fractale.gecif.net/python/puissance_4/
    rouge=[0,0]
    bleu=[0,0]

    for j in range(3,7):
        i=j-3
        k=j-1
        l=i
        if grille[i][j]==1:
            rouge[0]+=1
            bleu[0]=0
            if rouge[0]>=4:
                trouve=1
                return trouve
        elif grille[i][j]==2:
            rouge[0]=0
            bleu[0]+=1
            if bleu[0]>=4:
                trouve=2
                return trouve
        else:
            rouge[0]=0
            bleu[0]=0

        if grille[k][l]==1:
            rouge[1]+=1
            bleu[1]=0
            if rouge[1]>=4:
                trouve=1
                return trouve
        elif grille[k][l]==2:
            rouge[1]=0
            bleu[1]+=1
            if bleu[1]>=4:
                trouve=2
                return trouve
        else:
            rouge[1]=0
            bleu[1]=0

    # test des 2 diagonales décroissantes à 5 cases :
    #Source du code http://fractale.gecif.net/python/puissance_4/
    rouge=[0,0]
    bleu=[0,0]

    for j in range(2,7):
        i=j-2
        k=j-1
        l=i
        if grille[i][j]==1:
            rouge[0]+=1
            bleu[0]=0
            if rouge[0]>=4:
                trouve=1
                return trouve
        elif grille[i][j]==2:
            rouge[0]=0
            bleu[0]+=1
            if bleu[0]>=4:
                trouve=2
                return trouve
        else:
            rouge[0]=0
            bleu[0]=0

        if grille[k][l]==1:
            rouge[1]+=1
            bleu[1]=0
            if rouge[1]>=4:
                trouve=1
                return trouve
        elif grille[k][l]==2:
            rouge[1]=0
            bleu[1]+=1
            if bleu[1]>=4:
                trouve=2
                return trouve
        else:
            rouge[1]=0
            bleu[1]=0

    # test des 2 diagonales décroissantes à 6 cases :
    #Source du code http://fractale.gecif.net/python/puissance_4/
    rouge=[0,0]
    bleu=[0,0]

    for j in range(1,7):
        i=j-1
        k=i
        l=i
        if grille[i][j]==1:
            rouge[0]+=1
            bleu[0]=0
            if rouge[0]>=4:
                trouve=1
                return trouve
        elif grille[i][j]==2:
            rouge[0]=0
            bleu[0]+=1
            if bleu[0]>=4:
                trouve=2
                return trouve
        else:
            rouge[0]=0
            bleu[0]=0

        if grille[k][l]==1:
            rouge[1]+=1
            bleu[1]=0
            if rouge[1]>=4:
                trouve=1
                return trouve
        elif grille[k][l]==2:
            rouge[1]=0
            bleu[1]+=1
            if bleu[1]>=4:
                trouve=2
                return trouve
        else:
            rouge[1]=0
            bleu[1]=0



    # si on n'a rien trouvé on retourne 0 :
    return trouve

    # La fonction tester_saisie demande au joueur de saisir un nombre entre 0 et 6,
# et réitère la demande tant que la valeur saisie n'ets pas un entier dans cet intervale
#Source du code http://fractale.gecif.net/python/puissance_4/
def tester_saisie():
    global grille,joueur_courant,tab_colonne
    if joueur_courant==1:
        joueur='ROUGE'
    else:
        joueur='BLEU'
    saisie_correct=False
    # gestion des erreur et filtrage des entrées : demande une saisie jusqu'à ce que la valeur entrée soit un chiffre entre 0 et 6
    # Les messages d'erreurs orientant l'utilisateur sont affichés sur la sortie standard (sans provoquer d'erreur)
    while not saisie_correct:
        s_colonne=input("%s : entrez la colonne où jouer (de 0 à 6) :" % joueur)
#################################################
# Fonction d'arrêt de la partie
#Source du code http://fractale.gecif.net/python/puissance_4/
#################################################
    if s_colonne.upper()=='F':
 #quitte le programme et ferme la fenêtre de la tortue si l'utilisateur saise f (comme fin)
            print("Fin du programme car l'utilisateur a saisie F")
            bye()
            exit()

#################################################
# Fonctions de sauvegarde et chargement de partie
#Source du code http://fractale.gecif.net/python/puissance_4/
#################################################
    elif s_colonne.upper()=='S':
            # sauvegarde la sérialisation de la grille dans un fichier texte :
            fic=open('grille.txt','w')
            # convertit l'objet liste grile en chaine de caractères (sérialistation) :
            serialisation=str(grille)
            # enregistre la grille sur la première ligne du fichier grille.txt :
            fic.write(serialisation)
            fic.write('\n')
            # enregistre le joueur courant sur la deuxième ligne du fichier grille.txt :
            fic.write(str(joueur_courant))
            fic.close()
            print("\nL'état de la partie vient d'être enregistré dans le fichier grille.txt mais la partie continue.")
            print("C'est encore au joueur %s à jouer." % joueur)
    elif s_colonne.upper()=='R':
            if os.path.exists('grille.txt'):
                # restaure la grille et le joueur courant à partir du fichier texte grille.txt :
                fic=open('grille.txt','r')
                # fic est un itérateur pointant sur les lignes du fichier : on le convertit en liste
                ligne=list(fic)
                fic.close()
                # première ligne sans le \n : c'est la grille
                s_grille=ligne[0].strip()
                # deuxième ligne sans le \n : c'est le joueur courant
                s_joueur_courant=ligne[1].strip()
                # désérialisation des objets enregistrés en chaine de caractères :
                grille=eval(s_grille)
                joueur_courant=eval(s_joueur_courant)
                # ré-initialise la grille graphique dans la fenêtre de la tortue :
                reset()
                speed(0)
                hideturtle()
                dessiner_grille()
                # compte le nombre de pions dans chaque colonne et complète la grille graphique :
                tab_colonne=7*[0]
                for i in range(6):
                    for j in range(7):
                        if grille[i][j]!=0:
                            tab_colonne[j]+=1
                            dessiner_pion(j,5-i,grille[i][j])
                        print('\n\n\n\n\n\n=============================================')
                print(' PUISSANCE 4 : FINIR UNE PARTIE')
                print('=============================================')
                if joueur_courant==1:
                    joueur='ROUGE'
                else:
                    joueur='BLEU'
                print("\nL'état de la partie vient d'être restaurée à partir du fichier grille.txt.")
                print("C'est au joueur %s à jouer." % joueur)
                afficher_grille()
            else:
                print("\nLe fichier grille.txt n'existe pas.")
                print("Avant de vouloir restaurer une partie avec la commande R il faut en sauvegarder une avec la commande S.")

        # teste si la chaine saise est un entier :
    elif not s_colonne.isdigit():
            print("Erreur de saise : la valeur entrée par le joueur %s n'est pas un nombre entier. Recommencez." % joueur)
        # teste si la valeur numérique est comprise entre 0 et 6 :
    elif int(s_colonne)<0 or int(s_colonne)>6:
            print("Erreur de saise : la valeur numérique entrée par le joueur %s n'est pas comprise entre 0 et 6. Recommencez." % joueur)
    else:
            saisie_correct=True
    # la chaine s_colonne est un chiffre entre 0 et 6 : on la convertit en entier et on la renvoie
    return int(s_colonne)


##################################################
# Fonction d'annulation de coup
#################################################

# ############################################################################
# La fonction jouer() demande au joueur courant dans quelle colonne (de 0 à 6) il veut jouer
#Source du code http://fractale.gecif.net/python/puissance_4/

def jouer():
    global joueur_courant
    joueur=["ROUGE","BLEU"]
    # La fonction tester_saisie renvoie forcément un chiffre entre 0 et 6 :
    colonne=tester_saisie()
    while tab_colonne[colonne]==6:
        print('La colonne %d est pleine ! %s jouez dans une colonne non pleine' % (colonne,joueur[joueur_courant-1]))
        colonne=tester_saisie()
    grille[5-tab_colonne[colonne]][colonne]=joueur_courant
    # dessine le pion sur la grille graphique :
    dessiner_pion(colonne,tab_colonne[colonne],joueur_courant)
    tab_colonne[colonne]+=1
    print('\nLe joueur %s vient de jouer dans la colonne %d :' % (joueur[joueur_courant-1],colonne))
    
    

 

# ############################################################################
# La fonction dessiner_grille() dessine une grille vide dans la fenêtre de la tortue
#Source du code http://fractale.gecif.net/python/puissance_4/
def dessiner_grille():
    up()
    goto(x_base,y_base)
    down()
    # traits horizontaux :
    for i in range(8):
        forward(7*largeur)
        up()
        goto(x_base,y_base+i*largeur)
        down()
    # traits verticaux :
    up()
    goto(x_base,y_base)
    setheading(90)
    down()
    for i in range(9):
        forward(6*largeur)
        up()
        goto(x_base+i*largeur,y_base)
        down()
    # affiche le numéro des colonnes sous la grille :
    for i in range(7):
        up()
        goto(x_base+i*largeur+largeur//2,y_base-largeur//2)
        down()
        write(str(i))
        # ############################################################################
# La fonction dessiner_pion(x,y,couleur) ajoute un pion dans la case (x,y)
#Source du code http://fractale.gecif.net/python/puissance_4/
def dessiner_pion(x,y,couleur):
    # x de 0 à 6 et y de 0 à 5
    up()
    goto(x_base+(x+1)*largeur-largeur//8,y_base+(y+1)*largeur-largeur//2)
    down()
    if couleur==1:
        # pion ROUGE si couleur=1 :
        color('red')
    else:
        # pion BLEU si couleur=2 :
        color('blue')
    begin_fill()
    circle(largeur/2.5)
    end_fill()
############################################################
# Programme principal
###########################################################
largeur=60
x_base=-220
y_base=-150
setup(7*largeur+30, 430, 0, 0)
speed(0)
hideturtle() 
dessiner_grille()

print('\n\n\n\n\n\n=============================================')
print(' PUISSANCE 4 : NOUVELLE PARTIE')
print('=============================================\n\n')
print("Avant de lancer le programme réduisez la fenêtre de Python sur la moitié droite de l'écran.")
print("La fenêtre de la tortue sera affichée dans le coin supérieur gauche de l'écran.\n\n")
qui_commence()
print('Caractères particuliers à saisir à la place du numéro de la colonne à jouer :')
print('S : Sauvegarde la partie dans le fichier grille.txt')
print('R : Restaure la partie à partir du fichier grille.txt')
print('F : Fin du jeu (pour quitter le programme)')
print ('A:Annule de dernier coup du fichier grille.txt')
print('\nLe nom des joueurs sera ici ROUGE et BLEU.')
if joueur_courant==1:
    print('Le joueur ROUGE commence.')
else:
    print('Le joueur BLEU commence.')
print('\nDébut de la partie (la grille est vide) :')
gagnant=0
while not grille_pleine() and gagnant==0:
    afficher_grille()
    jouer()
    joueur_courant=3-joueur_courant
    gagnant=pions_alignes()
    if gagnant==1:
        print('Bravo ! Le joueur ROUGE a gagné !')
    elif gagnant==2:
        print('Bravo ! Le joueur BLEU a gagné !')


afficher_grille()
if gagnant==0:
    print("Fin de la partie : la grille est pleine et il n'y a pas 4 pions alignés")
elif grille_pleine():
    print("Fin de la partie : 4 pions sont alignés et la grille est pleine")
else:
    print("Fin de la partie : 4 pions sont alignés et la grille n'est pas pleine")

done()
##########################################
# Fin Du Programme
##########################################