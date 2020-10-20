# gbfactory
# 2020 10 15

import random

dim = int(input("Inserisi la dimensione della lista: "))

while dim < 3 or dim > 15:
    dim = int(input("Reinserisci la dimensione: "))

A = []

for i in range(dim):
    A.append(random.randrange(1, 100))

print("Lista originale")
print(A)

P = []
D = []

for x in A:
    if x % 2 == 0:
        P.append(x)
    else:
        D.append(x)

print("Lista Pari")
print(P)

print("Lista Dispari")
print(D)

divi = []

for x in A:
    if x % 2 == 0 or x % 3 == 0:
        divi.append(x)

print("Numeri divisibili per 2 o per 3")
print(divi)

media = sum(divi) / len(divi)

print("Media dell'array precedente")
print(media)

piccolo = A[:3]

print("Vettore di lunghezza 3")
print(piccolo)
