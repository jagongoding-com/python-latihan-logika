print('Masukkan nilai awal dan nilai akhir')

nilai_awal = int(input(' nilai awal: '))
nilai_akhir = int(input(' nilai akhir: '))

print("""\nTampilkan bilangan
 1. Ganjil
 2. Genap""")

pilihan = int(input('Pilihan: '))

# periksa kalau pilihan bukan 1 dan 2
if pilihan not in [1, 2]:
  print('Pilihan salah')
else:
  for x in range(nilai_awal, nilai_akhir + 1):
    if pilihan == 1 and x % 2 == 1:
      print(x, end=' ')
    elif pilihan == 2 and x % 2 == 0:
      print(x, end=' ')
  else:
    # ganti baris ketika perulangan selesai
    print('')
