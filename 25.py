def enumere(L):
    d = {}
    for i, e in enumerate(L):
        d.setdefault(e, []).append(i)
    return d

class Arbre:
    def __init__(self, etiquette):
        self.v = etiquette
        self.fg = None
        self.fd = None

    def parcours(self, liste):
        if self is not None:
            if self.fg is not None:
                self.fg.parcours(liste)
            liste.append(self.v)
            if self.fd is not None:
                self.fd.parcours(liste)
        return liste

    def insere(self, cle):
        if cle < self.v:
            if self.fg is not None:
                self.fg.insere(cle)
            else:
                self.fg = Arbre(cle)
        else:
            if self.fd is not None:
                self.fd.insere(cle)
            else:
                self.fd = Arbre(cle)

Abr = Arbre(5)
Abr.fg = Arbre(2)
Abr.fd = Arbre(7)
Abr.fg.fd = Arbre(3)
Abr.fg.fd.fd = Arbre(4)
Abr.fg.fg = Arbre(1)
Abr.fd.fg = Arbre(6)
