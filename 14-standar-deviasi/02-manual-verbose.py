import statistics

data = [90, 84, 88, 83, 87, 85, 83, 71]


print(data)

print('\n===== Hitung Rata-Rata =====')

rerata = statistics.mean(data)
print(f"rerata = ({' + '.join(f'{x}' for x in data)}) / {len(data)}")
print(f'rerata = {rerata}')

print('\n===== Hitung varian =====')

# varian = [(bilangan - rerata) ** 2 for bilangan in data]

# mode verbose
list_varian = []
for bilangan in data:
  item = (bilangan - rerata) ** 2
  list_varian.append(item)

  print(f'({bilangan} - {rerata}) ^ 2 = {item}')

varian = sum(list_varian) / (len(data) - 1)

print('\ntotal =', ' + '.join(f'{item}' for item in list_varian))
print('total =', sum(list_varian))

print(f'\nvarian = {sum(list_varian)} / ({len(data) - 1})')
print(f'varian = {varian}')

simpangan_baku = statistics.sqrt(varian)
print('\n===== Simpangan Baku =====')
print('s = akar kuadrat dari varian')
print(f's = akar kuadrat({varian})')
print(f's = {simpangan_baku}')
# print(statistics.stdev(data))
