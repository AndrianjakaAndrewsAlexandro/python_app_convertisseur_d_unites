# Les fonctions de backend utilisés dans l'appli de converisseur d 'unités

# LONGUEUR ET DISTANCES
# Fonction de raccourcissement
# De l'unité u1 vers l'unité u2 avec la valeur d'entrée valeur

#Pour l'un des unités appartien à [km, hm, dam, m, dm, cm, mm] ou que les deux unités sont égaux
def conv_long(u1, u2, valeur):
    listes = ["km", "hm", "dam", "m", "dm", "cm", "mm"]
    puiss = listes.index(u2) - listes.index(u1)
    reponse = valeur * (10**puiss)
    return reponse
#Test
#print(conv_long("cm", "cm", 20))

# Pouces conversion
def pouces(u1, u2, valeur):
    listes = ["km", "hm", "dam", "m", "dm", "cm", "mm"]
    if u1 == "pouces" and u2 == "pouces":
        return valeur
    elif u1 == "pouces" and u2 in listes:
        cm = valeur * 2.54
        return conv_long("cm", u2, cm)
    elif u2 == "pouces" and u1 in listes:
        cm = conv_long(u1, "cm", valeur)
        pouces = cm / 2.54
        return pouces

# Test
#print(pouces("pouces", "pouces", 18))

# Pieds conversion
def pieds(u1, u2, valeur):
    listes = ["km", "hm", "dam", "m", "dm", "cm", "mm"]
    if u1 == "pieds" and u2 == "pieds":
        return valeur
    elif u1 == "pieds" and u2 in listes:
        cm = valeur * 30.48
        return conv_long("cm", u2, cm)
    elif u2 == "pieds" and u1 in listes:
        cm = conv_long(u1, "cm", valeur)
        pieds = cm / 30.48
        return pieds

# Test
#print(pieds("m", "pieds", 30)) 


#Yards conversion
def yards(u1, u2, valeur):
    listes = ["km", "hm", "dam", "m", "dm", "cm", "mm"]
    if u1 == "yards" and u2 == "yards":
        return valeur
    elif u1 == "yards" and u2 in listes:
        m = valeur * 0.9144
        return conv_long("m", u2, m)
    elif u2 == "yards" and u1 in listes:
        m = conv_long(u1, "m", valeur)
        yards = m / 0.9144
        return yards

#Test
#print(yards("dm", "yards", 40))    

# Miles conversion
def miles(u1, u2, valeur):
    listes = ["km", "hm", "dam", "m", "dm", "cm", "mm"]
    if u1 == "miles" and u2 == "miles":
        return valeur
    elif u1 == "miles" and u2 in listes:
        km = valeur * 1.60934
        return conv_long("km", u2, km)
    elif u2 == "miles" and u1 in listes:
        km = conv_long(u1, "km", valeur)
        miles = km / 1.60934
        return miles

#Test
#print(miles("miles", "mm", 20))



# Pour les autres cas
def pouces_pieds(u1, u2, valeur):
    if u1 == "pouces" and u2 == "pieds":
        cm = pouces(u1, "cm", valeur)
        return pieds("cm", u2, cm)
    elif u1 == "pieds" and u2 == "pouces":
        cm = pieds(u1, "cm", valeur)
        return pouces("cm", u2, cm)

#print(pouces_pieds("pouces", "pieds", 20))    

def pouces_yards(u1, u2, valeur):
    if u1 == "pouces" and u2 == "yards":
        cm = pouces(u1, "cm", valeur)
        return yards("cm", u2, cm)
    elif u1 == "yards" and u2 == "pouces":
        cm = yards(u1, "cm", valeur)
        return pouces("cm", u2, cm)

#print(pouces_yards("pouces", "yards", 20))    

