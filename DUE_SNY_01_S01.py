import random
from traceback import print_tb
#from DUE_SNY_01_M01 import *

#import DUE_SNY_01_M01 as m
from DUE_SNY_01_M01 import osszeg as szum



#created by LP_R9SAAO
''' első probálkozás

kor = 50
nev= "Guszti"
hazas = True


kor += 5


print("Felhasználó:", nev, kor, hazas)

szoveg = "Rendszámtartó"

print(szoveg[0:4])
print(szoveg[4:8])
print(szoveg[-5:])

lista = ["Rend", "szám","tartó"]
print(lista)
print(lista[0],lista[1], lista[2], sep="")

lista.append("tábla")
print(lista)

halmaz = {1, 2, 3, "négy", 1}
print(halmaz)

szotar = {"név": "Józsi", "kor": 40, "hazas": True}
print(szotar)
'''

# kor = int(input("Hány éves vagy: "))

kor=50
print("A felhasználó kora:".center(50, "_"))
print(f"A felhasználó kora: {kor}")
print("A felhasználó kora: {}".format(kor))

print(random.randint(5,10))
szum()