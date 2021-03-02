panjang = int(input('Masukkan panjang deret: '))

angka1, angka2 = 0, 1

for i in range(panjang):
  if (i < 2):
    print(i, end=' ')
  else:
    angkaSekarang = angka1 + angka2
    print(angkaSekarang, end=' ')
    
    # update 2 variabel bantuan
    angka1 = angka2
    angka2 = angkaSekarang
    