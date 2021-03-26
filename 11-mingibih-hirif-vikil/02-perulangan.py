teks = input('Ketik sesuatu: ')
pengganti = input('Masukkan pengganti huruf vokal: ')

for huruf in 'aiueo':
  teks = teks.replace(huruf, pengganti)

print(f'\n{teks}')