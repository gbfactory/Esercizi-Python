# gbfactory
# 2020 15 10

ip = input("Inserisci un indirizzo IP: ")

ottetti = ip.split('.')

primo = ottetti[0]
primoBin = bin(int(primo))[2:]

print("Primo ottetto in binario: ")
print(primoBin)

if primoBin.startswith("0"):
    print("Questo IP è di Classe A")
elif primoBin.startswith("10"):
    print("Questo IP è di Classe B")
elif primoBin.startswith("110"):
    print("Questo IP è di Classe C")
elif primoBin.startswith("1110"):
    print("Questo IP è di Classe D")
elif primoBin.startswith("1111"):
    print("Questo IP è di Classe E")
