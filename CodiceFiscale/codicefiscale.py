# Codice Fiscale
# 18 01 2020

cognome = (input("Inserire il cognome: ")).replace(" ", "")
nome = (input("Inserire il nome: ")).replace(" ", "")
sesso = (input("inserire sesso(F o M): ")).upper()
data = input("inserire data di nascita (gg/mm/anno): ").split('/')
comune = input("inserire comune di nacita: ")

vocali = "aeiouAEIOU"

mesi = {'01': 'A', '02': 'B', '03': 'C', '04': 'D',
        '05': 'E', '06': 'H', '07': 'L', '08': 'M',
        '09': 'P', '10': 'R', '11': 'S', '12': 'T'}

pari = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
        '6': 6, '7': 7, '8': 8, '9': 9, 'A': 0, 'B': 1,
        'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7,
        'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13,
        'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19,
        'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}


dispari = {'0': 1, '1': 0, '2': 5, '3': 7, '4': 9, '5': 13,
           '6': 15, '7': 17, '8': 19, '9': 21, 'A': 1, 'B': 0,
           'C': 5, 'D': 7, 'E': 9, 'F': 13, 'G': 15, 'H': 17,
           'I': 19, 'J': 21, 'K': 2, 'L': 4, 'M': 18, 'N': 20,
           'O': 11, 'P': 3, 'Q': 6, 'R': 8, 'S': 12, 'T': 14,
           'U': 16, 'V': 10, 'W': 22, 'X': 25, 'Y': 24, 'Z': 23}

controllo = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F',
             6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L',
             12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R',
             18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X',
             24: 'Y', 25: 'Z'}

def CalcCognome(cognome):
    cons = []
    voc = []
    for x in cognome:
        if x in vocali:
            voc.append(x)
        else:
            cons.append(x)
    codCognome = "".join(cons + voc + ['x'] * 2)[0:3]

    #print(codCognome.upper())
    return codCognome.upper()


def CalcNome(nome):
    cons = []
    voc = []
    for x in nome:
        if x in vocali:
            voc.append(x)
        else:
            cons.append(x)
    if len(cons) > 3:
        cons[1:2] = []
    codNome = "".join(cons + voc + ['x'] * 2)[0:3]

    #print(codNome.upper())
    return codNome.upper()


def Data(data, sesso):
    anno = data[2][2:]
    mese = mesi[data[1]]
    if sesso == "F":
        giorno = data[0] + 40
    elif sesso == "M":
        giorno = data[0]

    #print(anno)
    #print(mese)
    #print(giorno)
    return anno + mese + giorno


def CalcCodComune(comune):
    com = comune.upper()

    f = open("comuni.txt", "r")
    for x in f:
        sCom = x.split(" -- ")
        if sCom[0] == com:
            codCat = sCom[1]
            break

    #print(codCat)
    return codCat.rstrip()

#print(codice1)

def CodiceControllo(codFisc):
    i = 0
    pariSomma = 0
    dispariSomma = 0
    p = []
    d = []
    while i < len(codFisc):
        if i % 2 != 0:
            #print(codFisc[i])
            p.append(codFisc[i])
        else:
            #print(codFisc[i])
            d.append(codFisc[i])
        i += 1

    for x in p:
        #print(x)
        pariSomma += pari[x]

    for y in d:
        #print(y)
        dispariSomma += dispari[y]

    carattere = controllo[((pariSomma + dispariSomma) % 26)]

    return carattere.upper()

codice1 = CalcCognome(cognome) + CalcNome(nome) + Data(data, sesso) + CalcCodComune(comune)

print(codice1 + CodiceControllo(codice1))
