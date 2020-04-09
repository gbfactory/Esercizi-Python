# Problema di trigonometria
# GB Factory
# 09 04 2020

import turtle
import math

# Dati iniziali del problema
gradiA = 50
posizioneAngolo = "B"
ipotenusaBC = 5

# Converto gradi in radianti
radianti = gradiA / 180.0 * math.pi

# Trovo il cateto AB e arrotondo a 2
catetoAB = round(ipotenusaBC * math.cos(radianti), 2)

# Trovo il cateto BC e arrotondo a 2
catetoAC = round(ipotenusaBC * math.sin(radianti), 2)

# Stampo i lati
print ("AB: ", catetoAB)
print ("AC: ", catetoAC)
print ("BC: ", ipotenusaBC)

# Disegno il triangolo con Turtle
tartaruga = turtle.Turtle()

# Disegno il cateto AC (misure amplificate per scala)
tartaruga.forward(catetoAC * 30)
 
# Disegno il cateto AB (misure amplificate per scala)
tartaruga.left(90)
tartaruga.forward(catetoAB * 30)

# Disegno l'ipotenusa (misure amplificate per scala)
tartaruga.left((180 - gradiA))
tartaruga.forward(ipotenusaBC * 30)

# Finisco la tartaruga
turtle.done()
