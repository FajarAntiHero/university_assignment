import os as os

def seratusRibu(n):
    seratusRibu = int(n / 100000) 
    n = jumlahUang - (seratusRibu*100000)
    print(f"Jumlah Pecahan Uang : {int(seratusRibu)} lembar Seratus Ribu ")
    return n

def limaPuluh(n):
    limaPuluh = int(n / 50000)
    n = jumlahUang - (limaPuluh*50000)
    print(f"Jumlah Pecahan Uang : {int(limaPuluh)} lembar Lima Puluh Ribu ")
    return n

def duaPuluh(n):
    duaPuluh = int(n / 20000)
    n = jumlahUang - (duaPuluh*20000)
    print(f"Jumlah Pecahan Uang : {int(duaPuluh)} lembar Dua Puluh Ribu ")
    return n

def sepuluhRibu(n):
    sepuluhRibu = int(n / 10000)
    n = jumlahUang - (sepuluhRibu*10000)
    print(f"Jumlah Pecahan Uang : {int(sepuluhRibu)} lembar Sepuluh Ribu ")
    return n

def limaRibu(n):
    limaRibu = int(n / 5000)
    n = jumlahUang - (limaRibu*5000)
    print(f"Jumlah Pecahan Uang : {int(limaRibu)} lembar Lima Ribu ")
    return n

def duaRibu(n):
    duaRibu = int(n / 2000)
    n = jumlahUang - (duaRibu*2000)
    print(f"Jumlah Pecahan Uang : {int(duaRibu)} lembar Dua Ribu ")
    return n

def seribu(n):
    seribu = int(n / 1000)
    n = jumlahUang - (seribu*1000)
    print(f"Jumlah Pecahan Uang : {int(seribu)} lembar Seribu ")
    return n

while True:
    sistem_operasi = os.name
    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")

    print(" AYO PECAHIN UANG \n")
    jumlahUang = int(input("Masukkan Jumlah Uang (IDR) : "))
    print("\n")

    print("======= DASHBOARD =======")
    print(" 100000  | 50000 | 20000 ")
    print(" 10000   | 5000  | 2000 ")
    print(" 1000    |       | \n")
    pecahan = str(input("Mau dipecah oleh Nominal Uang apa? "))
    print("=========================================================================== \n")

    if pecahan  == "100000":
        hasil = seratusRibu(jumlahUang)
        jumlahUang = int(hasil)
    elif pecahan == "50000":
        hasil = limaPuluh(jumlahUang)
        jumlahUang = int(hasil)
    elif pecahan == "20000":
        hasil = duaPuluh(jumlahUang)
        jumlahUang = int(hasil)
    elif pecahan == "10000":
        hasil = sepuluhRibu(jumlahUang)
        jumlahUang = int(hasil)
    elif pecahan == "5000":
        hasil = limaRibu(jumlahUang)
        jumlahUang = int(hasil)
    elif pecahan == "2000":
        hasil = duaRibu(jumlahUang)
        jumlahUang = int(hasil)
    elif pecahan == "1000":
        hasil = seribu(jumlahUang)
        jumlahUang = int(hasil)

    print(f"Sisa uang anda setelah dipecah adalah {jumlahUang} \n")
    hasilUang = jumlahUang
    if hasilUang != 0:
        ulang = str(input("Apakah Anda ingin melakukannya lagi? [y/n] : \n"))
        if ulang == "n" or ulang == "N":
            print(f"\n THANK YOU \n")
            break
    elif hasilUang == 0:
        print("Anda tidak Memiliki sisa Uang untuk dipecah lagi \n")
        print(f"\n THANK YOU \n")
        break
        