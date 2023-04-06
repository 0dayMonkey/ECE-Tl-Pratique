def nombre_de_mots(phrase):
    nb = len(phrase.split()) 
    if phrase[-1] in ('?', '!'):
        return nb
    else:
        return nb+1

def notes_triees(effectifs_notes):
    return [i for i, n in enumerate(effectifs_notes) for _ in range(n)]

def dec_to_bin(nb_dec):
    if nb_dec == 0:
        return '0'
    else:
        q, r = nb_dec // 2, nb_dec % 2
        return dec_to_bin(q) + str(r)
