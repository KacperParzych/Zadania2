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
s = {}
#4
def czy_prostokatny(a, b, c):
    if a**2 + b**2 == c**2:
        print("jest prostokatny")
        return 0
    elif a ** 2 + c ** 2 == b ** 2:
        print("jest prostokatny")
        return 0
    elif c**2 + b**2 == a**2:
        print("jest prostokatny")
        return 0
    else:
        print("jest nie prostokatny")
        return 0


print(czy_prostokatny(3, 3, 3))



