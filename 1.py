def verifie(tableau):
    return all(tableau[i] <= tableau[i+1] for i in range(len(tableau) - 1))

def depouille(urne):
    resultat = {}
    for bulletin in urne:
        resultat[bulletin] = resultat.get(bulletin, 0) + 1
    return resultat

def vainqueur(election):
    nmax = max(election.values())
    return [nom for nom, votes in election.items() if votes == nmax]
