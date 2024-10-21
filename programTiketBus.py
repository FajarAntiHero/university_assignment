#Variable Global
line = "-" * 52
title_struct = "{:^52}".format("penjualan tiket bus".upper())
title_bus = "{:^52}".format("xyz".upper())

#Input Struct
print(line)
print(title_struct)
print(title_bus)
print(line)
name = input("Input Nama Pembeli : ")
telp = input("Input No. Handphone : ")
jurusan = input("Input Jurusan [SBY/BL/LMP] : ")

#Expression After Choose Jurusan /Progress 1
if jurusan == "SBY" or jurusan == "sby":
    namaJurusan = "Surabaya"
    harga = 300000
elif jurusan == "BL" or jurusan == "bl":
    namaJurusan = "Bali"
    harga = 350000
elif jurusan == "LMP" or jurusan == "lmp":
    namaJurusan = "Lampung"
    harga = 500000
else:
    namaJurusan = "YOU STUPID"
    harga = 0

#Expression After Choose Jumlah/ Progress 2
jumlah = int(input("Masukkan Jumlah Beli : "))
if jumlah >= 3:
    potongan = int((jumlah*harga)*0.1)
else:
    potongan = 0

total = (jumlah*harga) - potongan

#Expression Before Payment / Progress 3
print(line)
print("Nama Pembeli : " +str(name))
print("No. Handphone : " +str(telp))
print("Kode Jurusan Yang Dipilih : " +str(jurusan)) 
print("Nama Kota Tujuan : " +str(namaJurusan))
print("Harga : " +str(harga))
print("Jumlah Beli : " +str(jumlah))
print("Potongan Yang didapat : " +str(potongan))
print("Total Bayar : " +str(total))
print(line)

#Expression for payment / Progress 4
bayar = int(input("Masukkan Uang Bayar : "))
if bayar >= harga:
    uangKembali = bayar-total
else:
    uangKembali = 0
print("Total Uang Kembali : " +str(uangKembali))

#Output Struct
outputPrint = input("Print Struk Pembelian? [YES/NO] : ")

if outputPrint == "YES" or outputPrint == "yes":
    print(line)
    print(title_struct)
    print(title_bus)
    print(line)
    print("Nama Pembeli : " +str(name))
    print("No. Handphone : " +str(telp))
    print("Kode Jurusan Yang Dipilih : " +str(jurusan)) 
    print("Nama Kota Tujuan : " +str(namaJurusan))
    print("Harga : " +str(harga))
    print("Jumlah Beli : " +str(jumlah))
    print(line)
    print("Potongan Yang didapat : " +str(potongan))
    print("Total Bayar : " +str(total))
    print("Uang Bayar : " +str(bayar))
    print("Uang Kembali : " +str(uangKembali))
    print(line)
else:
    print(line)
    print("thank you".upper())
    print("i wish you in hell nigga".upper())
    print(line)
