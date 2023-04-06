def liste_puissances(a, n):
    return [a**i for i in range(n)]

def liste_puissances_borne(a, borne):
    if borne <= a:
        return []
    tab = [a]
    while True:
        r = tab[-1] * a
        if r < borne:
            tab.append(r)
        else:
            break
    return tab

