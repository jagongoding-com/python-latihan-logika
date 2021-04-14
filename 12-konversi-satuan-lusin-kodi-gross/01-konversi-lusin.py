jumlah_barang = 24
jumlah_barang_dalam_lusin = jumlah_barang / 12

# konversi x.0 menjadi x
if jumlah_barang_dalam_lusin % 1 == 0:
  jumlah_barang_dalam_lusin = int(jumlah_barang_dalam_lusin)

print(f'{jumlah_barang} = {jumlah_barang_dalam_lusin} lusin')