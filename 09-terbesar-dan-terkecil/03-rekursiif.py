def nilai_maksimal (list):
  nilai_terbesar = list[0]

  # print(f'{list} -> {nilai_terbesar}')

  if len(list) > 1:
    # proses rekursif
    next_nilai_terbesar = nilai_maksimal(list[1:])

    if next_nilai_terbesar > nilai_terbesar:
      nilai_terbesar = next_nilai_terbesar

  # print(f'{list} -> {nilai_terbesar}')

  return nilai_terbesar

def nilai_minimal (list):
  nilai_terkecil = list[0]

  # print(f'{list} -> {nilai_terkecil}')

  if len(list) > 1:
    # proses rekursif
    next_nilai_terkecil = nilai_minimal(list[1:])

    if next_nilai_terkecil < nilai_terkecil:
      nilai_terkecil = next_nilai_terkecil

  # print(f'{list} -> {nilai_terkecil}')

  return nilai_terkecil

a = [3, 20, 100, -35, 50]
print(a)
print('Nilai terbesar:', nilai_maksimal(a))
print('Nilai terbesar:', nilai_minimal(a))