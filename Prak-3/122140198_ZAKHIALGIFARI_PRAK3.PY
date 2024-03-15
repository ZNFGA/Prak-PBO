class Dagangan:
    jumlah_barang = 0
    list_barang = []

    def __init__(self, nama, stok, harga):
        self.nama = nama
        self.stok = stok
        self.harga = harga
        Dagangan.jumlah_barang += 1
        Dagangan.list_barang.append((nama, stok, harga))

    @classmethod
    def lihat_barang(cls):
        print(f"Jumlah barang dagangan pada toko: {cls.jumlah_barang} buah")
        for i, data_barang in enumerate(cls.list_barang, start=1):
            nama, stok, harga = data_barang
            print(f"{i}. {nama} seharga Rp {harga} (stok: {stok})")

    def ubah_stok(self, stok_baru):
        self.stok = stok_baru
        return self.stok

    def hapus_dari_toko(self):
        for i, barang in enumerate(Dagangan.list_barang):
            if barang[0] == self.nama:
                del Dagangan.list_barang[i]
                Dagangan.jumlah_barang -= 1
                print(f"{self.nama} dihapus dari toko!")
                break

    def __del__(self):
        self.hapus_dari_toko()


# Contoh penggunaan
Dagangan1 = Dagangan("Galon Aqua 19L", 32, 17000)
Dagangan2 = Dagangan("Gas LPG 5 kg", 22, 88000)
Dagangan3 = Dagangan("Beras Ramos 5 kg", 13, 68000)

Dagangan.lihat_barang()

del Dagangan1

Dagangan.lihat_barang()

del Dagangan2
del Dagangan3
