teks = input('Ketik sesuatu: ')
pengganti = input('Masukkan pengganti huruf vokal: ')

for huruf in 'aiueoAIUEO':
  teks = teks.replace(huruf, pengganti)

print(f'\n{teks}')