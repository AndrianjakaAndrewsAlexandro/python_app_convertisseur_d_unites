# Convertisseur d'unités

# Importations
import customtkinter as ctk


# les fonctions
def pourcentage_larg(pourc):
    return (pourc * largeur_fenetre)/100

def pourcentage_haut(pourc):
    return (pourc * hauteur_fenetre)/100

# Création de la fenetre
fenetre = ctk.CTk()
fenetre.title("Convertisseur d'unités")

# Les varibales
bg = "white"
fg = "black"
blue = "#00F"



# Centrage et taille initiale de la fenêtre
largeur_fenetre = 800
hauteur_fenetre = 600

largeur_ecran = fenetre.winfo_screenwidth()
hauteur_ecran = fenetre.winfo_screenheight()

position_fenetre_largeur = (largeur_ecran // 2) - (largeur_fenetre // 2)
position_fenetre_hauteur = (hauteur_ecran // 2) - (hauteur_fenetre // 2)

fenetre.geometry(f"{largeur_fenetre}x{hauteur_fenetre}+{position_fenetre_largeur}+{position_fenetre_hauteur}")
fenetre.configure(fg_color=bg)
fenetre.iconbitmap("icons/logo.ico")

# Configuration des grid de la fenetre
fenetre.grid_columnconfigure(0, weight=1)
fenetre.grid_rowconfigure(0, weight=1)
fenetre.grid_rowconfigure(1, weight=20)

# Créations Widgets

# Les frames
#Frame du titre
frm_titre = ctk.CTkFrame(
    fenetre, 
    fg_color=bg, 
    )
frm_titre.grid(pady=10, 
               padx= 10, 
               sticky= "nesw", 
               ipady=10,
               column=0,
               row=0
               )
# Configuration des grids du frame de titre
frm_titre.grid_columnconfigure(0, weight=1)
frm_titre.grid_rowconfigure(0, weight=1)
frm_titre.grid_rowconfigure(1, weight=1)

#Titres
label_titre = ctk.CTkLabel(frm_titre, 
                           text="Convertisseur d'Unités"
                           )
label_titre.configure(font=("Aria", 26, "bold"), 
                      text_color=fg)
label_titre.grid(
    column=0,
    row=0,
    sticky="ew"
)


label_titre_info = ctk.CTkLabel(frm_titre, 
                                text="Transforme mesure entre différents systèmes (métrique, impérial, ect...)"
                                )
label_titre_info.configure(font=("Aria", 15, "bold"), 
                           text_color=fg)
label_titre_info.grid(
    column=0,
    row=1,
    sticky="ew"
)


# Frame principal
frm_principal = ctk.CTkFrame(fenetre, 
                             fg_color=bg 
                             )
frm_principal.grid(padx=10, 
                   pady=(0, 0),
                   sticky="nesw", 
                   ipadx= 10,
                   column=0,
                   row=1)

#Configuration de Frame principal
frm_principal.grid_columnconfigure(0, weight=1) # Diviser en quatres colonnes le collones 0 a une seule part
frm_principal.grid_columnconfigure(1, weight=20) # Le colonnes 1 a trois parts
frm_principal.grid_rowconfigure(0, weight=1)

#Frame des options
frm_option = ctk.CTkFrame(frm_principal, 
                          fg_color=bg, 
                          border_color=fg, 
                          border_width=2)
frm_option.grid(column=0, 
                row=0, 
                padx=2, 
                sticky = "nsew") # "nsew" permet e proncdre rour epave

# Frame de la converion principale
frm_conv_principal = ctk.CTkFrame(frm_principal, fg_color=bg, border_color=fg, border_width=2)
frm_conv_principal.grid(column=1, 
                        row=0, 
                        padx=2, 
                        sticky = "nsew")















fenetre.mainloop()