def pouces_miles(u1, u2, valeur):
    if u1 == "pouces" and u2 == "miles":
        cm = pouces(u1, "cm", valeur)
        return miles("cm", u2, cm)
    elif u1 == "miles" and u2 == "pouces":
        cm = miles(u1, "cm", valeur)
        return pouces("cm", u2, cm)

#print(pouces_miles("miles", "pouces", 20))    

def pieds_yards(u1, u2, valeur):
    if u1 == "pieds" and u2 == "yards":
        cm = pieds(u1, "cm", valeur)
        return yards("cm", u2, cm)
    elif u1 == "yards" and u2 == "pieds":
        cm = yards(u1, "cm", valeur)
        return pieds("cm", u2, cm)

#print(pieds_yards("yards", "pieds", 20))    

def pieds_miles(u1, u2, valeur):
    if u1 == "pieds" and u2 == "miles":
        cm = pieds(u1, "cm", valeur)
        return miles("cm", u2, cm)
    elif u1 == "miles" and u2 == "pieds":
        cm = miles(u1, "cm", valeur)
        return pieds("cm", u2, cm)

#print(pieds_miles("miles", "pieds", 20))

def yards_miles(u1, u2, valeur):
    if u1 == "yards" and u2 == "miles":
        cm = yards(u1, "cm", valeur)
        return miles("cm", u2, cm)
    elif u1 == "miles" and u2 == "yards":
        cm = miles(u1, "cm", valeur)
        return yards("cm", u2, cm)

#print(yards_miles("miles", "yards", 20))    

def longeurs_distances(u1, u2, valeur):
    listes = ["km", "hm", "dam", "m", "dm", "cm", "mm"]
    if u1 in listes and u2 in listes:
        return conv_long(u1, u2, valeur)
    elif u1 in listes and u2 not in listes:
        match u2:
            case "pouces":
                return pouces(u1, u2, valeur)
            case "pieds":
                return pieds(u1, u2, valeur)
            case "yards":
                return yards(u1, u2, valeur)
            case "miles":
                return miles(u1, u2, valeur)
    elif u1 not in listes and u2 in listes:
        match u1:
            case "pouces":
                return pouces(u1, u2, valeur)
            case "pieds":
                return pieds(u1, u2, valeur)
            case "yards":
                return yards(u1, u2, valeur)
            case "miles":
                return miles(u1, u2, valeur)  
    elif u1 not in listes and u2 not in listes:
        if (u1 == "pouces" and u2 == "pieds") or (u1 == "pieds" and u2 == "pouces"):
            return pouces_pieds(u1, u2, valeur)
        elif (u1 == "pouces" and u2 == "yards") or (u1 == "yards" and u2 == "pouces"):
            return pouces_yards(u1, u2, valeur)
        elif (u1 == "pouces" and u2 == "miles") or (u1 == "miles" and u2 == "pouces"):
            return pouces_miles(u1, u2, valeur)
        elif (u1 == "pieds" and u2 == "yards") or (u1 == "yards" and u2 == "pieds"):
            return pieds_yards(u1, u2, valeur)
        elif (u1 == "pieds" and u2 == "miles") or (u1 == "miles" and u2 == "pieds"):
            return pieds_miles(u1, u2, valeur)
        elif (u1 == "yards" and u2 == "miles") or (u1 == "miles" and u2 == "yards"):
            return yards_miles(u1, u2, valeur)



#print(conv_long("cm", "dm", 20))
#print(pouces("pouces", "dm", 18))
#print(pieds("m", "pieds", 30))
#print(yards("dm", "yards", 40))
#print(miles("miles", "mm", 20))
#print(pouces_pieds("pouces", "pieds", 20))
#print(pouces_yards("pouces", "yards", 20))
#print(pouces_miles("miles", "pouces", 20))
#print(pieds_yards("yards", "pieds", 20))
#print(pieds_miles("miles", "pieds", 20))
#print(yards_miles("miles", "yards", 20))


# TEST FINAL CONVERSION DE u1 en u2
#print(final_conv("cm", "mm", 10))











