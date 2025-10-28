# Program Penjualan Susu
print("=== Sistem Penjualan Susu ===")

# Input data dari pengguna
kode = int(input("Masukkan kode susu (1-3): "))
jumlah = int(input("Masukkan jumlah pembelian: "))
ukuran = input("Masukkan ukuran (B/S/K): ").upper()

# Inisialisasi variabel
nama = ""
harga = 0

# Logika berdasarkan kode susu dan ukuran
if kode == 1:  # Dancow
    nama = "Dancow"
    if ukuran == "B":
        harga = 10000
    elif ukuran == "S":
        harga = 4250
    elif ukuran == "K":
        harga = 2100
    else:
        print("Ukuran tidak valid!")

elif kode == 2:  # Indomilk
    nama = "Indomilk"
    if ukuran == "B":
        harga = 8500
    elif ukuran == "S":
        harga = 4000
    elif ukuran == "K":
        harga = 2025
    else:
        print("Ukuran tidak valid!")

elif kode == 3:  # Sustacal
    nama = "Sustacal"
    if ukuran == "B":
        harga = 17000
    elif ukuran == "S":
        harga = 14500
    elif ukuran == "K":
        harga = 8300
    else:
        print("Ukuran tidak valid!")

else:
    print("Kode susu tidak valid!")

# Hitung total harga (hanya jika kode & ukuran valid)
if harga > 0:
    total = harga * jumlah
    print("\n=== Detail Pembelian ===")
    print("Nama susu       :", nama)
    print("Ukuran          :", ukuran)
    print("Harga satuan    : Rp", harga)
    print("Jumlah beli     :", jumlah)
    print("Total harga     : Rp", total)
