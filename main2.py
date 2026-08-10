import customtkinter as ctk
import backends.longueur_distance as l_d

fenetre = ctk.CTk()

fenetre.geometry("800x600")
fenetre.title("Convertisseur d'unités")

# Configuration des grid de la fenetre
fenetre.grid_columnconfigure(0, weight=1)
fenetre.grid_columnconfigure(1, weight=1)

fenetre.grid_rowconfigure(0, weight=1)
fenetre.grid_rowconfigure(1, weight=1)
fenetre.grid_rowconfigure(2, weight=1)


# Fonction de conversion
def convertir():
    valeur = entree.get()
    depart = unite_depart.get()
    arrivee = unite_arrivee.get()
    print(f"La valeure entree est: {valeur}")
    print(f"Unité de départ: {depart}")
    print(f"L'unité d'arrivée: {arrivee}")
    match depart:
        case "Mètre":
            u1 = "m"
        case "Kilomètre":
            u1 = "km"
        case "Centimètre":
            u1 = "cm"
        case "Millimètre":
            u1 = "mm"            
    match arrivee:
            case "Mètre":
                u2 = "m"
            case "Kilomètre":
                u2 = "km"
            case "Centimètre":
                u2 = "cm"
            case "Millimètre":
                u2 = "mm" 
    resultat = l_d.final_conv(u1, u2, valeur)
    print(resultat)


# Premier frame
frame1 = ctk.CTkFrame(fenetre)
frame1.grid(
    row=0, 
    column=0,
    columnspan=2,
    sticky="nsew" # Frame1 s'étire dans toute la cellule
)

# Label du frame1 donc le titre
titre = ctk.CTkLabel(
    frame1,
    text="Convertisseur d'unités",
    font=("Arial", 28, "bold")
)
titre.grid(
    row=0, 
    column=0,
    padx=20,
    pady=20
)

# Configuration des grid de frame1
frame1.grid_columnconfigure(0, weight=1)
frame1.grid_rowconfigure(0, weight=1)



# Deuxième frame
frame2 = ctk.CTkFrame(fenetre)
frame2.grid(
    row=1,
    column=0,
    sticky="nsew"
)

# Configuration des grids de frame2
frame2.grid_columnconfigure(0, weight=1)
frame2.grid_rowconfigure(0, weight=1)
frame2.grid_rowconfigure(1, weight=1)
frame2.grid_rowconfigure(2, weight=1)
frame2.grid_rowconfigure(3, weight=1)
frame2.grid_rowconfigure(4, weight=1)

# Label "Valeur"
label_valeur = ctk.CTkLabel(
    frame2,
    text="Valeur"
)
label_valeur.grid(
    row=0,
    column=0,
    pady=10
)

# Champs de saisie
entree = ctk.CTkEntry(
    frame2,
    placeholder_text="Entrez une valeur"
    )
entree.grid(
    row=1,
    column=0,
    padx=30,
    pady=10,
    sticky="ew" # S'étire horizontalement avec la largeur disponible
)

# Choix de l'unité avec une liste déroulante on utilisant combobox
unite_depart = ctk.CTkComboBox(
    frame2,
    values=[
        "Mètre",
        "Kilomètre",
        "Centimètre",
        "Millimètre"
    ])
unite_depart.grid(
    row=2,
    column=0,
    padx=30,
    pady=10,
    sticky="ew"
)

unite_arrivee = ctk.CTkComboBox(
    frame2,
    values=[
        "Mètre",
        "Kilomètre",
        "Centimètre",
        "Millimètre"
    ])
unite_arrivee.grid(
    row=3,
    column=0,
    padx=30,
    pady=10,
    sticky="ew"
)

# Bouton de conversion
bouton_convertir = ctk.CTkButton(
    frame2,
    text="Convertir",
    command=convertir
    )
bouton_convertir.grid(
    row=4,
    column=0,
    padx=30, 
    pady=15    
)


# Troisième frame
frame3 = ctk.CTkFrame(fenetre)
frame3.grid(
    row=1,
    column=1,
    sticky="nsew"
)


# LOGIQUES






fenetre.mainloop()