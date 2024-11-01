#ASSETS
line = "="*50
title = "{:^50}".format("data nilai dasar pemrograman 17.1B.24".upper())

#DASHBOARD
print(line)
print("")
print(title)
print("")
print(line)
print("")


#Variable menyimpan data
list_nim = []
list_uts = []
list_uas = []
list_total = []

#PROGRESS 
#---INPUT---
jumlah = int(input("Masukkan Jumlah Data yang akan di input : "))
for i in range(jumlah):
    print(line)
    print("")
    print(f"Input Data ke {i+1}")
    list_nim.append(str(input("Masukkan NIM Siswa : ")))
    list_uts.append(int(input("Masukkan Nilai UTS Siswa : ")))
    list_uas.append(int(input("Masukkan Nilai UAS Siswa : ")))
    print("")
        
for j in range(jumlah):
    total_nilai = list_uts[j] + list_uas[j]
    list_total.append(int(total_nilai/2))  


#---OUTPUT---
print(line)
print("")
print(title)
print("")
print(line)
print("{:<13}{:^12}{:^12}{:^13}".format("NIM", "NILAI UTS", "NILAI UAS", "RATA RATA"))
print(line)
print("")
for x in range(jumlah):
    print("{:<13}{:^12}{:^12}{:^13}".format(list_nim[x], list_uts[x], list_uas[x], list_total[x]))
    print("")
print(line)
