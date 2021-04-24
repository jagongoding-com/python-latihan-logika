import statistics

# data = [7, 12, 3, 9, 4, 7]
data = [90, 84, 88, 83, 87, 85, 83, 71]

rerata = statistics.mean(data)

# versi perulangan
# list_varian = []
# for bilangan in data:
#   list_varian.append(
#     (bilangan - rerata) ** 2
#   )

# versi satu baris
list_varian = [(bilangan - rerata) ** 2 for bilangan in data]
varian = sum(list_varian) / (len(data) - 1)

simpangan_baku = statistics.sqrt(varian)

print(f'data \t\t -> {data}')
print(f'simpangan baku \t -> {simpangan_baku}')