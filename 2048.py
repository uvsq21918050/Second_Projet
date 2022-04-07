#####################################################################
# Docstring
#
# groupe MPCI TD1
# CHRISTOPHE Passcal
# CHAKROUN Mohammed
# KALI-A-NGOUELE Gloire
# https://github.com/uvsq21918050/Second_Projet_2048
#########################################

# ------------------------- Bibliothèques ------------------------- #
import tkinter as tk

# --------------------------- Constante --------------------------- #
HEIGHT_CANVAS = WIDHT_CANVAS = 400
N = 4
# ----------------------- Varaibles Globale ----------------------- #
Score = 0
# ------------------------ Partie Fonction ------------------------ #


def grille():
    """""""""""""""""
    Initialisation de notre grille et de la configuration Courante.
    i et j nous permettent de gérer les coordonnées des points délimitants le
    canvas
    """""""""""""""

    global Grille

    Grille = []  # Grille
    for i in range(0, N):
        intermediaire = []
        for j in range(1, N+1):
            xh = (j-1)*HEIGHT_CANVAS/N
            yh = i*HEIGHT_CANVAS/N
            xb = j*HEIGHT_CANVAS/N
            yb = (i+1)*WIDHT_CANVAS/N
            intermediaire.append(Canvas.create_rectangle(xh, yh, xb, yb,
                                                         fill='grey',
                                                         outline='white'))
        Grille.append(intermediaire)


def Up():
    pass


def Down():
    pass


def Left():
    pass


def Right():
    pass


def End():
    pass


def Load():
    pass


def Save():
    pass


def Calcul():
    pass

# ------------------------ Code Principale ------------------------ #

# Parrametre de la racine et Canvas


racine = tk.Tk()
racine.title("2048")
Canvas = tk.Canvas(bg='white', height=HEIGHT_CANVAS, width=WIDHT_CANVAS)
Plateau = grille()

# Bouttons
Bouton_Play = tk.Button(text='Play')
Bouton_Exit = tk.Button(text="Exit")
Bouton_Save = tk.Button(text="Sauvgarder")
Bouton_Load = tk.Button(text="Charger")
Bouton_Up = tk.Button(text="Haut")
Bouton_Down = tk.Button(text="Bas")
Bouton_Right = tk.Button(text="Droite")
Bouton_Left = tk.Button(text="Gauche")

# Label
Label_Score = tk.Label(text="Score")
# Label_Valeur_Score = tk.Label(textvariable= str(Score))


# Placement des éléments
Label_Score.grid(row=1, column=2)
# Label_Valeur_Score(row=1, column=3)
Canvas.grid(row=2, column=2, columnspan=4, rowspan=5)
Bouton_Play.grid(row=2, column=1)
Bouton_Exit.grid(row=3, column=1)
Bouton_Save.grid(row=4, column=1)
Bouton_Load.grid(row=5, column=1)
Bouton_Up.grid(row=3, column=3)
Bouton_Down.grid(row=4, column=3)
Bouton_Right.grid(row=4, column=2)
Bouton_Left.grid(row=4, column=4)

# mainloop
racine.mainloop()

# ----------------------- Fin du programme  ----------------------- #
