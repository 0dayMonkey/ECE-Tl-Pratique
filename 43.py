def ecriture_binaire_entier_positif(n):
    tab = []
    while n > 0:
        tab.insert(0, n%2)
        n = n // 2
    return tab

def tri_bulles(T):
    n = len(T)
    for i in range(n-1):
        for j in range(n-i-1):
            if T[j] > T[j+1]:
                T[j], T[j+1] = T[j+1], T[j]
    return T
