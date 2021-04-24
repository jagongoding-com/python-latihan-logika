import statistics

# data = [7, 12, 3, 9, 4, 7]
data = [86,87,88,86,87,85,86]

rerata = statistics.mean(data)
varian = [(bilangan - rerata) ** 2 for bilangan in data]

# for bilangan in data:
#   varian.append(
#     (bilangan - rerata) ** 2
#   )

simpangan_baku = statistics.sqrt(statistics.mean(varian))
print(simpangan_baku)