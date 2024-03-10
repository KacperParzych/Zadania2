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