# Cifrario di Augusto
# 31 01 2020

chiaro = ((input("Inserisci il chiaro: ")).lower()).replace(" ", "")
chiave = ((input("Inserisci la chiave: ")).lower()).replace(" ", "")

while len(chiave) < len(chiaro):
    print("La chiave deve essere lunga almeno quando il chiaro!")
    chiave = ((input("Reinserisci la chiave: ")).lower()).replace(" ", "")

numChiaro = []
numChiave = []
codCifrato = []

for e in chiaro:
    x = (ord(e) - 97) + 1
    numChiaro.append(x)

for e in chiave:
    x = (ord(e) - 97) + 1
    numChiave.append(x)

i = 0
while i < len(chiaro):
    if numChiave[i] < numChiaro[i]:
        c = 26 + (numChiave[i] - numChiaro[i])
        codCifrato.append(c)
    elif numChiave[i] > numChiaro[i]:
        c = numChiave[i] - numChiaro[i]
        codCifrato.append(c)
    i = i + 1

print("CHIARO: ", numChiaro)
print("CHIAVE: ", numChiave)
print("CODICE: ", codCifrato)
