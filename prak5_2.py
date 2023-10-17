#Input nama
nama = input("Nama : ")

#input jam kerja
jamKerja = int(input("Jam masuk kerja : "))

#gaji perhari
gajiPerhari = 175000

#ucapan selamat pagi, siang, sore, malam
#berdasarkan waktu
if jamKerja >=6 and jamKerja <= 12:
    print(f"selamat pagi {nama}\n")

elif jamKerja >= 12 and jamKerja <= 15 :
    print(f"selamat siang {nama}\n")

elif jamKerja >= 15 and jamKerja <= 18:
    print(f"selamat sore {nama}\n")

elif jamKerja >= 18 and jamKerja <= 24:
    print(f"selamat malam {nama}\n")
else:
    print("jam tidak valid!")


#jam keluar kerja
jamKeluarKerja = int(input("Jam keluar kerja: "))
#ucapan selamat pagi, siang, sore, malam
#berdasarkan waktu
if jamKeluarKerja >=6 and jamKeluarKerja <= 12:
    print(f"selamat pagi")

elif jamKeluarKerja >= 12 and jamKeluarKerja <= 15 :
    print(f"selamat siang")

elif jamKeluarKerja >= 15 and jamKeluarKerja <= 18:
    print(f"selamat sore")

elif jamKeluarKerja >= 18 and jamKeluarKerja <= 24:
    print(f"selamat malam")
else:
    print("Jam tidak valid!")

print(5*"-","rincian gaji",5*"-")

print(f"Nama : {nama}")

waktuKerja = jamKeluarKerja - jamKerja

print(f"Waktu Kerja = {waktuKerja} jam ({jamKerja} s.d {jamKeluarKerja})")

if waktuKerja <= 8:
    gaji_total = gajiPerhari
else:
    gaji_tambahan = (waktuKerja - 8) * 15000
    gaji_total = gajiPerhari + gaji_tambahan

print(f"Gaji perhari : {gajiPerhari}")
print(f"Lembur : {gaji_total} ({waktuKerja} * Rp.15,000)")
print ("---terima kasih---")

