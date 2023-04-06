def compte_caracteres(chaine):
    return {char: chaine.count(char) for char in set(chaine)}


def est_pangramme(texte):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    return alphabet.issubset(set(texte.lower()))
