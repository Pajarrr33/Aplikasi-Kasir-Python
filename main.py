# from os import system, name 
import os, locale
import barang
import lib.ui as ui
YangDibeli = []
Supplier = [
        ['Adi Sujipto',+62893120293,'Adiaja@gmail.com','Jalan Konggo Amur','Sabun']
    ]

# Bug cek_duplikasi

ui.clearCli()

def cek_duplikasi(triger):
    if int(len(YangDibeli)) > 0 :
        hasil = barang.cari(str(triger[0]),YangDibeli, True)
        if hasil:
            YangDibeli.pop(hasil[0])
            kuntitas = triger[3]
            triger.pop(3)
            kuntitas = int(kuntitas) + int(hasil[1][3])
            triger[3] = kuntitas
            return triger
    return triger

def handel_pilihan_kustom():
    dataKustom = ["===Kustom!==="]
    namaBarang = input("Apa nama barangnya?\n")
    hargaBarang = int(input("Berapa harga barangnya?\n"))
    kuantitasBarang = float(input("Berapa banyak yang dibeli?\n"))
    dataKustom.append(namaBarang)
    dataKustom.append(hargaBarang)
    dataKustom.append(kuantitasBarang)
    YangDibeli.append(dataKustom)

def handel_pilihan_basis_data():
    indeksPencarian = input("Masukan Nama Barang / ID-nya!\n")
    hasilPencarian = barang.cari(indeksPencarian)
    if hasilPencarian:
        kuantitasBarang = float(input("Berapa banyak yang dibeli?\n"))
        hasilPencarian.append(kuantitasBarang)
        YangDibeli.append(cek_duplikasi(hasilPencarian))
        # YangDibeli.append(hasilPencarian)
    else: 
        print("Maaf barang tidak terdaftar di basis data.")
        handel_pilihan_basis_data()

def cari_barang():
    print("="*30)
    indeksPencarian = input("Masukan Nama Barang / ID-nya!\n")
    hasilPencarian = barang.cari(indeksPencarian)
    if hasilPencarian:
        print("="*30)
        print("ID barang :" , hasilPencarian[0])
        print("Nama Barang :" , hasilPencarian[1])
        print("Harga Barang :" , hasilPencarian[2])
        print("Kategori Barang :" , hasilPencarian[3])
        print("Stock :" , hasilPencarian[4])
        print("="*30)
        PencarianBerulang = input("Apakah anda ingin mencari barang lagi?(y/n) :")
        if PencarianBerulang == "y" :
            cari_barang()
        else :
            ProdukBerulang = True
    else: 
        print("Maaf barang tidak terdaftar di basis data.")
        PencarianBerulang = input("Apakah anda ingin mencari barang lagi?(y/n) :")
        if PencarianBerulang == "y" :
            cari_barang()
        else :
            ProdukBerulang = True

def tambah_barang():
    print("="*30)
    print("Menu Tambah barang")
    print("="*30)

    # Get user input to add a new item
    id_produk = int(input("Masukan ID Produk : "))
    nama_produk = input("Masukan Nama Produk: ")
    harga = int(input("Masukan Harga : "))
    kategori = input("Masukan Kategori Produk : ")
    stock = int(input("Masukan Stok Produk : "))
    print("="*30)

    # Call the add_item method to add the new item to the array
    Tambah_barang = barang.tambah(id_produk,nama_produk,harga,kategori,stock)
    if Tambah_barang == True:
        BarangBerulang = input("Apakah anda ingin menambahkan barang lagi?(y/n) :")
        if BarangBerulang == "y" :
            tambah_barang()
        else :
            ProdukBerulang = True
    else :
        tambah_barang()


def penambahan_barang():
    tipeInput = input("Cari barang atau masukan kustom?\n(Cari isi 1, kustom isi 0)\n")
    if(int(tipeInput) == 1):
        handel_pilihan_basis_data()
    else: 
        handel_pilihan_kustom()
    ui.build(YangDibeli)
def tambahAkhiri():
    kataTAA = "Lanjut menambahakan barang(1) atau akhiri(0)?\n"
    tambahAtauAkhiri = int(input(kataTAA))
    while tambahAtauAkhiri == 1:
        penambahan_barang()
        tambahAtauAkhiri = int(input(kataTAA))
    if len(YangDibeli) < 1:
        utama()
    dihapus = int(input("Apa yang mau dihapus?\n(masukan 0 bila tidak ada)\n"))
    if dihapus > 0:
        YangDibeli.pop(dihapus-1)
        ui.build(YangDibeli)
        return tambahAkhiri()
    uangYgDibayar = int(input("Berapa uang yang dibayarkan?\n"))
    ui.build(YangDibeli,uangYgDibayar)
    return 0


def cek_supplier():
    CekBerulang = True
    while CekBerulang :
        print("="*30)
        print("Cek Data Supplier")
        print("="*30)

        CariNama = input("Masukan nama Supplier yang ingin anda cari :")

        Ditemukan = False

        for entry in Supplier:
            if entry[0] == CariNama:
                print("="*30)
                print("Nama Supplier:", entry[0])
                print("No Telephone:", entry[1])
                print("Email:", entry[2])
                print("Alamat:", entry[3])
                print("Supplier dari produk :", entry[4])
                Ditemukan = True
                break
                

        if Ditemukan == False :
            print("="*30)
            print("Nama Supplier tidak ditemukan")
            print("="*30)
            CekLagi = input("Cek supplier Gagal,apakah anda ingin cek lagi?(y/t)")
            if CekLagi == "y" :
                CekBerulang = True
            else :
                CekBerulang = False

        if Ditemukan == True :
            print("="*30)
            CekLagi = input("Cek supplier berhasil,apakah anda ingin cek lagi?(y/t)")
            if CekLagi == "y" :
                CekBerulang = True
            else :
                CekBerulang = False
    

