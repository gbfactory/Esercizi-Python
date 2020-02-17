# CODE CARD - Keyword Code
# 12 02 2020

key = (input("Inserisci la parola chiave: ")).upper()

alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']
keywlist = []

for e in key:
    keywlist.append(e)

# print(keywlist)

for e in alfabeto:
    if key.find(e) == - 1:
        keywlist.append(e)

print(alfabeto)
print(keywlist)

msg = (input("Inserisci il messaggio da decifrare: ")).upper()
msgList = []
decodeMsg = []

for e in msg:
    if ord(e) == 32:
        msgList.append("*")
    else:
        msgList.append(e)

#print(msgList)

i = 0;
while i < len(msgList):
    #print(msgList[i])
    if msgList[i] == "*":
        decodeMsg.append(" ")
    elif msgList[i] != "*":
        x = keywlist.index(msgList[i])
        decodeMsg.append(alfabeto[x])
    i = i + 1

for i in decodeMsg:
    if i == "*":
        print(" ", end = "")
    print(i, end = "")

#sbfhfywmpeumpjfqqclfswmdqefrmyq
#sbf hfywmpe ump jfqqclf swm dq efrmyq
