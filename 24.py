from collections import Counter

def nbr_occurrences(chaine):
    return dict(Counter(chaine))

def fusion(lst1, lst2):
    lst12 = []
    i1 = i2 = 0
    n1, n2 = len(lst1), len(lst2)
    while i1 < n1 and i2 < n2:
        if lst1[i1] < lst2[i2]:
            lst12.append(lst1[i1])
            i1 += 1
        else:
            lst12.append(lst2[i2])
            i2 += 1
    lst12.extend(lst1[i1:])
    lst12.extend(lst2[i2:])
    return lst12
