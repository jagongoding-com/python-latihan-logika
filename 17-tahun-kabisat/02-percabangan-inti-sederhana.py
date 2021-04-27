tahun = 1904

habis_dibagi_400 = tahun % 400 == 0
habis_dibagi_100 = tahun % 100 == 0
habis_dibagi_4 = tahun % 4 == 0

if habis_dibagi_400 or (habis_dibagi_4 and not habis_dibagi_100):
  print(f'{tahun} tahun kabisat')
else:
  print(f'{tahun} bukan tahun kabisat')