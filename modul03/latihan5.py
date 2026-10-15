target = 50
hari = 10

total_lolos = 0
banyak_lolos = 0

for hari in range(1, hari + 1):
    produksi = int(input(f"produksi hari ke-{hari}: "))
    if produksi >= target:
        total_lolos = total_lolos + produksi
        banyak_lolos = banyak_lolos + 1

if banyak_lolos == 0:
    print("tidak ada hari yang mencapai target")
else:
    rata = round(total_lolos / banyak_lolos, 2)
    print("hari mencapai target:", banyak_lolos)
    print("total unit pada hari produksi tersebut:", total_lolos)
    print("rata-rata unit pada hari tersebut:", rata)