# Les fonctions de backend utilisés dans l'appli de converisseur d 'unités

# LONGUEUR ET DISTANCES
# Fonction de raccourcissement
# De l'unité u1 vers l'unité u2 avec la valeur d'entrée valeur

#Pour l'un des unités appartien à [km, hm, dam, m, dm, cm, mm] ou que les deux unités sont égaux
def conv_volume(u1, u2, valeur):
    listes = ["kl", "hl", "dal", "l", "dl", "cl", "ml"]
    puiss = listes.index(u2) - listes.index(u1)
    reponse = valeur * (10**puiss)
    return reponse
#Test
#print(conv_long("cm", "cm", 20))

#Cube conversion
def m3(u1, u2, valeur):
    listes = ["kl", "hl", "dal", "l", "dl", "cl", "ml"]
    if u1 == "m3" and u2 == "m3":
        return valeur
    elif u1 == "m3" and u2 in listes:
        return conv_volume("kl", u2, valeur)
    elif u1 in listes and u2 == "m3":
        return conv_volume(u1, "kl", valeur)

def dm3(u1, u2, valeur):
    listes = ["kl", "hl", "dal", "l", "dl", "cl", "ml"]
    if u1 == "dm3" and u2 == "dm3":
        return valeur
    elif u1 == "dm3" and u2 in listes:
        return conv_volume("l", u2, valeur)
    elif u1 in listes and u2 == "dm3":
        return conv_volume(u1, "l", valeur)    

def cm3(u1, u2, valeur):
    listes = ["kl", "hl", "dal", "l", "dl", "cl", "ml"]
    if u1 == "cm3" and u2 == "cm3":
        return valeur
    elif u1 == "cm3" and u2 in listes:
        return conv_volume("cl", u2, valeur)
    elif u1 in listes and u2 == "cm3":
        return conv_volume(u1, "cl", valeur)

def mm3(u1, u2, valeur):
    listes = ["kl", "hl", "dal", "l", "dl", "cl", "ml"]
    if u1 == "mm3" and u2 == "mm3":
        return valeur
    elif u1 == "mm3" and u2 in listes:
        return conv_volume("ml", u2, valeur*100)
    elif u1 in listes and u2 == "mm3":
        return conv_volume(u1, "ml", valeur)*100

# au cube volume et conv volume conversion
def cube_volume(u1, u2, valeur):
    listes = ["kl", "hl", "dal", "l", "dl", "cl", "ml"]
    listes2 = ["m3", "dm3", "cm3", "mm3"]
    if u1 in listes2 and u2 in listes2:
        puiss = listes2.index(u2) - listes2.index(u1)
        reponse = valeur * (1000**puiss)
        return reponse
    elif u1 in listes and u2 in listes:
        return conv_volume(u1, u2, valeur)
    elif (u1 == "m3" and u2 in listes) or (u2 == "m3" and u1 in listes):
        return m3(u1, u2, valeur)
    elif (u1 == "dm3" and u2 in listes) or (u2 == "dm3" and u1 in listes):
            return dm3(u1, u2, valeur)
    elif (u1 == "cm3" and u2 in listes) or (u2 == "cm3" and u1 in listes):
            return cm3(u1, u2, valeur)
    elif (u1 == "mm3" and u2 in listes) or (u2 == "mm3" and u1 in listes):
            return mm3(u1, u2, valeur)
    



# Pouces conversion
def onces(u1, u2, valeur):
    listes = ["kl", "hl", "dal", "l", "dl", "cl", "ml", "m3", "dm3", "cm3", "mm3"]
    if u1 == "onces" and u2 == "onces":
        return valeur
    elif u1 == "onces" and u2 in listes:
        ml = valeur * 29.5735
        return cube_volume("ml", u2, ml)
    elif u2 == "onces" and u1 in listes:
        ml = cube_volume(u1, "ml", valeur)
        onces = ml / 29.5735
        return onces
    


# Test
#print(onces("onces", "m3", 20))

# Pieds conversion
def tasses(u1, u2, valeur):
    listes = ["kl", "hl", "dal", "l", "dl", "cl", "ml", "m3", "dm3", "cm3", "mm3"]
    if u1 == "tasses" and u2 == "tasses":
        return valeur
    elif u1 == "tasses" and u2 in listes:
        ml = valeur * 236.588
        return cube_volume("ml", u2, ml)
    elif u2 == "tasses" and u1 in listes:
        ml = cube_volume(u1, "ml", valeur)
        tasses = ml / 236.588
        return tasses

# Test
#print(pieds("m", "pieds", 30)) 


#Yards conversion
def pintes(u1, u2, valeur):
    listes = ["kl", "hl", "dal", "l", "dl", "cl", "ml", "m3", "dm3", "cm3", "mm3"]
    if u1 == "pintes" and u2 == "pintes":
        return valeur
    elif u1 == "pintes" and u2 in listes:
        ml = valeur * 473.176
        return cube_volume("ml", u2, ml)
    elif u2 == "pintes" and u1 in listes:
        ml = cube_volume(u1, "ml", valeur)
        pintes = ml / 473.176
        return pintes

