a, b, c = (
  int(input('Masukkan nilai a: ')),
  int(input('Masukkan nilai b: ')),
  int(input('Masukkan nilai c: '))
)

if (b > a > c) or (c > a > b):
  print('A adalah nilai tengah')
elif (a > b > c) or  (c > b > a):
  print('B adalah nilai tengah')
else:
  print('C adalah nilai tengah')
  