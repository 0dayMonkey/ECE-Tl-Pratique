def fibonacci(n):
    a, b = 1, 1
    for i in range(3, n+1):
        a, b = b, a+b
    return b

def pantheon(eleves, notes):
    note_maxi = 0
    meilleurs_eleves =  []

    for eleve, note in zip(eleves, notes):
        if note == note_maxi:
            meilleurs_eleves.append(eleve)
        elif note > note_maxi:
            note_maxi = note
            meilleurs_eleves = [eleve]

    return (note_maxi,meilleurs_eleves)
