# gbfdactory
# 2020 10 08

import random

dim = int(input("Inserisi la dimensione della lista: "))
A = []

for i in range(dim):
    A.append(random.randrange(1, 100))

print("Lista originale")
print (A)

B = A[:len(A)//2]
C = A[len(A)//2:]

print("Lista divisa in due parti")
print (B)
print (C)

