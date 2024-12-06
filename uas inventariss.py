import csv
class Inventaris:
    def __init__(self):
        self.stok = {}
        self.penjualan = []

    def tamabah_barang(self, nama_barang, jumlah, harga):
        if nama_barang in self.stok:
            self.stok[nama_barang] ['jumlah'] += jumlah
        else:
            self.stok[nama_barang] = {'jumlah': jumlah, 'harga': harga}
            print(f"{jumlah} {nama_barang} berhasil ditambahkan.")

    def kurangi_barang(self, nama_barang, jumlah):
        if nama_barang in self.stok and self.stok[nama_barang]['jumlah'] >= jumlah:
            self.stok[nama_barang]['jumlah'] -= jumlah
            self.penjualan.append((nama_barang, jumlah, self.stok[nama_barang]['harga']))
            print(f"{jumlah} {nama_barang} berhasil dijual.")
        else:
            print("stok tidak cukup atau barang tidak ada.")

    def peringatan_stok_rendah(self, batas):
        for barang, info in self.stok.items():
            if info['jumlah'] < batas:
                print(f"peringatan: stok {barang} rendah!")
        
    def hitung_total_nilai(self):
        total_nilai = sum(info['jumlah'] *info['harga'] for info in self.stok.values())
        return total_nilai 
        
    def laporan_penjualan(self):
        print("\nLaporan Penjualan:")
        for nama_barang, jumlah, harga in self.penjualan:
            print("f{nama_barang}: {jumlah} unit, Harga per unit: {harga}")
            

def main():
     inventaris = Inventaris()

     while True:
        print("\nMenu:")
        print("1. Tambah Barang")
        print("2. Kurang Barang")
        print("3. Peringatan Stok Rendah")
        print("4. Hitung Total Nilai Barang")
        print("5. Laporan Penjualan")
        print("7. Keluar")

        pilihan = input("Pilih menu (1-7): ")

        if pilihan == '1':
            nama_barang = input("Masukkan nama barang: ")
            jumlah = int(input("Masukkan jumlah barang: "))
            harga = float(input("Masukkan harga per unit: "))
            inventaris.tamabah_barang(nama_barang, jumlah, harga)
            
        elif pilihan == '2':
            nama_barang = input("Masukkan nama barang: ")
            jumlah = int(input("Masukkan jumlah yang dijual: '"))
            inventaris.kurangi_barang(nama_barang, jumlah)

        elif pilihan == '3':
            batas = int(input("Masukkan batas stok rendah: "))
            inventaris.peringatan_stok_rendah(batas)

        elif pilihan == '4':
            total_nilai = inventaris.hitung_total_nilai()
            print(f"Total nilai barang dalam inventaris: {total_nilai}")

        elif pilihan == '5':
            inventaris.laporan_penjualan()

        elif pilihan == '6':
            print("Keluar dari program.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
        


        
            
