bilangan = int(input('Masukkan bilangan: '))
pangkat = int(input('Masukkan pangkat: '))

hasil = bilangan

for i in range(pangkat - 1):
  hasil *= bilangan

print(hasil)
