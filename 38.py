def est_cyclique(plan):
    expediteur = 'A'
    destinataire = plan[expediteur]
    nb_destinaires = 1
    
    while destinataire != expediteur:
        destinataire = plan.get(destinataire, None)
        if destinataire is None:
            return False
        nb_destinaires += 1

    return nb_destinaires == len(plan)
