def moyenne(liste_notes):
    s_n, s_c = sum(v[0] * v[1] for v in liste_notes), sum(v[1] for v in liste_notes)
    return s_n / s_c


def pascal(n):
    triangle = [[1]]
    for k in range(1, n + 1):
        ligne_k = [1] + [triangle[k - 1][i - 1] + triangle[k - 1][i] for i in range(1, k)] + [1]
        triangle.append(ligne_k)
    return triangle
