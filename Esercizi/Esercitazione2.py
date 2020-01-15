# Esercitazione 2
# 14 01 2020

n = int(input("Inserisci il lato "))

l = int(input("Inserisci i lati del poligono da 3 a 10 "))

while l < 3 or l > 10:
    l = int(input("Reinserisci i lati del poligono "))

if l == 3:
    f = 0.28867
elif l == 4:
    f = 0.5
elif l == 5:
    f = 0.68819
elif l == 6:
    f = 0.86602
elif l == 7:
    f = 1.03826
elif l == 8:
    f = 1.20710
elif l == 9:
    f = 1.37373
elif l == 10:
    f = 1.53884

perimetro = n * l
apotema = f * l
area = perimetro / 2 * apotema

print("---[ RISULTATI ]---")
print(" > Lunghezza lato ", n)
print(" > N lati ", l)
print(" > Perimetro ", perimetro)
print(" > Apotema ", apotema)
print(" > Area ", area)
print("-------------------")
