def palindrome(mot):
    return mot.lower() == mot.lower()[::-1]


def somme(tab):
    return sum(tab)


def moyenne(tab):
    return sum(tab) / len(tab) if tab else None
