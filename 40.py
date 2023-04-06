def nombre_de_mots(phrase):
    nb = phrase.count(' ')
    if phrase[-1] in ('?', '!'):
        return nb
    else :
        return nb+1
