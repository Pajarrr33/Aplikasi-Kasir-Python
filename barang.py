class list_barang:
    # list [nomor_id, nama_produk, harga]
    # range random 898000000000-899800000000
    list = [
        [893814795871,'Mie Instan', 2000,'Makanan',123], 
        [893317772299,'Minyak Goreng', 12000,'Sembako',123],
        [891661637357,'Sabun', 1500,'Kosmetik',123], 
        [893893929999,'Tepung Terigu', 7000,'Sembako',123],
        [893279211041,'Tepung Maizena', 8000,'Sembako',123],
        [890542936532,'Tepung Beras', 6000,'Sembako',123],
        [888817056135,'Telur Ayam', 20000,'Hewani',123], 
        [895576475144,'Telur Bebek', 21000,'Hewani',123],
        [888244474674,'Telur Asin', 3000,'Hewani',123],
        [888658144992,'Air Mineral L', 10000,'Sembako',123],
        [892227935562,'Air Mineral M', 6000,'Sembako',123],
        [888111558814,'Air Mineral S', 3000,'Sembako',123],
        [896461272156,'Buku Tulis', 1500,'Alat Tulis',123],
        [893030280149,'Sampo Saset', 1000,'Kosmetik',123],
        [891847933160,'Sampo Botol', 9000,'Kosmetik',123],
        [891903686090,'Pengaris Plastik', 1000,'Alat Tulis',123],
        [895483399483,'Pengaris Metal', 5000,'Alat Tulis',123],
        [897779460340,'Roti', 1000,'Makanan',123],
        [893700966595,'Pasta Gigi S', 2500,'Kebutuhan Sehari-Hari',123],
        [891662091438,'Pasta Gigi M', 5000,'Kebutuhan Sehari-Hari',123],
        [892920719459,'Pasta Gigi L', 8000,'Kebutuhan Sehari-Hari',123],
        [895471550796,'Lanting S', 5000,'Kebutuhan Sehari-Hari',123],
        [890216600245,'Lanting M', 9000,'Kebutuhan Sehari-Hari',123],
        [892683501623,'Lanting L', 15000,'Kebutuhan Sehari-Hari',123],
        [896501141509,'Keripik S', 6000,'Makanan',123],
        [897238282110,'Keripik M', 10000,'Makanan',123],
        [897862254807,'Keripik L', 16000,'Makanan',123],
        [895433283732,'Popok Bayi S', 3000,'Kebutuhan Sehari-Hari',123],
        [892074736219,'Popok Bayi M', 150000,'Kebutuhan Sehari-Hari',123],
        [892074736219,'Popok Bayi M', 150000,'Kebutuhan Sehari-Hari',123],
        [888031051256,'Matrai 10.000', 11500,'Kebutuhan Sehari-Hari',123],
        [888031051256,'Matrai 6.000', 7500,'Kebutuhan Sehari-Hari',123],
    ]
def cari(input, list_yg_dicari = list_barang.list,printIndex = False):
    for i,x in enumerate(list_yg_dicari):
        if (str(x[0]) == input) or (x[1] == input) : 
            if(printIndex):
                return [i,x]
            return x
    return False

def tambah(id_produk,nama_produk,harga,kategori,stock):

    for item in list_barang.list:
         if item[1] == nama_produk:
            print("Terdapat Produk dengan nama yang sama,silahkan coba lagi dengan nama berbeda!")
            return False

    barang_baru = [id_produk,nama_produk,harga,kategori,stock]

    list_barang.list.append(barang_baru)
    print("Barang Berhasil ditambahkan")
    print("="*30)
    return True

def tambah_stock(nama_produk):
    for item in list_barang.list:
         if item[1] == nama_produk:
            print("="*30)
            print("ID barang :" , item[0])
            print("Nama Barang :" , item[1])
            print("Harga Barang :" , item[2])
            print("Kategori Barang :" , item[3])
            print("Stock :" , item[4])
            print("="*30)
            TambahStock = int(float(input("Masukan Jumlah Stock Yang ingin anda tambahkan :")))
            item[4] += TambahStock
            print("Stock Berhasil Ditambahkan")
            print("="*30)
            return True



def kurangstock(x):
    for item in list_barang.list:
        if item[1] == x[1]:
            item = x
            return True
        


