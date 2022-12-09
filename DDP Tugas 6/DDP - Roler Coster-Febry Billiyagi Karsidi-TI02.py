# Program Penghitung Tinggi badan untuk persyaratan bermain Roler Coaster
# Febry Billiyagi Karsidi - TI02

name = input('Nama: ')
age = int(input('Usia: '))
height = int(input('Tinggi Badan: '))

result_height = "Memenuhi Kriteria" if height > 90 else "Belum cukup tinggi, mohon kembali lagi nanti"

print('================================')
print('Nama     : ' + name, '\n', 'Usia     : ' + str(age), '\n', 'Tinggi badan     :' + str(height) + " CM", '\n', 'Ket: ' + result_height)
print('================================')

