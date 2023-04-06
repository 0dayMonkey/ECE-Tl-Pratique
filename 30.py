def moyenne(tab):
    return sum(tab) / len(tab)

def binaire(a):
    bin_a = ''
    while a > 0:
        bin_a = str(a % 2) + bin_a
        a //= 2
    return bin_a if bin_a else '0'