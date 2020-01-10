# Calcolatrice 1.0
# 08 01 2020

import Math.sqrt

# Inserisci due numeri
a = int(input("Inserisci un numero: "))
b = int(input("Inserisci un numero: "))

# Menu di scelta
print("Menu di scelta \n1) Addizione \n2) Sottrazione \n3) Moltiplicazione \n4) Divisione \5) Radice Quadrata")

sel = int(input("Seleziona cosa vuoi fare "))

# Calcolatrice
if sel == 1:
  risultato = a + b
elif sel == 2:
  risultato = a - b
elif sel == 3:
  risultato = a * b
elif sel == 4:
  if b != 0:
    risultato = a / b
  else:
    print("Impossibile")
elif sel == 5:
  if a > 0:
    risultato = Math.sqrt(a)
  else:
    print("Impossibile")

if sel <= 5:
  print("La scelta effettuata è ", sel)
  print("Il risultato è ", risultato)
