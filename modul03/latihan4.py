target = 50
hari = 10

total = 0
di_bawah = 0

for hari in range(1, hari + 1):
    produksi = int(input(f"produksi hari ke-{hari}: "))
    total = total + produksi
    if produksi < target:
        di_bawah = di_bawah + 1

print("total produksi", total)
print("rata-rata produksi", round(total / hari, 2))
print("hari di bawah target", di_bawah)