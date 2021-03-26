teks = input('Ketik sesuatu: ')
pengganti = input('Masukkan pengganti huruf vokal: ')

teks = teks.replace('a', pengganti)
teks = teks.replace('i', pengganti)
teks = teks.replace('u', pengganti)
teks = teks.replace('e', pengganti)
teks = teks.replace('o', pengganti)

print(f'\n{teks}')