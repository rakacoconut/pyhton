suhu_tertinggi = None
urutan_tertinggi = 0
count_lebih_80 = 0
total_suhu_80 = 0
count_suhu_80 = 0

for i in range(1, 9):
    suhu = int(input(f"Masukkan suhu hari ke-{i}: "))
    
    if suhu_tertinggi is None or suhu > suhu_tertinggi:
        suhu_tertinggi = suhu
        urutan_tertinggi = i

    if suhu > 80:
        count_lebih_80 += 1
        total_suhu_80 += 1
        count_suhu_80 += 1

print(f"suhu tertinggi: {suhu_tertinggi} (pencacatan ke={urutan_tertinggi})")
if count_suhu_80 == 0:
    print("tidak ada suhu di atas 80")
else:
    print(f"suhu melebihi 80: {count_lebih_80} kali")
    print(f"rata-rata suhu di atas 80: {total_suhu_80 / count_suhu_80}")