def convertir(tab):
    return sum(val * 2 ** i for i, val in enumerate(reversed(tab)))


def tri_insertion(tab):
    for i in range(1, len(tab)):
        valeur_insertion = tab[i]
        j = i
        while j > 0 and valeur_insertion < tab[j - 1]:
            tab[j] = tab[j - 1]
            j -= 1
        tab[j] = valeur_insertion
    return tab