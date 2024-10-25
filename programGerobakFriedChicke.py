"""
Soal:
Sebuah perusahaan ayam goreng dengan nama “GEROBAK FRIED CHICKEN” yang 
telah lumayan banyak pelanggannya, ingin dibantu dibuatkan program untuk membantu 
kelancaran usahaannya

Buatlah programnya dengan ketentuan: 
• Setiap pembeli dikenakan pajak sebesar 10% dari pembayaran. 
• Banyak Jenis, Jenis Potong dan Banyak Beli diinput.
"""
# IMPORT MODULE OS
import os


# ASSETS
line = "="*100
title = "{:^100}".format("gerobak fried chicken".upper())
dashboardP = "{:^100}".format("dashboard pemesanan".upper())
dashboardR = "{:^100}".format("dashboard riwayat".upper())
hasilPemesanan = "{:^100}".format("hasil pemesanan".upper())

#CLEAR LAYAR 
set_option = os.name
match set_option:
    case "posix": os.system("clear")
    case "nt": os.system("cls")

# MENU GEROBAK FRIED CHICKEN
def dashboard():
    print(title)
    print(line)
    print("")
    print("{:^100}".format("menu".upper()))
    print(line)
    print("| {:<10}{:^76}{:<10} |".format("Kode", "Jenis Potong", "Harga"))
    print(line)
    print("| {:<10}{:^76}{:<10} |".format("D", "Dada Atas", "10000"))
    print("| {:<10}{:^76}{:<10} |".format("P", "Paha Atas", "9000"))
    print("| {:<10}{:^76}{:<10} |".format("S", "Sayap", "9000"))
    print(line)

# Variable Data
dataPotong = []
dataJenis = []
dataHarga = []
dataJumlah = []

#Progress
dashboard()
main = str(input("Buat Pesanan / Riwayat Pesanan [B/R] : "))
if main == "B" or main == "b":
    print("")
    print(dashboardP)
    print("")
    while True:
        print(line)
        jenisPotong = str(input("Pesan bagian apa? [D/S/P] : "))
        print("")
        if jenisPotong == "D" or jenisPotong == "d":
            potong = int(input("Berapa Potong? : "))
            jenisPotong = "Dada Atas"
            hargaSatuan = 10000
            jumlahPotong = hargaSatuan * potong
            dataPotong.append(int(potong))
            dataJenis.append(jenisPotong)
            dataHarga.append(int(hargaSatuan))
            dataJumlah.append(int(jumlahPotong))
            tambah = str(input("Pesan Lagi? [Y/N] : "))
            if tambah == "N" or tambah == "n":
                break
            elif tambah == "Y" or tambah == "y":
                continue
            else:
                print("")
                print("KERJA YANG BENER!!")
                print("")
        elif jenisPotong == "S" or jenisPotong == "s":
            potong = int(input("Berapa Potong? : "))
            jenisPotong = "Sayap"
            hargaSatuan = 9000
            jumlahPotong = hargaSatuan * potong
            dataPotong.append(int(potong))
            dataJenis.append(jenisPotong)
            dataHarga.append(int(hargaSatuan))
            dataJumlah.append(int(jumlahPotong))
            tambah = str(input("Pesan Lagi? [Y/N] : "))
            if tambah == "N" or tambah == "n":
                break
            elif tambah == "Y" or tambah == "y":
                continue
            else:
                print("")
                print("KERJA YANG BENER!!")
                print("")
        elif jenisPotong == "P" or jenisPotong == "p":
            potong = int(input("Berapa Potong? : "))
            jenisPotong = "Paha Atas"
            hargaSatuan = 9000
            jumlahPotong = hargaSatuan * potong
            dataPotong.append(int(potong))
            dataJenis.append(jenisPotong)
            dataHarga.append(int(hargaSatuan))
            dataJumlah.append(int(jumlahPotong))
            tambah = str(input("Pesan Lagi? [Y/N] : "))
            if tambah == "N" or tambah == "n":
                break
            elif tambah == "Y" or tambah == "y":
                continue
            else:
                print("")
                print("KERJA YANG BENER!!")
                print("")
        else:
            print(line)
            print("\nKERJA YANG FOKUS, ULANG LAGI!!\n")
            print(line)
elif main == "R" or main == "r":
    match set_option:
        case "posix": os.system("clear")
        case "nt": os.system("cls")
    print(dashboardR)
    print("")
    print(line)
    print("PROGRAM SEDANG DALAM PERKEMBANGAN")
    print(line)
else:
    match set_option:
        case "posix": os.system("clear")
        case "nt": os.system("cls")
    print("KERJA GA BENER GW PECAT!") 

#Hasil Akhir
match set_option:
    case "posix": os.system("clear")
    case "nt": os.system("cls")
print(dashboardR)
print("")
print(line)
print("| {:<18}{:<20}{:<18}{:<20}{:<20} |".format("No","Bagian", "H. Satuan", "Kuantitas", "Jumlah"))
print(line)

for i in range(len(dataJenis)):
    print("| {:<18}{:<20}{:<18}{:<20}{:<20} |".format(i + 1,dataJenis[i], dataHarga[i], dataPotong[i], dataJumlah[i]))
print(line)

#Perhitungan Akhir
hargaAkhir = sum(dataJumlah)
pajak = int(hargaAkhir * 0.1)
total = hargaAkhir + pajak
print("")
print(f"Harga Akhir Ayam : {hargaAkhir}")
print(f"Jumlah Pajak : {pajak}")
print(f"Harga Keseluruhan : {total}")
print(line)
print("")
bayar = int(input("Nominal yang dibayarkan : "))
kembali = bayar - total
print(f"Kembalian Pembeli : {kembali}")
print("")
print("{:^100}".format("terimakasih".upper()))
print(line)
print("") 