def multiplication(n1, n2):
    return sum(n1 for _ in range(abs(n2))) * (-1 if n2 < 0 else 1)


def chercher(tab, n, i, j):
    while i <= j:
        m = (i + j) // 2
        if tab[m] < n:
            i = m + 1
        elif tab[m] > n:
            j = m - 1
        else:
            return m
    return None
