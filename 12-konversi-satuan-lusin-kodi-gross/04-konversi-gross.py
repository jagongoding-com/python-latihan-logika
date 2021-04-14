jumlah_barang = 216
jumlah_barang_dalam_gross = jumlah_barang / 144

# konversi x.0 menjadi x
if jumlah_barang_dalam_gross % 1 == 0:
  jumlah_barang_dalam_gross = int(jumlah_barang_dalam_gross)

print(f'{jumlah_barang} = {jumlah_barang_dalam_gross} gross')