def tambah_supplier():
    TambahBerulang = True
    while TambahBerulang :

        print("="*30)
        print("Tambah data supplier")
        print("="*30)

        # Get user input for the new entry
        nama = input("Masukan nama supplier: ")
        no_telphone = int(input("Masukan No Telphone supplier : "))  # Convert the input to an integer
        email = input("Masukan alamat email supplier : ")
        alamat = input("Masukan alamat supplier : ")
        produk = input("Masukan barang yang disuplai oleh supplier :")

        # Create a new entry with the user input
        new_entry = [nama,no_telphone, email, alamat, produk]

        # Append the new entry to the supplier array
        Supplier.append(new_entry)

        print("="*30)
        TambahLagi = input("Penambahan data supplier berhasil,apakah anda ingin menambahkan lagi?(y/t)")

        if TambahLagi == "y" :
            TambahBerulang = True
        else :
            TambahBerulang = False

def history_transaksi():
    def baca_transaksi_dari_file(file_name):
        transaksi = []
        with open(file_name, "r") as file:
            for line in file:
                items = line.strip().split(",")
                transaksi.append(items)
        return transaksi

    def hitung_total_pendapatan(transaksi):
        total_pendapatan = 0.0
        for item in transaksi:
            total_pendapatan += float(item[2])  # Mengambil totalBayar dari setiap transaksi
        return total_pendapatan

    file_name = "lib/transaction.txt"
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

    # Membaca data transaksi dari file
    transaksi = baca_transaksi_dari_file(file_name)

    # Menghitung total pendapatan dari transaksi
    total_pendapatan = hitung_total_pendapatan(transaksi)
    total_pendapatan_terformat = "{:,.3f}".format(total_pendapatan)

    print("="*30)
    print("Laporan Transaksi Kesuluruhan")
    print("="*30)
    # Menampilkan data transaksi
    for item in transaksi:
        print("Invoice :", item[0] , "Tanggal :" ,item[1], "Total :" ,item[2])
        print("="*30)

    print("Total Pendapatan :", total_pendapatan_terformat)


def menu():
    MenuBerulang = True
    while MenuBerulang :
        print("="*30)
        print("0. Keluar")
        print("1. Supplier")
        print("2. Produk")
        print("3. Transaksi")
        print("4. Laporan")
        print("="*30)
        Menu = int(float(input("Masukan menu yang anda inginkan : ")))
        if Menu == 0 :
            MenuBerulang = False
            Berulang = True
        if Menu == 1 :
            SupplierBerulang = True
            while SupplierBerulang :
                print("="*30)
                print("0. Keluar")
                print("1. Cek Supplier")
                print("2. Tambah Supplier")
                print("="*30)
                SupplierMenu = int(float(input("Masukan Menu yang anda inginkan :")))
                if   SupplierMenu == 0:
                        SupplierBerulang = False
                elif SupplierMenu == 1:
                    cek_supplier()
                elif SupplierMenu == 2:
                    tambah_supplier()
                else :
                    print("="*30)
                    print("Menu yang anda masukan salah silahkan coba lagi!")
                    SupplierBerulang = True


        if Menu == 2 :
            ProdukBerulang = True
            while ProdukBerulang :
                print("="*30)
                print("0. Keluar")
                print("1. Cek Barang")
                print("2. Tambah Barang")
                print("="*30)
                ProdukMenu = int(float(input("Masukan Menu yang anda inginkan :")))
                if  ProdukMenu == 0:
                        ProdukBerulang = False
                elif ProdukMenu == 1:
                    cari_barang()
                elif ProdukMenu == 2:
                    tambah_barang()
                else :
                    print("="*30)
                    print("Menu yang anda masukan salah silahkan coba lagi!")
                    SupplierBerulang = True

        if Menu == 3 :
            penambahan_barang()
            tambahAkhiri()
        if Menu == 4 :
            history_transaksi()
            Berulang = True 

def login():
    Username = "Muhammad Fauzan Ramadhan" 
    Password = 12345678 

    print("="*30)
    print("Silahkan Login Terlebih dahulu")
    print("="*30)
    UserUsername = input("Masukan Username :")
    UserPassword = int(float(input("Masukan password :")))
    if UserUsername == Username :
        if UserPassword == Password:
            menu()
        else :
            print("="*30)
            print("Password anda salah silahkan coba lagi")
    else :
        print("="*30)
        print("Username anda salah silahkan coba lagi")

            
def utama():
    print("Selamat Datang!")
    print("MESIN KASIR BASIS CLI 'CLIKAS'")
    print("Dibuat Oleh:")
    print("Kelompok 8 Tugas Besar Pengenalan Komputasi")
    print("Salsabila Widi Azzahra 16023191, Nafisa Bunga Sunarya 16023196, Muhammad Fauzan Ramadhan 16023201, Magnalia Beatifica Dei 16023206, Aurel Zalfa Prilia 16023211")
    Berulang = True
    while Berulang : 
        login()


utama()
