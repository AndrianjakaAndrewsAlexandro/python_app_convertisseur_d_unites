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

# Créations Widgets

# Les frames
#Frame du titre
frm_titre = ctk.CTkFrame(fenetre, fg_color=bg, border_color=fg, border_width=2)


# Frame principal
frm_principal = ctk.CTkFrame(fenetre, fg_color=blue, border_color=blue, border_width=2, height=550)
frm_principal.grid_columnconfigure(0, weight=1) # Diviser en quatres colonnes le collones 0 a une seule part
frm_principal.grid_columnconfigure(1, weight=3) # Le colonnes 1 a trois parts

#Frame des options
frm_option = ctk.CTkFrame(frm_principal, fg_color=bg, border_color=fg, border_width=2)

# Frame de la converion principale
frm_conv_principal = ctk.CTkFrame(frm_principal, fg_color=bg, border_color=fg, border_width=2)

# Les labels
#Titres
label_titre = ctk.CTkLabel(frm_titre, text="Convertisseur d'Unités")
label_titre.configure(font=("Aria", 26, "bold"), text_color=fg)
label_titre_info = ctk.CTkLabel(frm_titre, text="Transforme mesure entre différents systèmes (métrique, impérial, ect...)")
label_titre_info.configure(font=("Aria", 15, "bold"), text_color=fg)


# Les labels dans frame optins
#label_longeur = ctk.CTkLabel(frm_option, text="Longueur", text_color=fg)








# Placement des widgets
frm_titre.pack(pady=20, padx= 20, fill="x", ipady=10)
frm_principal.pack(padx=25, fill="both", ipadx= 10)
label_titre.pack()
label_titre_info.pack()
frm_option.grid(column=0, row=0, padx=5, sticky = "nsew") # "nsew" permet e proncdre rour epave
frm_conv_principal.grid(column=1,row=0, padx=5, sticky = "nsew")
#label_longeur.pack()














fenetre.mainloop()