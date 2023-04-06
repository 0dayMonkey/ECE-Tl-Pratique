def max_dico(dico):
    return max(dico.items(), key=lambda x: x[1])


class Pile:
    def __init__(self):
        self.contenu = []

    def est_vide(self):
        return not self.contenu

    def empiler(self, v):
        self.contenu.append(v)

    def depiler(self):
        return self.contenu.pop() if self.contenu else None


def eval_expression(tab):
    p = Pile()
    for element in tab:
        if element == "+":
            p.empiler(p.depiler() + p.depiler())
        elif element == "*":
            p.empiler(p.depiler() * p.depiler())
        else:
            p.empiler(element)
    return p.depiler()
