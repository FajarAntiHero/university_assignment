import os

class garis:
    
    def satuGaris(panjang_garis: int) -> str:
        garis = "-"*panjang_garis
        print(garis)
    def duaGaris(panjang_garis: int) -> str:
        garis = "="*panjang_garis
        print(garis)

def mainTitle(nameTitle : str) -> str:
    print("{:^100}".format(nameTitle.upper()))

def tableTitle(no: str, name:str, data:str):
    print("||{:^4}||{:^40}||{:^50}||".format(no.upper(), name.upper(), data.upper() ))

def clearTerminal() -> None:
    sistem_operasi = os.name
    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")
    
def inputMode() -> str:
    while True:
        try:
            mode = str(input("Masukkan Mode Perhitungan [OUT/IN]: "))
            if mode == "out" or mode == "OUT" or mode == "o" or mode == "O":
                hasil = "out"
                return hasil
            elif mode == "in" or mode == "IN" or mode == "i" or mode == "I":
                hasil = "in"
                return hasil
            else:
                print("Mode tidak tersedia! Mohon Diulang")
        except:
            print("Mode harus berupa huruf!! Mohon Diulang!")

def saldoAwal() -> int:
    while True:
        try:
            saldo = int(input("Masukkan jumlah saldo awal : "))
            return saldo
        except:
            print("Saldo Harus dalam bentuk angka!! Mohon ulangi")

def next():
    while True:
        inputNext = str(input("Lanjut [Y] : "))
        if inputNext == "Y" or inputNext == "y" or inputNext == "yes" or inputNext == "YES":
            nilai = "lanjut"
            return nilai
        elif inputNext == "N" or inputNext == "n" or inputNext == "no" or inputNext == "NO":
            nilai = "berhenti"
            return nilai
        else:
            print("Input tidak sesuai. Ulangi!")       

def countOut() -> str:
    clearTerminal()
    line = garis
    line.duaGaris(100)
    mainTitle("menghitung pengeluaran")
    line.duaGaris(100)
    print("")
    saldo = saldoAwal()

    dataNilaiPengeluaran = []
    dataNamaPengeluaran = []

    while True:
        try: 
            NamaPengeluaran = str(input("Nama Pengeluaran : "))
            nilaiPengeluarn = int(input("Masukkan nominal pengeluaran :"))
            dataNamaPengeluaran.append(NamaPengeluaran)
            dataNilaiPengeluaran.append(nilaiPengeluarn)
            line.satuGaris(100)
            proses = next()
            line.satuGaris(100)
            if proses == "berhenti":
                break
        except:
            print("Input yang dimasukkan tidak sesuai")

    clearTerminal()
    line.duaGaris(100)
    tableTitle("no", "nama pengeluaran", "nilai pengeluaran")
    line.duaGaris(100)
    for i in range(len(dataNilaiPengeluaran)):
        print("||{:^4}||{:^40}||{:^50}||".format(i+1, dataNamaPengeluaran[i], dataNilaiPengeluaran[i] ))
    line.satuGaris(100)
    print(f"Saldo awal anda : {saldo}")
    for i in range(len(dataNilaiPengeluaran)):
        saldoAkhir = saldo - dataNilaiPengeluaran[i]
        
    print(f"Saldo Tersisa : {saldoAkhir}")

    line.duaGaris(100)




