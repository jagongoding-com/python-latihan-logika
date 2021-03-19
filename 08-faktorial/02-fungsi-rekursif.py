n = int(input('Masukkan nilai n: '))

def hitung_faktorial (n):
  if n > 2:
    return n * hitung_faktorial(n - 1)

  return 2

faktorial = hitung_faktorial(n)
print(f'{n}! = {faktorial}')