#Test
#print(yards("dm", "yards", 40))    

# Miles conversion
def gallons(u1, u2, valeur):
    listes = ["kl", "hl", "dal", "l", "dl", "cl", "ml", "m3", "dm3", "cm3", "mm3"]
    if u1 == "gallons" and u2 == "gallons":
        return valeur
    elif u1 == "gallons" and u2 in listes:
        l = valeur * 3.78541
        return cube_volume("l", u2, l)
    elif u2 == "gallons" and u1 in listes:
        l = cube_volume(u1, "l", valeur)
        gallons = l / 3.78541
        return gallons

#Test
#print(miles("miles", "mm", 20))



# Pour les autres cas
def onces_tasses(u1, u2, valeur):
    if u1 == "onces" and u2 == "tasses":
        ml = onces(u1, "ml", valeur)
        return onces("ml", u2, ml)
    elif u1 == "tasses" and u2 == "onces":
        ml = tasses(u1, "ml", valeur)
        return onces("ml", u2, ml)

#print(pouces_pieds("pouces", "pieds", 20))    

def onces_pintes(u1, u2, valeur):
    if u1 == "onces" and u2 == "pintes":
        ml = onces(u1, "ml", valeur)
        return pintes("ml", u2, ml)
    elif u1 == "pintes" and u2 == "onces":
        ml = pintes(u1, "ml", valeur)
        return onces("ml", u2, ml)

#print(pouces_yards("pouces", "yards", 20))    

def onces_gallons(u1, u2, valeur):
    if u1 == "onces" and u2 == "gallons":
        ml = onces(u1, "ml", valeur)
        return gallons("ml", u2, ml)
    elif u1 == "miles" and u2 == "pouces":
        ml = gallons(u1, "ml", valeur)
        return onces("ml", u2, ml)

#print(pouces_miles("miles", "pouces", 20))    

def tasses_pintes(u1, u2, valeur):
    if u1 == "tasses" and u2 == "pintes":
        ml = tasses(u1, "ml", valeur)
        return pintes("ml", u2, ml)
    elif u1 == "pintes" and u2 == "tasses":
        ml = pintes(u1, "ml", valeur)
        return tasses("ml", u2, ml)

#print(pieds_yards("yards", "pieds", 20))    

def tasses_gallons(u1, u2, valeur):
    if u1 == "tasses" and u2 == "gallons":
        ml = tasses(u1, "ml", valeur)
        return gallons("ml", u2, ml)
    elif u1 == "gallons" and u2 == "tasses":
        ml = gallons(u1, "ml", valeur)
        return tasses("ml", u2, ml)

#print(pieds_miles("miles", "pieds", 20))

def pintes_gallons(u1, u2, valeur):
    if u1 == "pintes" and u2 == "gallons":
        ml = pintes(u1, "ml", valeur)
        return gallons("ml", u2, ml)
    elif u1 == "gallons" and u2 == "pintes":
        ml = gallons(u1, "ml", valeur)
        return pintes("ml", u2, ml)

#print(yards_miles("miles", "yards", 20))    

def volumes_capacites(u1, u2, valeur):
    listes = ["kl", "hl", "dal", "l", "dl", "cl", "ml", "m3", "dm3", "cm3", "mm3"]
    if u1 in listes and u2 in listes:
        return cube_volume(u1, u2, valeur)
    elif u1 in listes and u2 not in listes:
        match u2:
            case "onces":
                return onces(u1, u2, valeur)
            case "tasses":
                return tasses(u1, u2, valeur)
            case "pintes":
                return pintes(u1, u2, valeur)
            case "gallons":
                return gallons(u1, u2, valeur)
    elif u1 not in listes and u2 in listes:
        match u1:
            case "onces":
                return onces(u1, u2, valeur)
            case "tasses":
                return tasses(u1, u2, valeur)
            case "pintes":
                return pintes(u1, u2, valeur)
            case "gallons":
                return gallons(u1, u2, valeur)  
    elif u1 not in listes and u2 not in listes:
        if (u1 == "onces" and u2 == "tasses") or (u1 == "tasses" and u2 == "onces"):
            return onces_tasses(u1, u2, valeur)
        elif (u1 == "onces" and u2 == "pintes") or (u1 == "pintes" and u2 == "onces"):
            return onces_pintes(u1, u2, valeur)
        elif (u1 == "onces" and u2 == "gallons") or (u1 == "gallons" and u2 == "onces"):
            return onces_gallons(u1, u2, valeur)
        elif (u1 == "tasses" and u2 == "pintes") or (u1 == "pintes" and u2 == "tasses"):
            return tasses_pintes(u1, u2, valeur)
        elif (u1 == "tasses" and u2 == "gallons") or (u1 == "gallons" and u2 == "tasses"):
            return tasses_gallons(u1, u2, valeur)
        elif (u1 == "pintes" and u2 == "gallons") or (u1 == "gallons" and u2 == "pintes"):
            return pintes_gallons(u1, u2, valeur)




#TEST FINAL CONVERSION DE u1 en u2
#print(final_conv("gallons", "pintes", 20))











