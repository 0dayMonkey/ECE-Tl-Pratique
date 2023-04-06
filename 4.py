def a_doublon(liste):
    return any(liste[i] == liste[i-1] for i in range(1, len(liste)))

def voisinage(n, ligne, colonne):
    return [(l, c) for l in range(max(0, ligne-1), min(n, ligne+2)) for c in range(max(0, colonne-1), min(n, colonne+2)) if (l, c) != (ligne, colonne)]

def genere_grille(bombes):
    n = len(bombes)
    grille = [[0 for _ in range(n)] for _ in range(n)]
    for ligne, colonne in bombes:
        grille[ligne][colonne] = -1
        for l, c in voisinage(n, ligne, colonne):
            if grille[l][c] != -1:
                grille[l][c] += 1
    return grille
