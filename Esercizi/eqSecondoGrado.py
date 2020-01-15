# Equazioni di Secondo Grado
# 15 01 2020

import math

a = int(input("Inserisci il coefficiente a"))
b = int(input("Inserisci il coefficiente b"))
c = int(input("Inserisci il coefficiente c"))

if a == 0:
    print("Retta")

delta = pow(b, 2) - 4 * a * c
if delta == 0:
    # Una soluzione
    x1 = -b / (2 * a)
    print("x1 = x2 = ", x1)
elif delta > 0:
    x1 = (-b-math.sqrt(delta))/(2*a)
    x2 = (-b+math.sqrt(delta))/(2*a)
    print("x1 = ", x1)
    print("x2 = ", x2)
elif delta < 0:
    print("Nessuna soluzione")

if a > 0 and delta > 0:
    # Intervalli esterni
    print("Parabola sorridente")
    print("x <= ", x1, " o x>= ", x2)
elif a < 0 and delta > 0:
    # Intervalli interni
    print("Parabola triste")
    print(x1, " < x < ", x2)
