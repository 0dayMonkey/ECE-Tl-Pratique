def recherche(tab, n):
    deb, fin, indice = 0, len(tab) - 1, -1
    while deb <= fin and indice == -1:
        mil = (deb + fin) // 2
        if tab[mil] == n:
            indice = mil
        elif n > tab[mil]:
            deb = mil + 1
        else:
            fin = mil - 1
    return indice


ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def position_alphabet(lettre):
    return ord(lettre) - ord('A')


def cesar(message, decalage):
    return ''.join(ALPHABET[(position_alphabet(c) + decalage) % 26] if 'A' <= c <= 'Z' else c for c in message)
