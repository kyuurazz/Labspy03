print("Menentukan Bilangan Terbesar")
print()
n = 0
while True:
    a = int(input("Masukan Bilangan : "))
    if n < a:
        n = a
    if a==0:
        break

print("Bilangan Terbesar Adalah", n)