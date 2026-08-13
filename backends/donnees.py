# Mésures des données

def bit_oct(u1, u2, valeur):
    if u1 == u2:
        return valeur
    elif u1 == "o" and u2 == "bit":
        return valeur * 8
    elif u1 == "bit" and u2 == "o":
        return valeur / 8


def standard(u1, u2, valeur):
    listes = ["po", "to", "go", "mo", "ko", "o"]
    if u1 == u2:
        return valeur
    elif u1 in listes and u2 in listes:
        puiss = listes.index(u2) - listes.index(u1)
        return valeur * (1024 ** puiss)   

def donnees(u1, u2, valeur):
    listes = ["po", "to", "go", "mo", "ko", "o"]
    if u1 == u2:
        return valeur
    elif u1 in listes and u2 in listes:
        return standard(u1, u2, valeur)
    elif u1 in listes and u2 == "bit":
        o = standard(u1, "o", valeur)
        return bit_oct("o", "bit", o)
    elif u1 == "bit" and u2 in listes:
        o = bit_oct("bit", "o", valeur)
        return standard("o", u2, o)    
        

#print(informatiques("po", "to", 20))        