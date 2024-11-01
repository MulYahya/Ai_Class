import random

random.seed(30)

X = [random.randint(0, 10) for _ in range(20)]

print("List X:", X)

y1 = int(input("Masukkan angka genap (0-10): "))

if y1 % 2 == 0 and y1 in X:
    indeks_list = [i for i, x in enumerate(X) if x == y1]
    print(f"Angka {y1} ditemukan di indeks: {indeks_list}")
else:
    print(f"Angka {y1} tidak ada dalam list X atau bukan angka genap.")
