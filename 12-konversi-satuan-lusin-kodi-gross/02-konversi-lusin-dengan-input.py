jumlah_barang = int(input('Masukkan jumlah barang; '))

satuan_lusin = jumlah_barang / 12

# konversi x.0 menjadi x
if satuan_lusin % 1 == 0:
  satuan_lusin = int(satuan_lusin)

print(f'{jumlah_barang} = {satuan_lusin} lusin')
