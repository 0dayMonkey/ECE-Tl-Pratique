def max_et_indice(tab):
    maxi, index_m = tab[0], 0
    for i, val in enumerate(tab[1:], 1):
        if val > maxi:
            index_m, maxi = i, val
    return maxi, index_m


def est_un_ordre(tab):
    return all(i in tab for i in range(1, len(tab) + 1))


def nombre_points_rupture(ordre):
    assert est_un_ordre(ordre)
    n, nb = len(ordre), 0
    if ordre[0] != 1:
        nb += 1
    nb += sum(1 for i in range(len(ordre) - 1) if abs(ordre[i + 1] - ordre[i]) != 1)
    if ordre[n - 1] != n:
        nb += 1
    return nb
