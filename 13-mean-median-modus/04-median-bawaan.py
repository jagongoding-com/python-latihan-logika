import statistics

inputan = input('Masukkan deret bilangan (pisahkan dengan koma): ')
data = []

# konversi inputan ke dalam list yg berisi integer
for bilangan in inputan.split(','):
    data.append(int(bilangan))

median = statistics.median(data)
print(f'Data -> {data}')
print(f'Median -> {median}')
