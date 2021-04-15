def rata_rata (deret):
  return sum(deret) / len(deret)

inputan = input('Masukkan deret bilangan (pisahkan dengan koma): ')
data = []

# konversi inputan ke dalam list yg berisi integer
for bilangan in inputan.split(','):
    data.append(int(bilangan))

print(f'Data -> {data}')
print(f'Mean -> {rata_rata(data)}')