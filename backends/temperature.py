# Les température
# F: Fahrenheit, C: Celcius? K: Kelvin


def F_C(u1, u2, valeur):
    if (u1 == "F" and u2 == "F") or (u1 == "C" and u2 == "C"):
        return valeur
    elif u1 == "F" and u2 == "C":
        return (valeur - 32) * (5/9)
    elif u1 == "C" and u2 == "F":
        return (valeur * (9/5)) + 32

def K_C(u1, u2, valeur):
    if (u1 == "K" and u2 == "K") or (u1 == "C" and u2 == "C"):
        return valeur
    elif u1 == "K" and u2 == "C":
        return valeur - 273.15
    elif u1 == "C" and u2 == "K":
        return valeur + 273.15

def F_K(u1, u2, valeur):
    if (u1 == "F" and u2 == "F") or (u1 == "K" and u2 == "K"):
        return valeur
    elif u1 == "K" and u2 == "F":
        C = K_C("K", "C", valeur)
        return F_C("C", "F", C)      
    elif u1 == "F" and u2 == "K":
        C = F_C("F", "C", valeur)
        return K_C("C", "K", C)


def temperatures(u1, u2, valeur):
    listes = ["F", "C"]
    if u1 in listes and u2 in listes:
        return F_C(u1, u2, valeur)
    elif u1 not in listes and u2 in listes:
        if u2 == "F":
            return F_K(u1, u2, valeur)
        elif u2 == "C":
            return K_C(u1, u2, valeur)
    elif u1 in listes and u2 not in listes:
        if u1 == "F":
            return F_K(u1, u2, valeur)
        elif u1 == "C":
            return K_C(u1, u2, valeur)
    elif u1 not in listes and u2 not in listes:
        if u1 == "K" and u2 == "K":
            return valeur    

#print(temperatures("C", "C", 20))        