# CODE CARD - Caesar's code
# 30/01/2020

key = (input("Inserisci la lettera chiave: ")).upper()

while len(key) != 1 or ord(key) < 65 or ord(key) > 90:
    key = (input("Reinserisci la lettera chiave: ")).upper()

alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']

keyPos = alfabeto.index(key)

alfabetoCifrato = []

# aggiungi lettere di avanzo
i = 0
while i < keyPos:
    x = (len(alfabeto) - keyPos) + i
    alfabetoCifrato.append(alfabeto[x])
    i = i + 1

# aggiunge il resto dell'alfabeto
while i < (len(alfabeto)):
    alfabetoCifrato.append(alfabeto[i - keyPos])
    i = i + 1

print(alfabeto)
print(alfabetoCifrato)

messaggio = (input("Inserisci il messaggio da decifrare ")).upper()

messaggioDecifrato = []

for e in messaggio:
    if ord(e) < 65 or ord(e) > 90:
        messaggioDecifrato.append(e)
    else:
        x = alfabeto.index(e)
        messaggioDecifrato.append(alfabetoCifrato[x])

print("".join(messaggioDecifrato))

# FRASE DI PROVA
# grkd qkwo ny combod kqoxdc zvki? s-czi!
