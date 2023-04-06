def maxliste(tab):
    return max(tab)


class Pile:
    def __init__(self):
        self.valeurs = []

    def est_vide(self):
        return not self.valeurs

    def empiler(self, c):
        self.valeurs.append(c)

    def depiler(self):
        return self.valeurs.pop() if self.valeurs else None


def parenthesage(ch):
    p = Pile()
    for c in ch:
        if c == "(":
            p.empiler(c)
        elif c == ")":
            if p.est_vide():
                return False
            else:
                p.depiler()
    return p.est_vide()
