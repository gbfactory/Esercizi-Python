import random

A = []
B = []
S = []
K = []
D = []
M = []
P = []

dim = int(input("Inserisci la dimensione"))
while dim < 2 or dim > 10:
  dim = int(input("Reinserisci la dimensione"))

# VETTORE A
i = 0
while i < dim:
  x = random.randint(1, 30) # numero random tra 1 e 30
  A.append(x)
  i = i + 1
print(A)

# VETTORE B
i = 0
while i < dim:
  x = random.randint(1, 30)
  B.append(x)
  i = i + 1
print(B)

print("----------------------------")
print("1) Somma componente per componente")
print("2) Moltiplicazione per uno scalare")
print("3) Differenza componente per componente")
print("4) Moltiplicazione scalare della somma")
print("5) Concatenazione dei due vettori di partenza")
print("6) Media degli elementi di posto pari del v A")
print("----------------------------")

sel = int(input("Inserisci scelta menu"))

# punto 1
if sel == 1:
  i = 0
  while i < dim:
    x = A[i] + B[i]
    S.append(x)
    i = i + 1
  print(S)
# punto 2
elif sel == 2:
  k = int(input("Inserisci k"))
  while k == 0:
    k = int(input("Reinserisci k != 0"))
  i = 0
  while i < dim:
    x = A[i] * k
    K.append(x)
    i = i + 1
  print(K)
# punto 3
elif sel == 3:
  i = 0
  while i < dim:
    x = A[i] - B[i]
    D.append(x)
    i = i + 1
  print(D)
# punto 4
elif sel == 4:
  i = 0
  somma = 0
  while i < dim:
    x = A[i] * B[i]
    somma = somma + x
    i = i + 1
  print(somma)
# punto 5
elif sel == 5:
  x = A + B
  print(x)
# punto 6
elif sel == 6:
  while i < dim:
    if i % 2:
      P.append(A[i])
  print(P)
  x = sum(P) / len(P)
  print(x)
else:
  print("Scelta non valida!")
