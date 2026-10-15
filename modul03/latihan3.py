total = 0
banyak = 0

durasi = int(input("waktu proses(menit,-1 selesai): "))
while durasi != -1:
    total = total + durasi
    banyak = banyak + 1
    durasi = int(input("waktu proses(menit,-1 selesai): "))

if banyak == 0:
    print("belum ada data yang dimasukkan")
else:
    print("banyak data", banyak)
    print("rata-rata", round(total / banyak,2), "menit")