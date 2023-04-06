def recherche_indices_classement(elt, tab):
    l_inf, l_eg, l_sup = [], [], []
    for i, val in enumerate(tab):
        if val > elt:
            l_sup.append(i)
        elif val < elt:
            l_inf.append(i)
        else:
            l_eg.append(i)
    return l_inf, l_eg, l_sup


def moyenne(nom, dico_result):
    if nom in dico_result:
        notes = dico_result[nom]
        total_points = sum(note * coef for note, coef in notes.values())
        total_coefficients = sum(coef for _, coef in notes.values())
        return round(total_points / total_coefficients, 1)
    return -1
