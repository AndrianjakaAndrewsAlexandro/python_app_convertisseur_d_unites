# LES TEMPS

def tris_60(u1, u2, valeur):
    listes = ["heures", "min", "sec"]
    puiss = listes.index(u2) - listes.index(u1)
    return valeur * (60 ** puiss)

def heures_jours(u1, u2, valeur):
    if (u1 == "heures" and u2 == "heures") or (u1 == "Jours" and u2 == "jours"):
        return valeur
    elif u1 == "jours" and u2 == "heures":
        return valeur * 24
    elif u1 == "heures" and u2 == "jours":
        return valeur / 24

def restant(u1, u2, valeur):
    listes = ["annee", "mois", "sem", "jours"]
    if u1 == u2:
        return valeur
    elif u1 in listes and u2 in listes:
        match u1:
            case "annee":
                match u2:
                    case "mois":
                        return valeur * 12
                    case "sem":
                        return valeur * 52.142857
                    case "jours":
                        return valeur * 365
            case "mois":
                match u2:
                    case "annee":
                        return valeur / 12
                    case "sem":
                        return valeur * 4
                    case "jours":
                        return valeur * 30
            case "sem":
                match u2:
                    case "annee":
                        return valeur / 52.142857
                    case "mois":
                        return valeur / 4
                    case "jours":
                        return valeur * 7 
            case "jours":
                match u2:
                    case "annee":
                        return valeur / 365
                    case "mois":
                        return valeur / 30
                    case "sem":
                        return valeur / 7

#print(restant("jours", "annee", 10))                                                

def temps(u1, u2, valeur):
    listes = ["heures", "min", "sec"]   
    listes2 = ["annee", "mois", "sem", "jours"]
    if u1 == u2:
        return valeur
    elif u1 in listes and u2 in listes:
        return tris_60(u1, u2, valeur)
    elif u1 in listes and u2 in listes2:
        heures = tris_60(u1, "heures", valeur)
        jours = heures_jours("heures", "jours", heures)
        return restant("jours", u2, jours)
    elif u1 in listes2 and u2 in listes:
        jours = restant(u1, "jours", valeur)
        heures = heures_jours("jours", "heures", jours)
        return tris_60("heures", u2, heures)
    elif u1 in listes2 and u2 in listes2:
        return restant(u1, u2, valeur)


#print(temps("annee", "annee", 20))    
