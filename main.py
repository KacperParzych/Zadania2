import random
#1
zbior1 = {1-i: i for i in range(1, 10)}
print(zbior1)
zbior2 = [4**i for i in range(0, 7)]
print(zbior2)
zbior3 = []
for i in zbior2:
    if i % 2 == 0:
        zbior3.append(i)
print(zbior3)
#2
lista1 = []
for i in range(0, 10):
    A = random.randint(1, 100)
    lista1.append(A)
print(lista1)

lista2 = []
for i in lista1:
    if i % 2 == 0:
        lista2.append(i)
print(lista2)
#3
zakupy = {"ziemniaki": "kg","lizaki": "sztuki","batony": "sztuki"}
s = [key for key in zakupy.keys()]
#4
def czy_prostokatny(a, b, c):
    if a**2 + b**2 == c**2:
        return "jest prostokatny"
    elif a ** 2 + c ** 2 == b ** 2:
        return "jest prostokatny"
    elif c**2 + b**2 == a**2:
        return "jest prostokatny"
    else:
        return "jest nie prostokatny"



print(czy_prostokatny(3, 3, 3))

#5
def pole_trapezu(q=5,w=3,e=6):
    pole = (1/2)*(q+w)*e
    return pole
print(pole_trapezu())
#6
import sys
import math
def iloczyn_elementow(o=1, p=4, ile=10):
    for i in range(ile):
        o = p*o
    return o

print(iloczyn_elementow())


import math

def pierwiastek(l):
    if l > 0:
        wynik = math.sqrt(l)
        return wynik
    else:
        print("Error!")
    return None

print("Podaj liczbe")
l = float(input())
print(pierwiastek(l))

