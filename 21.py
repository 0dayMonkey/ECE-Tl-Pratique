class Noeud:
    def __init__(self, g, v, d):
        self.gauche = g
        self.valeur = v
        self.droit = d
    
    def __repr__(self):
        return str(self.valeur)

    def est_une_feuille(self):
        return self.gauche is None and self.droit is None


def expression_infixe(e):
    if e.gauche is not None:
        return f'({expression_infixe(e.gauche)}{e.valeur}{expression_infixe(e.droit)})'
    else:
        return str(e.valeur)


e = Noeud(Noeud(Noeud(None, 3, None),
            '*', Noeud(Noeud(None, 8, None), '+', Noeud(None, 7, None))),
            '-', Noeud(Noeud(None, 2, None), '+', Noeud(None, 1, None)))
    

def delta(liste):
    tab = [liste[0]]
    for i in range(1, len(liste)):
        tab.append(liste[i] - liste[i-1])
    return tab
