# CODE CARD - Reverse Code
# 14/02/2020

# Inserita una stringa al contrario, la restituisce dritta e scambia la prima con l'ultima lettera

frase = input("Inserisci una stringa: ")

lista = frase.split()

decode = []

print(lista)

i = 0
while i < len(lista):
    word = lista[i]
    wordRev = word[::-1]
    wordSwap = wordRev[1:len(wordRev) - 1]
    wordFinal = wordRev[len(wordRev) - 1] + wordSwap + wordRev[0]
    decode.append(wordFinal)
    i = i + 1

print(" ".join(decode))

# FRASE DI PROVA
# caio cmoe sati
