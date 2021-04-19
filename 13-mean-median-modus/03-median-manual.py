def nilai_tengah(deret):
  deret.sort()
  n = len(deret) # ambil panjang data
  i_tengah = n // 2 # dibulatkan ke bawah

  # jika n adalah ganjil
  if n % 2 == 1:
    return deret[i_tengah]

  # jika n genap
  return (deret[i_tengah - 1] + deret[i_tengah]) / 2

inputan = input('Masukkan deret bilangan (pisahkan dengan koma): ')
data = []

# konversi inputan ke dalam list yg berisi integer
for bilangan in inputan.split(','):
    data.append(int(bilangan))

print(f'Data -> {data}')
print(f'Median -> {nilai_tengah(data)}')
