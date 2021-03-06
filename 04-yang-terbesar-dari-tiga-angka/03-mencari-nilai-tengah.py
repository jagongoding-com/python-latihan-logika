a, b, c = (
  int(input('Masukkan nilai a: ')),
  int(input('Masukkan nilai b: ')),
  int(input('Masukkan nilai c: '))
)

if (a > b and a < c) or (a < b and a > c):
  print('A adalah nilai tengah')
elif (b > a and b < c) or  (b < a and b > c):
  print('B adalah nilai tengah')
else:
  print('C adalah nilai tengah')
  