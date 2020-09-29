# Cifrario di Cesare v2
# 25 09 2020
# by gbfactory

import tkinter as tk
from tkinter import messagebox

# cifra
def cifraMessaggio():
    # var stringa
    stringa = etrStringa.get().upper()

    # controllo stringa
    if stringa == "":
        return tk.messagebox.showerror("Errore", "Devi inserire una stringa!")

    # controllo passo
    if etrPasso.get() == "":
        return tk.messagebox.showerror("Errore", "Devi inserire un passo!")
    
    # var passo
    passo = int(etrPasso.get())

    # controllo passo
    if passo > 10 or passo < 3:
        return tk.messagebox.showerror("Errore", "Il passo deve essere compreso tra 3 e 10!")

    # var str finale
    res = ""

    # codice cifratura
    for i in stringa:
        m = ord(i)

        if 65 <= m <= 90 - passo:
            res += chr(m + passo)
        elif m + passo > 90:
            res += chr(m - (26 - passo))
        else:
            res += chr(m)

    # mostra il risultato
    etrRes.delete(0, tk.END)    # cancella eventuale txt precedente
    etrRes.insert(0, res)       # imposta il nuovo txt

# decifra
def decifraMessaggio():
    # var stringa
    stringa = etrStringa.get().upper()

    # controllo stringa
    if stringa == "":
        return tk.messagebox.showerror("Errore", "Devi inserire una stringa!")

    # controllo passo
    if etrPasso.get() == "":
        return tk.messagebox.showerror("Errore", "Devi inserire un passo!")
    
    # var passo
    passo = int(etrPasso.get())

    # controllo passo
    if passo > 10 or passo < 1:
        return tk.messagebox.showerror("Errore", "Il passo deve essere compreso tra 1 e 9!")

    # var str finale
    res = ""

    # codice decifratura
    for i in stringa:
        m = ord(i)

        if (m < 65 or m > 90):
            res += chr(m)
        elif m - passo <= 64:
            res += chr(m + (26 - passo))
        elif 65 <= m <= 90 - passo:
            res += chr(m - passo)

    # mostra il risultatog 
    etrRes.delete(0, tk.END)    # cancella eventuale txt precedente
    etrRes.insert(0, res)       # imposta il nuovo txt

# gui
gui = tk.Tk()
gui.title("Cifrario di Cesare")
gui.geometry("500x250")

# stringa da cifrare o decifrare
lblInfo = tk.Label(text="Inserisci la stringa")
lblInfo.pack()

etrStringa = tk.Entry()
etrStringa.pack()

# passo
lblPasso = tk.Label(text="Inserisci il passo")
lblPasso.pack()

etrPasso = tk.Entry()
etrPasso.pack()

# bottoni per la cifratura e decifratura
btnCifra = tk.Button(gui, text="Cifra", command=cifraMessaggio)
btnCifra.pack()

btnDecifra = tk.Button(gui, text="Decifra", command=decifraMessaggio)
btnDecifra.pack()

#risultato
resTitle = tk.Label(text="Risultato")
resTitle.pack()

etrRes = tk.Entry()
etrRes.pack()

# gui
gui.mainloop()
