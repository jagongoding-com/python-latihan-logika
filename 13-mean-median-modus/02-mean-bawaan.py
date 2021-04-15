import statistics

inputan = input('Masukkan deret bilangan (pisahkan dengan koma): ')
data = []

# konversi inputan ke dalam list yg berisi integer
for bilangan in inputan.split(','):
    data.append(int(bilangan))

rerata = statistics.mean(data)
print(f'Data -> {data}')
print(f'Mean -> {rerata}')