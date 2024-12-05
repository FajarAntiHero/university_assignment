from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk


window = tk.Tk()
window.configure(bg = "white")
window.geometry("1000x500")
window.resizable(False, False)
window.title("PROGRAM BIODATA")
frame = ttk.Frame(window)
frame.pack(padx=15, fill="x", expand=True)

background_image = Image.open("LOGO_UBSI-removebg-preview.png")  # Ganti dengan path gambar Anda
bg = ImageTk.PhotoImage(background_image)
background_label = tk.Label(frame, image=bg)
background_label.place(relwidth=1, relheight=1)  # Menutupi seluruh jendela

NAMA = tk.StringVar()
UMUR = tk.IntVar()
WARGA_NEGARA = tk.StringVar()
ALAMAT = tk.StringVar()
KODE_POS = tk.IntVar()
KOTA = tk.StringVar()
PROVINSI = tk.StringVar()
NO_TELP = tk.IntVar()
STATUS = tk.StringVar()
FAKULTAS = tk.StringVar()


def submit():
    data = [NAMA, UMUR, WARGA_NEGARA, ALAMAT, KODE_POS, KOTA, PROVINSI, NO_TELP, STATUS, FAKULTAS]
    keterangan = ["Nama", "Umur", "Kewarganegaraan", "Alamat", "Kode Pos", "Kota", "Provinsi", "Nomor Telpon", "Status", "Fakultas"]

    # Menggabungkan semua pesan menjadi satu string
    pesan = ""
    for i in range(len(data)):
        pesan += f"{keterangan[i]} : {data[i].get()}\n"  # Tambahkan newline untuk tiap data

    # Menampilkan semua data dalam satu dialog
    showinfo(title="BIODATA ANDA", message=pesan)


inputNama = ttk.Label(frame, text="Nama Anda")
inputNama.pack(padx=10, fill="x", expand=True)
inputNamaEntry = ttk.Entry(frame, textvariable=NAMA)
inputNamaEntry.pack(padx=10, fill="x", expand=True)

inputUmur = ttk.Label(frame, text="Umur Anda")
inputUmur.pack(padx=10, fill="x", expand=True)
inputUmurEntry = ttk.Entry(frame, textvariable=UMUR)
inputUmurEntry.pack(padx=10, fill="x", expand=True)

inputWargaNegara = ttk.Label(frame, text="Kewarganegaraan Anda")
inputWargaNegara.pack(padx=10, fill="x", expand=True)
inputWargaNegaraEntry = ttk.Entry(frame, textvariable=WARGA_NEGARA)
inputWargaNegaraEntry.pack(padx=10, fill="x", expand=True)

inputAlamat = ttk.Label(frame, text="Alamat Anda")
inputAlamat.pack(padx=10, fill="x", expand=True)
inputAlamatEntry = ttk.Entry(frame, textvariable=ALAMAT)
inputAlamatEntry.pack(padx=10, fill="x", expand=True)

inputKodePos = ttk.Label(frame, text="Kode Pos Anda")
inputKodePos.pack(padx=10, fill="x", expand=True)
inputKodePosEntry = ttk.Entry(frame, textvariable=KODE_POS)
inputKodePosEntry.pack(padx=10, fill="x", expand=True)

inputKota = ttk.Label(frame, text="Nama Kota Asal")
inputKota.pack(padx=10, fill="x", expand=True)
inputKotaEntry = ttk.Entry(frame, textvariable=KOTA)
inputKotaEntry.pack(padx=10, fill="x", expand=True)

inputProvinsi = ttk.Label(frame, text="Nama Provinsi Asal")
inputProvinsi.pack(padx=10, fill="x", expand=True)
inputProvinsiEntry = ttk.Entry(frame, textvariable=PROVINSI)
inputProvinsiEntry.pack(padx=10, fill="x", expand=True)

inputTelp = ttk.Label(frame, text="Nomer Telpon Anda")
inputTelp.pack(padx=10, fill="x", expand=True)
inputTelpEntry = ttk.Entry(frame, textvariable=NO_TELP)
inputTelpEntry.pack(padx=10, fill="x", expand=True)

inputstatus = ttk.Label(frame, text="Status [Dosen/Mahasiswa]")
inputstatus.pack(padx=10, fill="x", expand=True)
inputstatusEntry = ttk.Entry(frame, textvariable=STATUS)
inputstatusEntry.pack(padx=10, fill="x", expand=True)

inputFakultas = ttk.Label(frame, text="Nama Fakultas Anda")
inputFakultas.pack(padx=10, fill="x", expand=True)
inputFakultasEntry = ttk.Entry(frame, textvariable=FAKULTAS)
inputFakultasEntry.pack(padx=10, fill="x", expand=True)


# SUBMIT BUTTON
submitButton = ttk.Button(frame, text="SUBMIT",command=submit)
submitButton.pack(padx=10, pady=10, fill="x", expand=True)


window.mainloop()