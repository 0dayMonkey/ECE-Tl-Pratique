def couples_consecutifs(tab):
    t = [(tab[i], tab[i+1]) for i in range(len(tab)-1) if tab[i+1] - tab[i] == 1]
    return t
