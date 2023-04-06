def multiplication(n1, n2):
    if n1 == 0 or n2 == 0:
        return 0
    if n1 < 0:
        return -multiplication(-n1, n2)
    if n2 < 0:
        return -multiplication(n1, -n2)
    s = 0
    for _ in range(n2):
        s += n1
    return s

def dichotomie(tab, x):
    debut, fin = 0, len(tab) - 1
    while debut <= fin:
        m = (debut + fin) // 2
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
            fin = m - 1
    return False
