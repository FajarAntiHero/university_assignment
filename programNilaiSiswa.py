#Assets
line = "="*30
title = "{:^30}".format("data penilaian".upper())
title2 = "{:^30}".format("hasil penilaian".upper())

#HEADER
print(line)
print(title)
print(line)

#================== INPUT NILAI =====================
nim = input("Masukkan NIM : ")
nama = input("Masukkan Nama : ")
nilaiAbsen = int(input("Masukkan Nilai Absen : "))
nilaiTugas = int(input("Masukkan Nilai Tugas : "))
nilaiUTS = int(input("Masukkan Nilai UTS : "))
nilaiUAS = int(input("Masukkan Nilai UAS : "))

#================== OUTPUT ==========================
print(line)
print(title2)
print(line)
print("NIM Anda : ", nim)
print("nama anda : ", nama)

#HITUNG NILAI
hasilNilai = ((nilaiAbsen*0.2)
              +(nilaiTugas*0.25)
              +(nilaiUTS*0.25)
              +(nilaiUAS*0.3))
print("Hasil Nilai Anda : ", hasilNilai)

#HITUNG GRADE
if hasilNilai == 100 or hasilNilai >= 90:
    print("Grade anda : A")
elif hasilNilai == 89 or hasilNilai >= 76:
    print("Grade anda : B")
elif hasilNilai == 75 or hasilNilai >= 60:
    print("Grade anda : C")
elif hasilNilai == 59 or hasilNilai >= 46:
    print("Grade Anda : D")
elif hasilNilai == 45 or hasilNilai >= 0:
    print("Grade Anda : E")
else:
    print("nilai diluar nalar")

#HITUNG KETERANGAN LULUS ATAU GAGAL
if hasilNilai > 50:
    print("Keterangan : Lulus")
else:
    print("Keterangan : Gagal")

print(line)
print("{:^30}".format("terimakasih".upper()))
print(line)

#Code Made By Fajar Maulana
