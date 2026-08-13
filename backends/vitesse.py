# VITESSES

def km_h__m_s(u1, u2, valeur):
    if (u1 == "km_h" and u2 == "km_h") or (u1 == "m_s" and u2 == "m_s"):
        return valeur
    elif u1 == "km_h" and u2 == "m_s":
        return valeur / 3.6
    elif u1 == "m_s" and u2 == "km_h":
        return valeur * 3.6

def km_h_mph(u1, u2, valeur):
    if (u1 == "km_h" and u2 == "km_h") or (u1 == "mph" and u2 == "mph"):
        return valeur
    elif u1 == "km_h" and u2 == "mph":
        return valeur / 1.60934
    elif u1 == "mph" and u2 == "km_h":
        return valeur * 1.60934

def km_h_noeuds(u1, u2, valeur):
    if (u1 == "km_h" and u2 == "km_h") or (u1 == "noeuds" and u2 == "noeuds"):
        return valeur
    elif u1 == "km_h" and u2 == "noeuds":
        return valeur / 1.852
    elif u1 == "noeuds" and u2 == "km_h":
        return valeur * 1.852

def mph_noeuds(u1, u2, valeur):
    if (u1 == "mph" and u2 == "mph") or (u1 == "noeuds" and u2 == "noeuds"):
        return valeur
    elif u1 == "mph" and u2 == "noeuds":
        km_h = km_h_mph("mph", "km_h", valeur)
        return km_h_noeuds("km_h", "noeuds", km_h)
    elif u1 == "noeuds" and u2 == "mph":
        km_h = km_h_noeuds("noeuds", "km_h", valeur)    
        return km_h_mph("km_h", "mph", km_h)

def vitesses(u1, u2, valeur):
    listes = ["km_h", "m_s"]    
    if u1 in listes and u2 in listes:
        return km_h__m_s(u1, u2, valeur)
    elif u1 in listes and u2 not in listes:
        if u2 == "mph":
            km_h = km_h__m_s(u1, "km_h", valeur)
            return km_h_mph("km_h", "mph", km_h)
        elif u2 == "noeuds":
            km_h = km_h__m_s(u1, "km_h", valeur)
            return km_h_noeuds("km_h", "noeuds", km_h)
    elif u1 not in listes and u2 in listes:
        if u1 == "mph":
            km_h = km_h_mph("mph", "km_h", valeur)
            return km_h__m_s("km_h", u2, km_h)
        elif u1 == "noeuds":
            km_h = km_h_noeuds("noeuds", "km_h", valeur)
            return km_h__m_s("km_h", u2, km_h)
    elif u1 not in listes and u2 not in listes:
        return mph_noeuds(u1, u2, valeur)    

#print(conv_final("m_s", "m_s", 20))    