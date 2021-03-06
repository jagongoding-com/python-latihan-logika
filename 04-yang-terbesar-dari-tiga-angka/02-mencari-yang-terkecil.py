a, b, c = (
  int(input('Masukkan nilai a: ')),
  int(input('Masukkan nilai b: ')),
  int(input('Masukkan nilai c: '))
)

if a < b and a < c:
  print('A yang terkecil')
elif b < a and b < c:
  print('B yang terkecil')
else:
  print('C yang terkecil')