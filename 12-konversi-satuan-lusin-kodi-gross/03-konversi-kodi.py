jumlah_barang = 60
jumlah_barang_dalam_kodi = jumlah_barang / 20

# konversi x.0 menjadi x
if jumlah_barang_dalam_kodi % 1 == 0:
  jumlah_barang_dalam_kodi = int(jumlah_barang_dalam_kodi)

print(f'{jumlah_barang} = {jumlah_barang_dalam_kodi} kodi')