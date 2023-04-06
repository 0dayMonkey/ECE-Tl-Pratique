def aire_triangle(a, b, c):
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5


def perimetre_triangle(a, b, c):
    return a + b + c


def racine(a, n=2):
    return a ** (1 / n)
