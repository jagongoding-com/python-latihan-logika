def apakah_kabisat (tahun):
  habis_dibagi_400 = tahun % 400 == 0
  habis_dibagi_100 = tahun % 100 == 0
  habis_dibagi_4 = tahun % 4 == 0

  if habis_dibagi_400 or (habis_dibagi_4 and not habis_dibagi_100):
    print(f'{tahun} tahun kabisat')
  else:
    print(f'{tahun} bukan tahun kabisat')

apakah_kabisat(1600)
apakah_kabisat(1900)
apakah_kabisat(1904)
apakah_kabisat(2000)
apakah_kabisat(2004)
apakah_kabisat(2005)
apakah_kabisat(2006)
apakah_kabisat(2008)
apakah_kabisat(2013)