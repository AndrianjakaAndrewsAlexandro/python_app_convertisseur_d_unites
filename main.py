# Convertisseur d'unités

# Importations
import customtkinter as ctk
import tkinter
from tkinter import messagebox
from PIL import ImageTk, Image

from backends.longueur_distance import *
from backends.poids_masse import *
from backends.volume_capacite import *
from backends.temperature import *
from backends.surface import *
from backends.vitesse import *
from backends.temps import *
from backends.donnees import *

#Les thèmes sombre et clair
def light_mode():
    # Les backgrounds
    fenetre.configure(fg_color="white")
    frm_titre.configure(fg_color="white")
    frm_principal.configure(fg_color="white")
    frm_conv_principal.configure(fg_color="white")
    frm_option.configure(fg_color="white")
    frm_conversion.configure(fg_color="white")
    frm_parametre.configure(fg_color="white")
    frm_de.configure(fg_color="white")
    frm_vers.configure(fg_color="white")
    frm_table_conv.configure(fg_color="white")
    frm_conv_rapide.configure(fg_color="white")

    btn_longueur.configure(fg_color="white", text_color="black")
    btn_volume.configure(fg_color="white", text_color="black")
    btn_masse.configure(fg_color="white", text_color="black")
    btn_surface.configure(fg_color="white", text_color="black")
    btn_informatique.configure(fg_color="white", text_color="black")
    btn_temperature.configure(fg_color="white", text_color="black")
    btn_temps.configure(fg_color="white", text_color="black")
    btn_vitesse.configure(fg_color="white", text_color="black")
    bouton_conversion.configure(text_color="black")
    btn_clair.configure(fg_color="white", text_color="black")
    btn_sombre.configure(fg_color="white", text_color="black")

    label_de.configure(fg_color="white", text_color="black")
    label_vers.configure(fg_color="white", text_color="black")
    label_titre.configure(fg_color="white", text_color="black")
    label_titre_info.configure(fg_color="white", text_color="black")

    entree_de.configure(fg_color="white", text_color="black")
    entree_vers.configure(fg_color="white", text_color="black")

    combobox_de.configure(fg_color="white", text_color="black", dropdown_fg_color="white", dropdown_text_color="black")
    combobox_vers.configure(fg_color="white", text_color="black", dropdown_fg_color="white", dropdown_text_color="black")

def night_mode():
    # Les backgrounds
    fenetre.configure(fg_color="black", text_color="white")
    frm_titre.configure(fg_color="black")
    frm_principal.configure(fg_color="black")
    frm_conv_principal.configure(fg_color="black")
    frm_option.configure(fg_color="black")
    frm_conversion.configure(fg_color="black")
    frm_parametre.configure(fg_color="black")
    frm_de.configure(fg_color="black")
    frm_vers.configure(fg_color="black")
    frm_table_conv.configure(fg_color="black")
    frm_conv_rapide.configure(fg_color="black")

    btn_longueur.configure(fg_color="black", text_color="white")
    btn_volume.configure(fg_color="black", text_color="white")
    btn_masse.configure(fg_color="black", text_color="white")
    btn_surface.configure(fg_color="black", text_color="white")
    btn_informatique.configure(fg_color="black", text_color="white")
    btn_temperature.configure(fg_color="black", text_color="white")
    btn_temps.configure(fg_color="black", text_color="white")
    btn_vitesse.configure(fg_color="black", text_color="white")
    bouton_conversion.configure(text_color="white")
    btn_clair.configure(fg_color="black", text_color="white")
    btn_sombre.configure(fg_color="black", text_color="white")

    label_de.configure(fg_color="black", text_color="white")
    label_vers.configure(fg_color="black", text_color="white")
    label_titre.configure(fg_color="black", text_color="white")
    label_titre_info.configure(fg_color="black", text_color="white")

    entree_de.configure(fg_color="black", text_color="white")
    entree_vers.configure(fg_color="black", text_color="white")

    combobox_de.configure(fg_color="black", text_color="white", dropdown_fg_color="black", dropdown_text_color="white",)
    combobox_vers.configure(fg_color="black", text_color="white", dropdown_fg_color="black", dropdown_text_color="white",)
    
    


    # Je continuerai plus tard    



# les fonctions
def error_message():
    error = messagebox.showerror("Erreur", "Veuillez d'abord entrer la domaine de mésure à utiliser qui se situe à votre gauche", parent=fenetre) 

