import statistics

data = [90, 84, 88, 83, 87, 85, 83, 71]

simpangan_baku = statistics.stdev(data)
simpangan_baku_populasi = statistics.pstdev(data)

print(simpangan_baku)
print(simpangan_baku_populasi)