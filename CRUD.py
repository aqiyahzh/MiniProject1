class TokoATK:
    def __init__(self):
        self.barang = []

    def tambah(self, produk):
        self.barang.append(produk)
        print(f"Produk '{produk['Nama Produk']}' sudah ditambahkan nihh")

    def tampil(self):
        if not self.barang:
            print("Belum ada produk yang ditambahkan.")
        else:
            print("Daftar produk yang tersedia:")
            for idx, produk in enumerate(self.barang, start=1):
                print(f"{idx}. {produk['Nama Produk']} | Harga: {produk['Harga']} | Stok: {produk['Stok']} | Kategori: {produk['Kategori']} | ID: {produk['ID']}")

    def perbaharui(self, index, updated):
        if 1 <= index <= len(self.barang):
            self.barang[index - 1] = updated
            print(f"Produk '{updated['Nama Produk']}' sudah diperbaharui.")
        else:
            print("Index produk yang anda masukkan salah.")

    def hapus(self, index):
        if 1 <= index <= len(self.barang):
            delete = self.barang.pop(index - 1)
            print(f"Produk '{delete['Nama Produk']}' berhasil dihapus.")
        else:
            print("Index produk yang anda masukkan salah.")

def menu():
    print('''
        Program Pendataan Barang Toko Alat Tulis 
        by: Aqiyah Zulqiyah (2309116075)
        ''')
    print('[1] Tampil Data')
    print('[2] Tambah Data')
    print('[3] Edit Data')
    print('[4] Hapus Data')
    print('[5] Keluar')
    print('')

toko = TokoATK()

while True:
    menu()
    kode = input('Masukkan Pilihan Anda: ')

    if kode == '1':
        toko.tampil()

    elif kode == '2':
        nama_barang = input("Masukkan nama produk: ")
        harga_barang = float(input("Masukkan harga produk: Rp. "))
        stok_barang = int(input("Masukkan stok produk: "))
        kategori_barang = input("Masukkan kategori produk: ")
        id_barang = input("Masukkan ID produk: ")
        
        barang_baru = {'Nama Produk': nama_barang, 'Harga': harga_barang, 'Stok': stok_barang, 'Kategori': kategori_barang, 'ID': id_barang}
        toko.tambah(barang_baru)

    elif kode == '3':
        toko.tampil()
        index = int(input("Masukkan index produk yang ingin diedit: "))
        nama_baru = input("Masukkan nama produk yang baru: ")
        harga_baru = float(input("Masukkan harga produk yang baru: Rp. "))
        stok_baru = int(input("Masukkan stok produk yang terbaru: "))
        edit_kategori = input("Masukkan kategori produk yang baru: ")
        id_baru = input("Masukkan ID Produk yang baru: ")
        barang_baru = {'Nama Produk': nama_baru, 'Harga': harga_baru, 'Stok': stok_baru, 'Kategori': edit_kategori, 'ID': id_baru}
        toko.perbaharui(index, barang_baru)

    elif kode == '4':
        toko.tampil()
        index = int(input("Masukkan index produk yang ingin dihapus: "))
        toko.hapus(index)

    elif kode == '5':
        print("Terima kasih! Anda telah keluar dari program.")
        break

    else:
        print('Kode yang anda masukkan tidak jelas. Tolong masukkan angka 1-5 saja jangan aneh-aneh :)')
