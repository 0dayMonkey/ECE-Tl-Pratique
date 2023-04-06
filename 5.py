from random import randint

def lancer(n):
    return [randint(1, 6) for _ in range(n)]

def paire_6(tab):
    return sum(1 for v in tab if v == 6) >= 2

def nbLig(image):
    return len(image)

def nbCol(image):
    return len(image[0])

def negatif(image):
    return [[255 - pixel for pixel in row] for row in image]

def binaire(image, seuil):
    return [[int(pixel >= seuil) for pixel in row] for row in image]
