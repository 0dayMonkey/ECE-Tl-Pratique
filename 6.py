def recherche(tab, n):
    try:
        return tab.index(n)
    except ValueError:
        return len(tab)


def distance(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5


def plus_courte_distance(tab, depart):
    return min(tab, key=lambda point: distance(point, depart))
