def fusion(tab1, tab2):
    return sorted(tab1 + tab2)


romains = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def traduire_romain(nombre):
    total = 0
    prev_value = 0
    for char in nombre:
        value = romains[char]
        if value > prev_value:
            total += value - 2 * prev_value
        else:
            total += value
        prev_value = value
    return total
