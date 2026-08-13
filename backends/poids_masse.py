# POIDS ET MASSE

#Pour l'un des unités appartien à [km, hm, dam, m, dm, cm, mm] ou que les deux unités sont égaux
def conv_masse(u1, u2, valeur):
    listes = ["t", "q", "dkg", "kg", "hg", "dag", "g", "dg", "cg", "mg"]
    puiss = listes.index(u2) - listes.index(u1)
    reponse = valeur * (10**puiss)
    return reponse


# Onces conversion
def onces(u1, u2, valeur):
    listes = ["t", "q", "dkg", "kg", "hg", "dag", "g", "dg", "cg", "mg"]
    if u1 == "onces" and u2 == "onces":
        return valeur
    elif u1 == "onces" and u2 in listes:
        g = valeur * 28.3495
        return conv_masse("g", u2, g)
    elif u2 == "onces" and u1 in listes:
        g = conv_masse(u1, "g", valeur)
        onces = g / 28.3495
        return onces

# Livres conversion
def livres(u1, u2, valeur):
    listes = ["t", "q", "dkg", "kg", "hg", "dag", "g", "dg", "cg", "mg"]
    if u1 == "livres" and u2 == "livres":
        return valeur
    elif u1 == "livres" and u2 in listes:
        kg = valeur * 0.453592
        return conv_masse("kg", u2, kg)
    elif u2 == "livres" and u1 in listes:
        kg = conv_masse(u1, "kg", valeur)
        livres = kg / 0.453592
        return livres    


def onces_livres(u1, u2, valeur):
    if u1 == "onces" and u2 == "livres":
        g = onces(u1, "g", valeur)
        return livres("g", u2, g)
    elif u1 == "livres" and u2 == "onces":
        g = livres(u1, "g", valeur)
        return onces("g", u2, g)

    
# Conversion final
def poids_masses(u1, u2, valeur):
    listes = ["t", "q", "dkg", "kg", "hg", "dag", "g", "dg", "cg", "mg"]
    if u1 in listes and u2 in listes:
        return conv_masse(u1, u2, valeur)
    elif u1 in listes and u2 not in listes:
        match u2:
            case "onces":
                return onces(u1, u2, valeur)
            case "livres":
                return livres(u1, u2, valeur)
    elif u1 not in listes and u2 in listes:
        match u1:
            case "onces":
                return onces(u1, u2, valeur)
            case "livres":
                return livres(u1, u2, valeur)  
    elif u1 not in listes and u2 not in listes:
        if (u1 == "onces" and u2 == "livres") or (u1 == "livres" and u2 == "onces"):
            return onces_livres(u1, u2, valeur)
          
#print(final_conv("mg", "livres", 20))                   