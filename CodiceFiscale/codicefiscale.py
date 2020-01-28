# Codice Fiscale
# 18 01 2020

cogn = input("Inserisci il cognome: ")
noms = input("Inserisci il nome: ")
sess = input("Inserisci il sesso: ")
dataGiorno = int(input("Inserisci il giorno di nascita: "))
dataMese = int(input("Inserisci il mese di nascita: "))
dataAnno = int(input("Inserisci l'anno di nascita: "))
luogo = input("Inserisci il luogo di nascita: ")

codicefiscale = ""

# CALCOLO COGNOME
cognome = cogn.upper()
cCons = ""
cVocs = ""

i = 0
for i in cognome:
    c = i
    if c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U':
        if len(cVocs) < 3:
            cVocs = cVocs + c
        else:
            cCons = cCons + c
            if len(cCons) == 3:
                cVocs = ""
                break

if len(cCons) < 3:
    if len(cCons) == 2:
        cCons = cCons + cVocs[0]
    if len(cCons) == 1:
        if len(cCons) > 1:
            cCons = cCons + cVocs[0] + cVocs[1]
        else:
            cCons = cCons + cVocs[0] + "X"
    if len(cCons) == 0:
        if len(cVocs) < 3:
            cCons = cCons + cVocs + "X"
        else:
            cCons = cVocs

codicefiscale = codicefiscale + cCons

# CALCOLO NOME
nome = noms.upper()

nCons = ""
nVocs = ""

i = 0
for i in nome:
    c = i
    if c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U':
        if len(nVocs) < 3:
            nVocs = nVocs + c
        else:
            nCons = nCons + c
            if len(nCons) == 4:
                nVocs = ""
                break

if len(nCons) < 3:
    if len(nCons) == 2:
        nCons = nVocs[0]
    if len(nCons) == 1:
        if len(nVocs) > 1:
            nCons = nCons[0] + nVocs[1]
        else:
            nCons = nCons + nVocs[0] + 'X'
    if len(nCons) == 0:
        if len(nVocs) < 3:
            nVocs = nVocs + 'X'
        else:
            nCons = nVocs

if len(nCons) > 3:
    temp = nCons
    nCons = ""
    nCons = nCons + temp[0] + temp[2] + temp[3]

codicefiscale = codicefiscale + nCons

# ANNO
anno = dataAnno % 100

if anno <= 9:
    annoString = "0" + str(anno)
else:
    annoString = str(anno)

codicefiscale = codicefiscale + annoString

# MESE
if dataMese == 1:
    meseCode = "A"
elif dataMese == 2:
    meseCode = "B"
elif dataMese == 3:
    meseCode = "C"
elif dataMese == 4:
    meseCode = "D"
elif dataMese == 5:
    meseCode = "E"
elif dataMese == 6:
    meseCode = "H"
elif dataMese == 7:
    meseCode = "L"
elif dataMese == 8:
    meseCode = "M"
elif dataMese == 9:
    meseCode = "P"
elif dataMese == 10:
    meseCode = "R"
elif dataMese == 11:
    meseCode = "S"
elif dataMese == 12:
    meseCode = "T"

codicefiscale = codicefiscale + meseCode

# GIORNO
sesso = sess.upper()
if sesso == "F":
    giornoCode = str(dataGiorno + 40)
else:
    giornoCode = str(dataGiorno)

codicefiscale = codicefiscale + giornoCode

# CODICE CATASTALE
comune = luogo.upper()

f = open("comuni.txt", "r")
for x in f:
    sCom = x.split(" -- ")
    if sCom[0] == comune:
        codCat = sCom[1]
        break

codicefiscale = codicefiscale + codCat

# CARATTERE DI CONTROLLO

# caratteri pari
pari = ""
for i in range(len(codicefiscale)):
    if i % 2 == 0:
        pari = pari + codicefiscale[i]

# caratteri dispari
dispari = ""
for i in range(len(codicefiscale)):
    if i % 2 == 0:
        dispari = dispari + codicefiscale[i]

# conversione char dispari
rDispari = 0
for i in dispari:
    if i == 0 or i == 'A':
        rDispari = rDispari + 1
        break
    elif i == 1 or i == 'B':
        rDispari = rDispari + 0
        break
    elif i == 2 or i == 'C':
        rDispari = rDispari + 5
        break
    elif i == 3 or i == 'D':
        rDispari = rDispari + 7
        break
    elif i == 4 or i == 'E':
        rDispari = rDispari + 9
        break
    elif i == 5 or i == 'F':
        rDispari = rDispari + 13
        break
    elif i == 6 or i == 'G':
        rDispari = rDispari + 15
        break
    elif i == 7 or i == 'H':
        rDispari = rDispari + 17
        break
    elif i == 8 or i == 'I':
        rDispari = rDispari + 19
        break
    elif i == 9 or i == 'J':
        rDispari = rDispari + 21
        break
    elif i == 'K':
        rDispari = rDispari + 2
        break
    elif i == 'L':
        rDispari = rDispari + 4
        break
    elif i == 'M':
        rDispari = rDispari + 18
        break
    elif i == 'N':
        rDispari = rDispari + 20
        break
    elif i == 'O':
        rDispari = rDispari + 11
        break
    elif i == 'P':
        rDispari = rDispari + 3
        break
    elif i == 'Q':
        rDispari = rDispari + 6
        break
    elif i == 'R':
        rDispari = rDispari + 8
        break
    elif i == 'S':
        rDispari = rDispari + 12
        break
    elif i == 'T':
        rDispari = rDispari + 14
        break
    elif i == 'U':
        rDispari = rDispari + 16
        break
    elif i == 'V':
        rDispari = rDispari + 10
        break
    elif i == 'W':
        rDispari = rDispari + 22
        break
    elif i == 'X':
        rDispari = rDispari + 25
        break
    elif i == 'Y':
        rDispari = rDispari + 24
        break
    elif i == 'Z':
        rDispari = rDispari + 23
        break

# conversione valori pari
rPari = 0

for i in pari:
    n = ord(i)

    if i.isalpha():
        rPari = rPari + n
    else:
        x = n - 65
        rPari = rPari + x

# somma
somma = rDispari + rPari
resto = int(somma % 26)
restoConv = ord(resto) + 65
codicefiscale = codicefiscale + restoConv

print(codicefiscale)
