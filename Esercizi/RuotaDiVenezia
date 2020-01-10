# Ruova di Venezia
# 10 01 2020

import random

# Prendere la ruota di venezia ed estrarre S numeri

A = list()  #A = [1, 2, 3, 4, 5, .... 90]
B = list()
Estratti = []

i = 0
while i < 90:
  A.append(i + 1)
  i = i + 1
print (A)

Estratti.append("VENEZIA")

i = 0
while i <= 4:
  x = random.randint(0, 89 - i)
  
  if A[x] not in B:
    Estratti.append(A[x])
    B.append(A[x])

  i = i + 1
print (Estratti)
