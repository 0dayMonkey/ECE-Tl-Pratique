def ajoute_dictionnaires(d1, d2):
    d = {k: d1[k] + d2[k] if k in d2 else d1[k] for k in d1}
    d.update({k: d2[k] for k in d2 if k not in d})
    return d


from random import randrange

def nbre_coups():
    n = 0
    cases_vues = {0}
    case_en_cours = 0
    nbre_cases = 12
    while len(cases_vues) < nbre_cases:
        x = randrange(1, 7)
        case_en_cours = (case_en_cours + x) % nbre_cases
        if case_en_cours not in cases_vues:
            cases_vues.add(case_en_cours)
        n += 1
    return n
