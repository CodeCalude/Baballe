from tkinter import *

cvs_largeur = 700
cvs_hauteur = 500

taille_Balle = 50

#Deplacements de la balle:
dx=5
dy=-10

def deplacement():
    global dx, dy

    #Au limite haute du canvas on inverse le sens
    if MonCanevas.coords(balle)[3]>cvs_hauteur or MonCanevas.coords(balle)[3]<0+taille_Balle:
        dy = -1*dy

    #Au limite de la largeur du canvas on inverse le sens
    if MonCanevas.coords(balle)[2]>cvs_largeur or MonCanevas.coords(balle)[2]<0+taille_Balle:
        dx = -1*dx

    #On deplace la balle :
    MonCanevas.move(balle,dx,dy)
    #On repete cette fonction
    MaFenetre.after(20,deplacement)

#On cree une fenetre et un canevas:
MaFenetre = Tk()
MonCanevas = Canvas(MaFenetre,width = cvs_largeur, height = cvs_hauteur , bd=0, bg="white")
MonCanevas.grid(row=0, column=0, padx=20,pady=20, columnspan=2)

#Creation  d'un bouton "Lancer la balle":
Bouton_Lancer=Button(MaFenetre, text ='Lancer la balle', command = deplacement)
#On ajoute l'affichage du bouton dans la fenêtre tk:
Bouton_Lancer.grid(row=1, column=0, padx=10,pady=10)

#Creation  d'un bouton "Quitter":
Bouton_Quitter=Button(MaFenetre, text ='Quitter', command = MaFenetre.destroy)
#On ajoute l'affichage du bouton dans la fenêtre tk:
Bouton_Quitter.grid(row=1, column=1, padx=10,pady=10)

#On cree une balle rouge:
balle = MonCanevas.create_oval(
    cvs_largeur/2,
    cvs_hauteur/2,
    (cvs_largeur/2)+taille_Balle,
    (cvs_hauteur/2)+taille_Balle,
    fill='red')

#deplacement()
 
#On lance la boucle principale:
MaFenetre.mainloop()