def factorielle(n):
    return 1 if n == 0 else n * factorielle(n - 1)


def somme_recursive(n):
    return 0 if n == 0 else n + somme_recursive(n - 1)


def puissance_recursive(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        temp = puissance_recursive(x, n // 2)
        return temp * temp
    else:
        return x * puissance_recursive(x, n - 1)
