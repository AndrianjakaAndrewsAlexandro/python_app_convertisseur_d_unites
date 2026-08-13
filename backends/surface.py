# Les surfaces

def standard(u1, u2, valeur):
    listes = ["km2", "ha", "a", "m2", "dm2", "cm2", "mm2"]
    elant = listes.index(u2) - listes.index(u1)
    return valeur * (10 ** (2*elant))

#print(standard("cm2", "m2", 20))

def acres_m2(u1, u2, valeur):
    if u1 == u2:
        return valeur
    elif u1 == "acres" and u2 == "m2":
        return valeur * 4046.856
    elif u1 == "m2" and u2 == "acres":
        return valeur /4046.856

def surfaces(u1, u2, valeur):
    listes = ["km2", "ha", "a", "m2", "dm2", "cm2", "mm2"]
    if u1 == u2:
        return valeur
    elif u1 in listes and u2 in listes:
        return standard(u1, u2, valeur)
    elif u1 == "acres" and u2 in listes:
        m2 = acres_m2(u1, "m2", valeur)
        return standard("m2", u2, m2)
    elif u1 in listes and u2 == "acres":
        m2 = standard(u1, "m2", valeur)
        return acres_m2("m2", "acres", m2)

#print(surface("dm2", "acres", 20))