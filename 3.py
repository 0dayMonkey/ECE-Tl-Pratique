def moyenne(tab):
    s_valeur = sum(v[0]*v[1] for v in tab)
    s_coef = sum(v[1] for v in tab)
    return s_valeur / s_coef if s_coef != 0 else None

def affiche(dessin):
    for ligne in dessin:
        print("".join(" *" if col == 1 else "  " for col in ligne))

def zoomListe(liste_depart, k):
    return [elt for elt in liste_depart for _ in range(k)]

def zoomDessin(grille, k):
    return [zoomListe(elt, k) for elt in grille for _ in range(k)]
