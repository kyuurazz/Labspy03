print("Latihan 4 Bilangan acak")
from random import random
n = int(input("Masukan Nilai N: "))
for i in range(n):
    while 1:
        n = random()
        if n < 0.5:
            break
    print(n)
print("Selesai")