def error_verification():
    listes = [".", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    vide = ""
    if entree_de.get() == vide:
        error = messagebox.showerror("Erreur", "Veuillez entrer une valeur pour effectuer la conversion")
    for i in entree_de.get():
        if i not in listes:
            error = messagebox.showerror("Erreur", "Veuillez entrer une valeur valide pour la conversion")
            entree_de.set(vide)
            break
    if combobox_de.get() == vide:
        error = messagebox.showerror("Erreur", "Pour aboutir à la conversion, veuillez entrer l'unité à convertir", parent=fenetre)    
    if combobox_vers.get() == vide:
        error = messagebox.showerror("Erreur", "Pour aboutir à la conversion, veuillez entrer l'unité à convertir", parent=fenetre)

def racc_error_verification():
    listes = [".", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    vide = ""
    if entree_de.get() == vide:
        error = messagebox.showerror("Erreur", "Veuillez entrer une valeur pour effectuer la conversion")
    for i in entree_de.get():
        if i not in listes:
            error = messagebox.showerror("Erreur", "Veuillez entrer une valeur valide pour la conversion")
            entree_de.set(vide)
            break
    


def fonction_longueur():
    bouton_conversion.configure(command=convertir_longueur)

    combobox_de.configure(values=["Kilomètre (km)", "Héctomètre (hm)", "Décamètre (dam)", "Mètre (m)", "Décimètre (dm)", "Centimètre (cm)", "Milimètre (mm)", "Pouces (in)", "Pieds (ft)", "Yards (yd)", "Miles (mi)"])
    combobox_vers.configure(values=["Kilomètre (km)", "Héctomètre (hm)", "Décamètre (dam)", "Mètre (m)", "Décimètre (dm)", "Centimètre (cm)", "Milimètre (mm)", "Pouces (in)", "Pieds (ft)", "Yards (yd)", "Miles (mi)"]) 

    racc_longueur()    

    if frm_principal.cget("fg_color") == "white":

        btn_longueur.configure(fg_color=blue, text_color=bg)
        btn_masse.configure(fg_color=bg, text_color=fg)
        btn_volume.configure(fg_color=bg, text_color=fg)
        btn_temperature.configure(fg_color=bg, text_color=fg)
        btn_surface.configure(fg_color=bg, text_color=fg)
        btn_vitesse.configure(fg_color=bg, text_color=fg)
        btn_temps.configure(fg_color=bg, text_color=fg)
        btn_informatique.configure(fg_color=bg, text_color=fg)

    elif frm_principal.cget("fg_color") == "black":   
        btn_longueur.configure(fg_color=blue, text_color=bg)
        btn_masse.configure(fg_color=fg, text_color=bg)
        btn_volume.configure(fg_color=fg, text_color=bg)
        btn_temperature.configure(fg_color=fg, text_color=bg)
        btn_surface.configure(fg_color=fg, text_color=bg)
        btn_vitesse.configure(fg_color=fg, text_color=bg)
        btn_temps.configure(fg_color=fg, text_color=bg)
        btn_informatique.configure(fg_color=fg, text_color=bg) 
    
    

def fonction_masse():
    bouton_conversion.configure(command=convertir_masse)

    combobox_de.configure(values=["Tonne (t)", "Quintal (q)", "Dizaine de kilogramme (dkg)", "Kilogramme (kg)", "Héctogramme (hg)", "Décagramme (dag)", "Gramme (g)", "Décigramme (dg)", "Centigramme (cg)", "Milligramme (mg)", "Once (oz)", "Livre (lb)"])
    combobox_vers.configure(values=["Tonne (t)", "Quintal (q)", "Dizaine de kilogramme (dkg)", "Kilogramme (kg)", "Héctogramme (hg)", "Décagramme (dag)", "Gramme (g)", "Décigramme (dg)", "Centigramme (cg)", "Milligramme (mg)", "Once (oz)", "Livre (lb)"]) 
    
    racc_masse()
    
    if frm_principal.cget("fg_color") == "white":
    
            btn_masse.configure(fg_color=blue, text_color=bg)
            btn_longueur.configure(fg_color=bg, text_color=fg)
            btn_volume.configure(fg_color=bg, text_color=fg)
            btn_temperature.configure(fg_color=bg, text_color=fg)
            btn_surface.configure(fg_color=bg, text_color=fg)
            btn_vitesse.configure(fg_color=bg, text_color=fg)
            btn_temps.configure(fg_color=bg, text_color=fg)
            btn_informatique.configure(fg_color=bg, text_color=fg)
    
    elif frm_principal.cget("fg_color") == "black":   
            btn_masse.configure(fg_color=blue, text_color=bg)
            btn_longueur.configure(fg_color=fg, text_color=bg)
            btn_volume.configure(fg_color=fg, text_color=bg)
            btn_temperature.configure(fg_color=fg, text_color=bg)
            btn_surface.configure(fg_color=fg, text_color=bg)
            btn_vitesse.configure(fg_color=fg, text_color=bg)
            btn_temps.configure(fg_color=fg, text_color=bg)
            btn_informatique.configure(fg_color=fg, text_color=bg)
    

def fonction_volume():
    bouton_conversion.configure(command=convertir_volume)

    combobox_de.configure(values=["Kilolitre (kl)", "Héctolitre (hl)", "Décalitre (dal)", "Litre (l)", "Décilitre (dl)", "Centilitre (cl)", "Millilitre (ml)", "Mètre cube (m3)", "Décimètre cube (dm3)", "Centimètre cube (cm3)", "Millimètre cube (mm3)", "Onces (oz)", "Tasses", "Pintes", "Gallons"])
    combobox_vers.configure(values=["Kilolitre (kl)", "Héctolitre (hl)", "Décalitre (dal)", "Litre (l)", "Décilitre (dl)", "Centilitre (cl)", "Millilitre (ml)", "Mètre cube (m3)", "Décimètre cube (dm3)", "Centimètre cube (cm3)", "Millimètre cube (mm3)", "Onces (oz)", "Tasses", "Pintes", "Gallons"]) 
    
    racc_volume()

    if frm_principal.cget("fg_color") == "white":
    
            btn_volume.configure(fg_color=blue, text_color=bg)
            btn_masse.configure(fg_color=bg, text_color=fg)
            btn_longueur.configure(fg_color=bg, text_color=fg)
            btn_temperature.configure(fg_color=bg, text_color=fg)
            btn_surface.configure(fg_color=bg, text_color=fg)
            btn_vitesse.configure(fg_color=bg, text_color=fg)
            btn_temps.configure(fg_color=bg, text_color=fg)
            btn_informatique.configure(fg_color=bg, text_color=fg)
    
    elif frm_principal.cget("fg_color") == "black":   
            btn_volume.configure(fg_color=blue, text_color=bg)
            btn_masse.configure(fg_color=fg, text_color=bg)
            btn_longueur.configure(fg_color=fg, text_color=bg)
            btn_temperature.configure(fg_color=fg, text_color=bg)
            btn_surface.configure(fg_color=fg, text_color=bg)
            btn_vitesse.configure(fg_color=fg, text_color=bg)
            btn_temps.configure(fg_color=fg, text_color=bg)
            btn_informatique.configure(fg_color=fg, text_color=bg)

    

def fonction_temperature():
    bouton_conversion.configure(command=convertir_temperature)

    combobox_de.configure(values=["Kelvin (°K)", "Celcius (°C)", "Fahrenheit (°F)"])
    combobox_vers.configure(values=["Kelvin (°K)", "Celcius (°C)", "Fahrenheit (°F)"])      
    
    racc_temperature()

    if frm_principal.cget("fg_color") == "white":
    
            btn_temperature.configure(fg_color=blue, text_color=bg)
            btn_masse.configure(fg_color=bg, text_color=fg)
            btn_volume.configure(fg_color=bg, text_color=fg)
            btn_longueur.configure(fg_color=bg, text_color=fg)
            btn_surface.configure(fg_color=bg, text_color=fg)
            btn_vitesse.configure(fg_color=bg, text_color=fg)
            btn_temps.configure(fg_color=bg, text_color=fg)
            btn_informatique.configure(fg_color=bg, text_color=fg)
    
    elif frm_principal.cget("fg_color") == "black":   
            btn_temperature.configure(fg_color=blue, text_color=bg)
            btn_masse.configure(fg_color=fg, text_color=bg)
            btn_volume.configure(fg_color=fg, text_color=bg)
            btn_longueur.configure(fg_color=fg, text_color=bg)
            btn_surface.configure(fg_color=fg, text_color=bg)
            btn_vitesse.configure(fg_color=fg, text_color=bg)
            btn_temps.configure(fg_color=fg, text_color=bg)
            btn_informatique.configure(fg_color=fg, text_color=bg)

    

def fonction_surface():
    bouton_conversion.configure(command=convertir_surface)

    combobox_de.configure(values=["Kilomètre carré (km2)", "Héctare (ha)", "Aire (a)", "Mètre carré (m2)", "Décimètre carré (dm2)", "Centimètre carré (cm2)", "Millimètre carré (mm2)"])
    combobox_vers.configure(values=["Kilomètre carré (km2)", "Héctare (ha)", "Aire (a)", "Mètre carré (m2)", "Décimètre carré (dm2)", "Centimètre carré (cm2)", "Millimètre carré (mm2)"])
    
    racc_surface()

    if frm_principal.cget("fg_color") == "white":
    
            btn_surface.configure(fg_color=blue, text_color=bg)
            btn_masse.configure(fg_color=bg, text_color=fg)
            btn_volume.configure(fg_color=bg, text_color=fg)
            btn_temperature.configure(fg_color=bg, text_color=fg)
            btn_longueur.configure(fg_color=bg, text_color=fg)
            btn_vitesse.configure(fg_color=bg, text_color=fg)
            btn_temps.configure(fg_color=bg, text_color=fg)
            btn_informatique.configure(fg_color=bg, text_color=fg)
    
    elif frm_principal.cget("fg_color") == "black":   
            btn_surface.configure(fg_color=blue, text_color=bg)
            btn_masse.configure(fg_color=fg, text_color=bg)
            btn_volume.configure(fg_color=fg, text_color=bg)
            btn_temperature.configure(fg_color=fg, text_color=bg)
            btn_longueur.configure(fg_color=fg, text_color=bg)
            btn_vitesse.configure(fg_color=fg, text_color=bg)
            btn_temps.configure(fg_color=fg, text_color=bg)
            btn_informatique.configure(fg_color=fg, text_color=bg)

    

def fonction_vitesse():
    bouton_conversion.configure(command=convertir_vitesse)

    combobox_de.configure(values=["Kilomètre par heure (km/h)", "Mètre par seconde (m/s)", "Mile par heure (mph)", "Noeud (kn)"])
    combobox_vers.configure(values=["Kilomètre par heure (km/h)", "Mètre par seconde (m/s)", "Mile par heure (mph)", "Noeud (kn)"]) 
    
    racc_vitesse()

    if frm_principal.cget("fg_color") == "white":
    
            btn_vitesse.configure(fg_color=blue, text_color=bg)
            btn_masse.configure(fg_color=bg, text_color=fg)
            btn_volume.configure(fg_color=bg, text_color=fg)
            btn_temperature.configure(fg_color=bg, text_color=fg)
            btn_surface.configure(fg_color=bg, text_color=fg)
            btn_longueur.configure(fg_color=bg, text_color=fg)
            btn_temps.configure(fg_color=bg, text_color=fg)
            btn_informatique.configure(fg_color=bg, text_color=fg)
    
    elif frm_principal.cget("fg_color") == "black":   
            btn_vitesse.configure(fg_color=blue, text_color=bg)
            btn_masse.configure(fg_color=fg, text_color=bg)
            btn_volume.configure(fg_color=fg, text_color=bg)
            btn_temperature.configure(fg_color=fg, text_color=bg)
            btn_surface.configure(fg_color=fg, text_color=bg)
            btn_longueur.configure(fg_color=fg, text_color=bg)
            btn_temps.configure(fg_color=fg, text_color=bg)
            btn_informatique.configure(fg_color=fg, text_color=bg)

                

def fonction_temps():
    bouton_conversion.configure(command=convertir_temps)

    combobox_de.configure(values=["Année (a)", "Mois (m)", "Semaine (sem)", "Jours (j)", "Heures (h)", "Minute (min)", "Seconde (sec)"])
    combobox_vers.configure(values=["Année (a)", "Mois (m)", "Semaine (sem)", "Jours (j)", "Heures (h)", "Minute (min)", "Seconde (sec)"]) 

    if frm_principal.cget("fg_color") == "white":
    
            btn_temps.configure(fg_color=blue, text_color=bg)
            btn_masse.configure(fg_color=bg, text_color=fg)
            btn_volume.configure(fg_color=bg, text_color=fg)
            btn_temperature.configure(fg_color=bg, text_color=fg)
            btn_surface.configure(fg_color=bg, text_color=fg)
            btn_vitesse.configure(fg_color=bg, text_color=fg)
            btn_longueur.configure(fg_color=bg, text_color=fg)
            btn_informatique.configure(fg_color=bg, text_color=fg)
    
    elif frm_principal.cget("fg_color") == "black":   
            btn_temps.configure(fg_color=blue, text_color=bg)
            btn_masse.configure(fg_color=fg, text_color=bg)
            btn_volume.configure(fg_color=fg, text_color=bg)
            btn_temperature.configure(fg_color=fg, text_color=bg)
            btn_surface.configure(fg_color=fg, text_color=bg)
            btn_vitesse.configure(fg_color=fg, text_color=bg)
            btn_longueur.configure(fg_color=fg, text_color=bg)
            btn_informatique.configure(fg_color=fg, text_color=bg)

    
def fonction_donnee():
    bouton_conversion.configure(command=convertir_donnee)

    combobox_de.configure(values=["Pétaoctet (PO)", "Téraoctet (TO)", "Gigaoctet (GO)", "Mégaoctet (MO)", "Kilooctet (KO)", "Octet (O)", "Bit"])
    combobox_vers.configure(values=["Pétaoctet (PO)", "Téraoctet (TO)", "Gigaoctet (GO)", "Mégaoctet (MO)", "Kilooctet (KO)", "Octet (O)", "Bit"]) 

    if frm_principal.cget("fg_color") == "white":
    
            btn_informatique.configure(fg_color=blue, text_color=bg)
            btn_masse.configure(fg_color=bg, text_color=fg)
            btn_volume.configure(fg_color=bg, text_color=fg)
            btn_temperature.configure(fg_color=bg, text_color=fg)
            btn_surface.configure(fg_color=bg, text_color=fg)
            btn_vitesse.configure(fg_color=bg, text_color=fg)
            btn_temps.configure(fg_color=bg, text_color=fg)
            btn_longueur.configure(fg_color=bg, text_color=fg)
    
    elif frm_principal.cget("fg_color") == "black":   
            btn_informatique.configure(fg_color=blue, text_color=bg)
            btn_masse.configure(fg_color=fg, text_color=bg)
            btn_volume.configure(fg_color=fg, text_color=bg)
            btn_temperature.configure(fg_color=fg, text_color=bg)
            btn_surface.configure(fg_color=fg, text_color=bg)
            btn_vitesse.configure(fg_color=fg, text_color=bg)
            btn_temps.configure(fg_color=fg, text_color=bg)
            btn_longueur.configure(fg_color=fg, text_color=bg)

    
# Fonctions convertir                         

def convertir_longueur():
    error_verification()
    valeur = float(entree_de.get())
    depart = combobox_de.get()
    arrivee = combobox_vers.get()
    print(f"La valeure entree est: {valeur}")
    print(f"Unité de départ: {depart}")
    print(f"L'unité d'arrivée: {arrivee}")
    match depart:
        case "Mètre (m)":
            u1 = "m"
        case "Kilomètre (km)":
            u1 = "km"
        case "Centimètre (cm)":
            u1 = "cm"
        case "Milimètre (mm)":
            u1 = "mm"
        case "Héctomètre (hm)":
            u1 = "hm"
        case "Décamètre (dam)":
            u1 = "dam" 
        case "Décimètre (dm)":
            u1 = "dm" 
        case "Pouces (in)":
            u1 = "pouces" 
        case "Pieds (ft)":
            u1 = "pieds"
        case "Yards (yd)":
            u1 = "yards" 
        case "Miles (mi)":
            u1 = "miles"                                 
    match arrivee:
            case "Mètre (m)":
                u2 = "m"
            case "Kilomètre (km)":
                u2 = "km"
            case "Centimètre (cm)":
                u2 = "cm"
            case "Milimètre (mm)":
                u2 = "mm"
            case "Héctomètre (hm)":
                u2 = "hm"
            case "Décamètre (dam)":
                u2 = "dam" 
            case "Décimètre (dm)":
                u2 = "dm" 
            case "Pouces (in)":
                u2 = "pouces" 
            case "Pieds (ft)":
                u2 = "pieds"
            case "Yards (yd)":
                u2 = "yards" 
            case "Miles (mi)":
                u2 = "miles"              
    resultat = longeurs_distances(u1, u2, valeur)
    entree_vers.set(resultat)

def convertir_masse():
    error_verification()
    valeur = float(entree_de.get())
    depart = combobox_de.get()
    arrivee = combobox_vers.get()
    print(f"La valeure entree est: {valeur}")
    print(f"Unité de départ: {depart}")
    print(f"L'unité d'arrivée: {arrivee}")
    match depart:
        case "Tonne (t)":
            u1 = "t"
        case "Quintal (q)":
            u1 = "q"
        case "Dizaine de kilogramme (dkg)":
            u1 = "dkg"
        case "Kilogramme (kg)":
            u1 = "kg"
        case "Héctogramme (hg)":
            u1 = "hg"
        case "Décagramme (dag)":
            u1 = "dag" 
        case "Gramme (g)":
            u1 = "g"
        case "Décigramme (dg)":
            u1 = "dg"
        case "Centigramme (cg)":
            u1 = "cg"
        case "Milligramme (mg)":
            u1 = "mg"
        case "Once (oz)":
            u1 = "onces"
        case "Livre (lb)":
            u1 = "livres"
                               
    match arrivee:
        case "Tonne (t)":
            u2 = "t"
        case "Quintal (q)":
            u2 = "q"
        case "Dizaine de kilogramme (dkg)":
            u2 = "dkg"
        case "Kilogramme (kg)":
            u2 = "kg"
        case "Héctogramme (hg)":
            u2 = "hg"
        case "Décagramme (dag)":
            u2 = "dag" 
        case "Gramme (g)":
            u2 = "g"
        case "Décigramme (dg)":
            u2 = "dg"
        case "Centigramme (cg)":
            u2 = "cg"
        case "Milligramme (mg)":
            u2 = "mg"
        case "Once (oz)":
            u2 = "onces"
        case "Livre (lb)":
            u2 = "livres"            
    resultat = poids_masses(u1, u2, valeur)
    entree_vers.set(resultat)

def convertir_volume():
    error_verification()
    valeur = float(entree_de.get())
    depart = combobox_de.get()
    arrivee = combobox_vers.get()
    print(f"La valeure entree est: {valeur}")
    print(f"Unité de départ: {depart}")
    print(f"L'unité d'arrivée: {arrivee}")
    match depart:
        case "Kilolitre (kl)":
            u1 = "kl"
        case "Héctolitre (hl)":
            u1 = "hl"
        case "Décalitre (dal)":
            u1 = "dal"
        case "Litre (l)":
            u1 = "l"
        case "Décilitre (dl)":
            u1 = "dl"
        case "Centilitre (cl)":
            u1 = "cl" 
        case "Millilitre (ml)":
            u1 = "ml"
        case "Mètre cube (m3)":
            u1 = "m3"
        case "Décimètre cube (dm3)":
            u1 = "dm3"
        case "Centimètre cube (cm3)":
            u1 = "cm3"
        case "Millimètre cube (mm3)":
            u1 = "mm3"    
        case "Onces (oz)":
            u1 = "onces"
        case "Tasses":
            u1 = "tasses"
        case "Gallons":
            u1 ="gallons"
        case "Pintes":
            u1 = "pintes"                    
    match arrivee:
            case "Kilolitre (kl)":
                u2 = "kl"
            case "Héctomètre (hm)":
                u2= "hl"
            case "Décalitre (dal)":
                u2 = "dal"
            case "Litre (l)":
                u2 = "l"
            case "Décilitre (dl)":
                u2 = "dl"
            case "Centilitre (cl)":
                u2 = "cl" 
            case "Millilitre (ml)":
                u2 = "ml"
            case "Mètre cube (m3)":
                u2 = "m3"
            case "Décimètre cube (dm3)":
                u2 = "dm3"
            case "Centimètre cube (cm3)":
                u2 = "cm3"
            case "Millimètre cube (mm3)":
                u2 = "mm3"    
            case "Onces (oz)":
                u2 = "onces"
            case "Tasses":
                u2 = "tasses"
            case "Gallons":
                u2 ="gallons"
            case "Pintes":
                u2 = "pintes"              
    resultat = volumes_capacites(u1, u2, valeur)
    entree_vers.set(resultat)

def convertir_temperature():
    error_verification()
    valeur = float(entree_de.get())
    depart = combobox_de.get()
    arrivee = combobox_vers.get()
    print(f"La valeure entree est: {valeur}")
    print(f"Unité de départ: {depart}")
    print(f"L'unité d'arrivée: {arrivee}")
    match depart:
        case "Kelvin (°K)":
            u1 = "K"
        case "Celcius (°C)":
            u1 = "C"
        case "Fahrenheit (°F)":
            u1 = "F"
                            
    match arrivee:
        case "Kelvin (°K)":
            u2 = "K"
        case "Celcius (°C)":
            u2 = "C"
        case "Fahrenheit (°F)":
            u2 = "F"    
                          
    resultat = temperatures(u1, u2, valeur)
    entree_vers.set(resultat)

def convertir_surface():
    error_verification()
    valeur = float(entree_de.get())
    depart = combobox_de.get()
    arrivee = combobox_vers.get()
    print(f"La valeure entree est: {valeur}")
    print(f"Unité de départ: {depart}")
    print(f"L'unité d'arrivée: {arrivee}")
    match depart:
        case "Kilomètre carré (km2)":
            u1 = "km2"
        case "Héctare (ha)":
            u1 = "ha"
        case "Aire (a)":
            u1 = "a"
        case "Mètre carré (m2)":
            u1 = "m2"
        case "Décimètre carré (dm2)":
            u1 = "dm2"
        case "Centimètre carré (cm2)":
            u1 = "cm2" 
        case "Millimètre carré (mm2)":
            u1 = "mm2" 
    match arrivee:
        case "Kilomètre carré (km2)":
            u2 = "km2"
        case "Héctare (ha)":
            u2 = "ha"
        case "Aire (a)":
            u2 = "a"
        case "Mètre carré (m2)":
            u2 = "m2"
        case "Décimètre carré (dm2)":
            u2 = "dm2"
        case "Centimètre carré (cm2)":
            u2 = "cm2" 
        case "Millimètre carré (mm2)":
            u2 = "mm2"                                         
    resultat = surfaces(u1, u2, valeur)
    entree_vers.set(resultat)

def convertir_vitesse():
    error_verification()
    valeur = float(entree_de.get())
    depart = combobox_de.get()
    arrivee = combobox_vers.get()
    print(f"La valeure entree est: {valeur}")
    print(f"Unité de départ: {depart}")
    print(f"L'unité d'arrivée: {arrivee}")
    match depart:
        case "Kilomètre par heure (km/h)":
            u1 = "km_h"
        case "Mètre par seconde (m/s)":
            u1 = "m_s"
        case "Mile par heure (mph)":
            u1 = "mph"
        case "Noeud (kn)":
            u1 = "noeuds"

    match arrivee:
        case "Kilomètre par heure (km/h)":
            u2 = "km_h"
        case "Mètre par seconde (m/s)":
            u2 = "m_s"
        case "Mile par heure (mph)":
            u2 = "mph"
        case "Noeud (kn)":
            u2 = "noeuds"        
                 
    resultat = vitesses(u1, u2, valeur)
    entree_vers.set(resultat)

def convertir_temps():
    error_verification()
    valeur = float(entree_de.get())
    depart = combobox_de.get()
    arrivee = combobox_vers.get()
    print(f"La valeure entree est: {valeur}")
    print(f"Unité de départ: {depart}")
    print(f"L'unité d'arrivée: {arrivee}")
    match depart:
        case "Année (a)":
            u1 = "annee"
        case "Mois (m)":
            u1 = "mois"
        case "Semaine (sem)":
            u1 = "sem"
        case "Jours (j)":
            u1 = "jours"
        case "Heures (h)":
            u1 = "heures"
        case "Minute (min)":
            u1 = "min" 
        case "Seconde (sec)":
            u1 = "sec"   

    match arrivee:
        case "Année (a)":
            u2 = "annee"
        case "Mois (m)":
            u2 = "mois"
        case "Semaine (sem)":
            u2 = "sem"
        case "Jours (j)":
            u2 = "jours"
        case "Heures (h)":
            u2 = "heures"
        case "Minute (min)":
            u2 = "min" 
        case "Seconde (sec)":
            u2 = "sec"                         
                  
    resultat = temps(u1, u2, valeur)
    entree_vers.set(resultat)

def convertir_donnee():
    error_verification()
    valeur = float(entree_de.get())
    depart = combobox_de.get()
    arrivee = combobox_vers.get()
    print(f"La valeure entree est: {valeur}")
    print(f"Unité de départ: {depart}")
    print(f"L'unité d'arrivée: {arrivee}")
    match depart:
        case "Pétaoctet (PO)":
            u1 = "po"
        case "Téraoctet (TO)":
            u1 = "to"
        case "Gigaoctet (GO)":
            u1 = "go"
        case "Mégaoctet (MO)":
            u1 = "mo"
        case "Kilooctet (KO)":
            u1 = "ko"
        case "Octet (O)":
            u1 = "o" 
        case "Bit":
            u1 = "bit" 

    match arrivee:
        case "Pétaoctet (PO)":
            u2 = "po"
        case "Téraoctet (TO)":
            u2 = "to"
        case "Gigaoctet (GO)":
            u2 = "go"
        case "Mégaoctet (MO)":
            u2 = "mo"
        case "Kilooctet (KO)":
            u2 = "ko"
        case "Octet (O)":
            u2 = "o" 
        case "Bit":
            u2 = "bit"                           
               
    resultat = donnees(u1, u2, valeur)
    entree_vers.set(resultat)                            

  
# Création des fonctions pour conversion rapides
# Pour la longueur et distance
def pouce_en_cm():
    racc_error_verification()
    valeur = float(entree_de.get())
    resultat = longeurs_distances("pouces", "cm", valeur)
    entree_vers.set(resultat)

def cm_en_pouce():
    racc_error_verification()
    valeur = float(entree_de.get())
    resultat = longeurs_distances("cm", "pouces", valeur)
    entree_vers.set(resultat)

def pied_en_cm():
    racc_error_verification()
    valeur = float(entree_de.get())
    resultat = longeurs_distances("pieds", "cm", valeur)
    entree_vers.set(resultat)

def cm_en_pied():
    racc_error_verification()
    valeur = float(entree_de.get())
    resultat = longeurs_distances("cm", "pieds", valeur)
    entree_vers.set(resultat)
 
def once_en_g():
    racc_error_verification()
    valeur = float(entree_de.get())
    resultat = poids_masses("onces", "g", valeur)
    entree_vers.set(resultat)

def g_en_once():
    racc_error_verification()
    valeur = float(entree_de.get())
    resultat = poids_masses("g", "onces", valeur)
    entree_vers.set(resultat)

def kg_en_livre():
    racc_error_verification()
    valeur = float(entree_de.get())
    resultat = poids_masses("kg", "livres", valeur)
    entree_vers.set(resultat)

def livre_en_kg():
    racc_error_verification()
    valeur = float(entree_de.get())
    resultat = poids_masses("livres", "kg", valeur)
    entree_vers.set(resultat)

def ml_en_tasse():
    racc_error_verification()
    valeur = float(entree_de.get())
    resultat = volumes_capacites("ml", "tasses", valeur)
    entree_vers.set(resultat)

def tasse_en_ml():
    racc_error_verification()
    valeur = float(entree_de.get())
    resultat = volumes_capacites("tasses", "ml", valeur)
    entree_vers.set(resultat)    

def l_en_gallon():
    racc_error_verification()
    valeur = float(entree_de.get())
    resultat = volumes_capacites("l", "gallons", valeur)
    entree_vers.set(resultat)

def gallon_en_l():
    racc_error_verification()
    valeur = float(entree_de.get())
    resultat = volumes_capacites("gallons", "l", valeur)
    entree_vers.set(resultat) 

def C_en_F():
    racc_error_verification()
    valeur = float(entree_de.get())
    resultat = F_C("C", "F", valeur)
    entree_vers.set(resultat)

def F_en_C():
    racc_error_verification()
    valeur = float(entree_de.get())
    resultat = F_C("F", "C", valeur)
    entree_vers.set(resultat)

def ha_en_m2():
    racc_error_verification()
    valeur = float(entree_de.get())
    resultat = surfaces("ha", "m2", valeur)
    entree_vers.set(resultat) 

def m2_en_ha():
    racc_error_verification()
    valeur = float(entree_de.get())
    resultat = surfaces("m2", "ha", valeur)
    entree_vers.set(resultat)  

def kmh_en_ms():
    racc_error_verification()
    valeur = float(entree_de.get())
    resultat = vitesses("km_h", "m_s", valeur)
    entree_vers.set(resultat)

def ms_en_kmh():
    racc_error_verification()
    valeur = float(entree_de.get())
    resultat = vitesses("m_s", "km_h", valeur)
    entree_vers.set(resultat)             


       

# Fonction d' execution
def racc_longueur():
    frm_conv_rapide.grid_columnconfigure(0, weight=1) 
    frm_conv_rapide.grid_columnconfigure(1, weight=1)
    frm_conv_rapide.grid_rowconfigure(0, weight=1)
    frm_conv_rapide.grid_rowconfigure(1, weight=1)

    btn_pouce_en_cm = ctk.CTkButton(frm_conv_rapide,
                                    text="Pouce en cm",
                                    command=pouce_en_cm)
    btn_pouce_en_cm.grid(
        column=0,
        row=0
    ) 

    btn_cm_en_pouce = ctk.CTkButton(frm_conv_rapide,
                                        text="cm en pouce",
                                        command=cm_en_pouce)
    btn_cm_en_pouce.grid(
            column=1,
            row=0
        )  

    btn_pied_en_cm = ctk.CTkButton(frm_conv_rapide,
                                        text="Pied en cm",
                                        command=pied_en_cm)
    btn_pied_en_cm.grid(
            column=0,
            row=1
        )                      
    btn_cm_en_pied = ctk.CTkButton(frm_conv_rapide,
                                        text="cm en pied",
                                        command=cm_en_pied)
    btn_cm_en_pied.grid(
            column=1,
            row=1
        )


def racc_masse():
    frm_conv_rapide.grid_columnconfigure(0, weight=1) 
    frm_conv_rapide.grid_columnconfigure(1, weight=1)
    frm_conv_rapide.grid_rowconfigure(0, weight=1)
    frm_conv_rapide.grid_rowconfigure(1, weight=1)

    btn_once_en_g = ctk.CTkButton(frm_conv_rapide,
                                        text="Once en g",
                                        command=once_en_g)
    btn_once_en_g.grid(
            column=0,
            row=0
        )

    btn_g_en_once = ctk.CTkButton(frm_conv_rapide,
                                        text="g en once",
                                        command=g_en_once)
    btn_g_en_once.grid(
            column=1,
            row=0
        )

    btn_kg_en_livre = ctk.CTkButton(frm_conv_rapide,
                                        text="Kg en livre",
                                        command=kg_en_livre)
    btn_kg_en_livre.grid(
            column=0,
            row=1
        )    

    btn_livre_en_kg = ctk.CTkButton(frm_conv_rapide,
                                        text="Pouce en cm",
                                        command=pouce_en_cm)
    btn_livre_en_kg.grid(
            column=1,
            row=1
        ) 

def racc_volume():
    frm_conv_rapide.grid_columnconfigure(0, weight=1) 
    frm_conv_rapide.grid_columnconfigure(1, weight=1)
    frm_conv_rapide.grid_rowconfigure(0, weight=1)
    frm_conv_rapide.grid_rowconfigure(1, weight=1)

    btn_tasse_en_ml = ctk.CTkButton(frm_conv_rapide,
                                            text="Tasse en ml",
                                            command=tasse_en_ml)
    btn_tasse_en_ml.grid(
            column=0,
            row=0
            )

    btn_ml_en_tasse = ctk.CTkButton(frm_conv_rapide,
                                            text="ml en tasse",
                                            command=ml_en_tasse)
    btn_ml_en_tasse.grid(
                column=1,
                row=0
            )

    btn_l_en_gallon = ctk.CTkButton(frm_conv_rapide,
                                            text="Litre en gallon",
                                            command=l_en_gallon)
    btn_l_en_gallon.grid(
                column=0,
                row=1
            )

    btn_gallon_en_l = ctk.CTkButton(frm_conv_rapide,
                                            text="Gallon en litre",
                                            command=gallon_en_l)
    btn_gallon_en_l.grid(
                column=1,
                row=1
            )
    

def racc_temperature():
    frm_conv_rapide.grid_columnconfigure(0, weight=1) 
    frm_conv_rapide.grid_columnconfigure(1, weight=1)
    frm_conv_rapide.grid_rowconfigure(0, weight=1)

    btn_F_en_C = ctk.CTkButton(frm_conv_rapide,
                                                text="Fahrenheit en Celcius",
                                                command=F_en_C)
    btn_F_en_C.grid(
                    column=0,
                    row=0
                )
    btn_C_en_F = ctk.CTkButton(frm_conv_rapide,
                                                text="Celcius en Fahrenheit",
                                                command=C_en_F)
    btn_C_en_F.grid(
                    column=1,
                    row=0
                )

def racc_surface():
    frm_conv_rapide.grid_columnconfigure(0, weight=1) 
    frm_conv_rapide.grid_columnconfigure(1, weight=1)
    frm_conv_rapide.grid_rowconfigure(0, weight=1)

    btn_ha_en_m2 = ctk.CTkButton(frm_conv_rapide,
                                                    text="ha en m2",
                                                    command=ha_en_m2)
    btn_ha_en_m2.grid(
                        column=0,
                        row=0
                    )
    btn_m2_en_ha = ctk.CTkButton(frm_conv_rapide,
                                                    text="m2 en ha",
                                                    command=m2_en_ha)
    btn_m2_en_ha.grid(
                        column=0,
                        row=0
                    )

def racc_vitesse():
    frm_conv_rapide.grid_columnconfigure(0, weight=1) 
    frm_conv_rapide.grid_columnconfigure(1, weight=1)
    frm_conv_rapide.grid_rowconfigure(0, weight=1)

    btn_kmh_en_ms = ctk.CTkButton(frm_conv_rapide,
                                                        text="km/h en m/s",
                                                        command=kmh_en_ms)
    btn_kmh_en_ms.grid(
                            column=0,
                            row=0
                        )
    btn_ms_en_kmh = ctk.CTkButton(frm_conv_rapide,
                                                        text="m/s en km/h",
                                                        command=ms_en_kmh)
    btn_ms_en_kmh.grid(
                            column=1,
                            row=0
                        )


# Création de la fenetre
fenetre = ctk.CTk()
fenetre.title("Convertisseur d'unités")


# Les varibales
bg = "white"
fg = "black"
blue = "#2563EB"
grey = "#A0A0A0"


# Centrage et taille initiale de la fenêtre
largeur_fenetre = 800
hauteur_fenetre = 600

largeur_ecran = fenetre.winfo_screenwidth()
hauteur_ecran = fenetre.winfo_screenheight()

position_fenetre_largeur = (largeur_ecran // 2) - (largeur_fenetre // 2)
position_fenetre_hauteur = (hauteur_ecran // 2) - (hauteur_fenetre // 2)

fenetre.geometry(f"{largeur_fenetre}x{hauteur_fenetre}+{position_fenetre_largeur}+{position_fenetre_hauteur}")
fenetre.configure(fg_color=bg)
fenetre.minsize(width=600, height=400)
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
    fg_color=bg
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
label_titre.configure(font=("Aria", 40, "bold"), 
                      text_color=fg
                      )
label_titre.grid(
    column=0,
    row=0,
    sticky="ew"
)


label_titre_info = ctk.CTkLabel(frm_titre, 
                                text="Transforme mesure entre différents systèmes (métrique, impérial, ect...)"
                                )
label_titre_info.configure(font=("Aria", 18), 
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
                   ipadx= 3,
                   column=0,
                   row=1)

#Configuration de Frame principal
frm_principal.grid_columnconfigure(0, weight=1) # Diviser en quatres colonnes le collones 0 a une seule part
frm_principal.grid_columnconfigure(1, weight=6) # Le colonnes 1 a trois parts
frm_principal.grid_rowconfigure(0, weight=1)

#Frame des options
frm_option = ctk.CTkFrame(frm_principal, 
                          fg_color=bg, 
                          border_color=fg, 
                          border_width=2)
frm_option.grid(column=0, 
                row=0, 
                padx=1,
                ipadx=50, 
                sticky = "nsew") # "nsew" permet e proncdre rour epave

# Configuration des grid de frm_option
frm_option.grid_columnconfigure(0, weight=1)
frm_option.grid_rowconfigure(0, weight=1)
frm_option.grid_rowconfigure(1, weight=1)
frm_option.grid_rowconfigure(2, weight=1)
frm_option.grid_rowconfigure(3, weight=1)
frm_option.grid_rowconfigure(4, weight=1)
frm_option.grid_rowconfigure(5, weight=1)
frm_option.grid_rowconfigure(6, weight=1)
frm_option.grid_rowconfigure(7, weight=1)
frm_option.grid_rowconfigure(8, weight=4) # Pour les paramètres

# Frame des onglets
btn_longueur = ctk.CTkButton(frm_option, 
                             text="Longueur",  
                             fg_color=bg, 
                             text_color=fg,
                             hover_color= blue,
                             command=fonction_longueur,
                             font=("Aria", 15, "bold")
                             )
btn_longueur.grid(
    column=0,
    row=0,
    sticky="nsew"
)

btn_masse = ctk.CTkButton(frm_option, 

                          text="Masse", 
                          fg_color=bg, 
                          text_color=fg,
                          hover_color= blue,
                          command=fonction_masse,
                          font=("Aria", 15, "bold")
                          )
btn_masse.grid(
    column=0,
    row=1,
    sticky="nsew"
)

btn_volume = ctk.CTkButton(frm_option, 
                           text="Volume", 
                           fg_color=bg, 
                           text_color=fg,
                           hover_color= blue,
                           command=fonction_volume,
                           font=("Aria", 15, "bold")
                           )
btn_volume.grid(
    column=0,
    row=2,
    sticky="nsew"
)

btn_temperature = ctk.CTkButton(frm_option, 
                                text="Température", 
                                fg_color=bg, 
                                text_color=fg,
                                hover_color= blue,
                                command=fonction_temperature,
                                font=("Aria", 15, "bold")
                                )
btn_temperature.grid(
    column=0,
    row=3,
    sticky="nsew"
)

btn_surface = ctk.CTkButton(frm_option, 
                            text="Surface", 
                            fg_color=bg, 
                            text_color=fg,
                            hover_color= blue,
                            command=fonction_surface,
                            font=("Aria", 15, "bold")
                            )
btn_surface.grid(
    column= 0,
    row=4,
    sticky="nsew"
)

btn_vitesse = ctk.CTkButton(frm_option, 
                            text="Vitesse", 
                            fg_color=bg, 
                            text_color=fg,
                            hover_color= blue,
                            command=fonction_vitesse,
                            font=("Aria", 15, "bold")
                            )
btn_vitesse.grid(
    column=0,
    row=5,
    sticky="nsew"
)

btn_temps = ctk.CTkButton(frm_option, 
                          text="Temps", 
                          fg_color=bg, 
                          text_color=fg,
                          hover_color=blue,
                          command=fonction_temps,
                          font=("Aria", 15, "bold")
                          )
btn_temps.grid(
    column=0,
    row=6,
    sticky="nsew"
)

btn_informatique = ctk.CTkButton(frm_option, 
                                 text="Données", 
                                 fg_color=bg, 
                                 text_color=fg,
                                 hover_color= blue,
                                 command=fonction_donnee,
                                 font=("Aria", 15, "bold")
                                 )
btn_informatique.grid(
    column=0,
    row=7,
    sticky="nsew"
)

frm_parametre = ctk.CTkFrame(frm_option, 
                             fg_color=bg)
frm_parametre.grid(
    column=0,
    row=8,
    sticky="nsew",
)

# Configuration des grid de frm_parametre
frm_parametre.grid_columnconfigure(0, weight=1)
frm_parametre.grid_columnconfigure(1, weight=1)
frm_parametre.grid_rowconfigure(0, weight=1)


# Dans les parametres
btn_clair = ctk.CTkButton(frm_parametre, 
                          text="Clair",
                          fg_color=bg, 
                          text_color=fg,
                          hover_color= blue,
                          width=90,
                          font=("Aria", 15, "bold"),
                          command=light_mode
                          )
btn_clair.grid(
    column=0,
    row=0,
    ipadx=0,
    ipady=8,
    padx=1
)

btn_sombre = ctk.CTkButton(frm_parametre, 
                          text="Sombre",
                          fg_color=bg, 
                          text_color=fg,
                          hover_color= blue,
                          width=90,
                          font=("Aria", 15, "bold"),
                          command=night_mode
                          )
btn_sombre.grid(
    column=1,
    row=0,
    ipadx=0,
    ipady=8,
    padx=1
)





# Frame de la converion principale
frm_conv_principal = ctk.CTkFrame(frm_principal, 
                                  fg_color=bg
                                  )
frm_conv_principal.grid(column=1, 
                        row=0, 
                        padx=2, 
                        sticky = "nsew")

# Configuration des grids de frm_conv_principal
frm_conv_principal.grid_columnconfigure(0, weight=1)
frm_conv_principal.grid_rowconfigure(0, weight=4)
frm_conv_principal.grid_rowconfigure(1, weight=1)


# La table de conversion
frm_table_conv = ctk.CTkFrame(frm_conv_principal, 
                              fg_color=bg,
                              border_color=grey,
                              border_width=2
                              )
frm_table_conv.grid(column=0,
                    row=0,
                    sticky="nsew")

# Configuration des grids de frm_table_conv
frm_table_conv.grid_columnconfigure(0, weight=1)
frm_table_conv.grid_rowconfigure(0, weight=2)
frm_table_conv.grid_rowconfigure(1, weight=1)

# frm de conversion 
frm_conversion = ctk.CTkFrame(frm_table_conv, 
                              fg_color=bg,
                              )
frm_conversion.grid(
    column=0,
    row=0,
    ipadx=10,
    ipady=10,
    padx=10,
    pady=10,
    sticky="nsew"
)
# Configuration des grids de frm_conversion
frm_conversion.grid_columnconfigure(0, weight=4)
frm_conversion.grid_columnconfigure(1, weight=1)
frm_conversion.grid_columnconfigure(2, weight=4)
frm_conversion.grid_rowconfigure(0, weight=1)


#frm d'entree
frm_de = ctk.CTkFrame(frm_conversion,
                      fg_color=bg)
frm_de.grid(
    column=0,
    row=0,
    ipadx=2,
    padx=6
    #sticky="nsew"
)

# Configuration des grids de frm_de
frm_de.grid_columnconfigure(0, weight=1)
frm_de.grid_rowconfigure(0, weight=1)
frm_de.grid_rowconfigure(1, weight=1)
frm_de.grid_rowconfigure(2, weight=1)

# Label de frm_de
label_de = ctk.CTkLabel(frm_de,
                        text_color=fg,
                        fg_color=bg,
                        text="De",
                        font=("Aria", 15, "bold")
                        )
label_de.grid(
    column=0,
    row=0,
    ipadx=10,
    pady=3)

# Conbobox de frm_de
combobox_de = ctk.CTkComboBox(frm_de,
                              values=[],
                              fg_color=bg,
                              text_color=fg,
                              border_color=grey,
                              width=460,
                              height=80,
                              dropdown_fg_color=bg,
                              dropdown_text_color=fg,
                              state="readonly",
                              dropdown_hover_color=blue,
                              font=("Aria", 20, "bold"),
                              dropdown_font=("Aria", 15, "bold")
                              )
combobox_de.grid(
    column=0,
    row=1,
    # ipadx=60,
    # ipady=20,
    pady=3
)

# Entree de frm_de
entree_de = ctk.CTkEntry(frm_de,
                         fg_color=bg,
                         text_color=fg,
                         border_color=grey,
                         placeholder_text="Valeur 1",
                         width=460,
                         height=80,
                         font=("Aria", 20, "bold")
                         )
entree_de.grid(
    column=0,
    row=2,
    # ipadx=60,
    # ipady=20,
    pady=(6,0)
)

#frm de sortie
frm_vers = ctk.CTkFrame(frm_conversion,
                        fg_color=bg
                        )
frm_vers.grid(
    column=2,
    row=0,
    ipadx=2,
    padx=6
    #sticky="nsew"
)

# Configuration des grids de frm_vers
frm_vers.grid_columnconfigure(0, weight=1)
frm_vers.grid_rowconfigure(0, weight=1)
frm_vers.grid_rowconfigure(1, weight=1)
frm_vers.grid_rowconfigure(2, weight=1)

# Label de frm_de
label_vers = ctk.CTkLabel(frm_vers,
                        text_color=fg,
                        fg_color=bg,
                        text="Vers",
                        font=("Aria", 15, "bold")
                        )
label_vers.grid(
    column=0,
    row=0,
    ipadx=10,
    pady=3)

# Conbobox de frm_de
combobox_vers = ctk.CTkComboBox(frm_vers,
                              values=[],  
                              fg_color=bg,
                              text_color=fg,
                              border_color=grey,
                              width=460,
                              height=80,
                              dropdown_fg_color=bg,
                              dropdown_text_color=fg,
                              state="readonly",
                              dropdown_hover_color=blue,
                              font=("Aria", 20, "bold"),
                              dropdown_font=("Aria", 15, "bold")
                              )
combobox_vers.grid(
    column=0,
    row=1,
    # ipadx=60,
    # ipady=20,
    pady=3
)

# Entree de frm_de
entree_vers = ctk.CTkEntry(frm_vers,
                           fg_color=bg,
                           text_color=fg,
                           border_color=grey,
                           placeholder_text="Valeur 2",
                           width=460,
                           height=80,
                           font=("Aria", 20, "bold")
                           )
entree_vers.grid(
    column=0,
    row=2,
    # ipadx=60,
    # ipady=20,
    pady=(6,0)
)

# Bouton de conversion
bouton_conversion = ctk.CTkButton(frm_table_conv,
                                  text="Convertir",
                                  fg_color=blue,
                                  text_color=fg,
                                  command=error_message,
                                  hover_color="#0A0",
                                  font=("Aria", 20, "bold")
                                  )
bouton_conversion.grid(
    column=0,
    row=1,
    ipadx=10,
    ipady=10,
    sticky="ew",
    padx=20,
    pady=(0,12)
)

# frm conversion rapide
frm_conv_rapide = ctk.CTkFrame(frm_conv_principal,
                               fg_color=bg,
                               border_color=grey,
                               border_width=2)
frm_conv_rapide.grid(
    column=0,
    row=1,
    sticky='nsew',
    pady=(4,0)
)




fenetre.mainloop()