def indices_maxi(tab):
    maxi = max(tab)
    return maxi, [i for i, x in enumerate(tab) if x == maxi]

def positif(pile):
    return [x for x in pile if x >= 0]
