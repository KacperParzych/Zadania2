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

