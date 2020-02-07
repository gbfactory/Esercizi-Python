# Inserire da tastiera una frase, trasformarla in lista e calcoare la somma degli ordinali di ogni parola.
# 07 02 2020

frase = input("Inserisci una frase: ")

lista = []

lista = frase.split(" ")

print(lista)

somma = 0
for e in lista:
    for x in e:
        somma = somma + ord(x)
    print(somma)
    somma = 0
