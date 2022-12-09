# Kalkulator Sederhana
# Oleh Febry Billiyagi Karsidi - TI 02

angka_pertama = int(input("Angka Pertama: "))
angka_kedua = int(input("Angka Kedua: "))
operator = int(input('''
Pilih Operator :
1. Penjumlahan
2. Pengurangan
3. Perkalian
4. Pembagian
5. Perpangkatan

Pilih no dari operasi diatas: '''))

if operator == 1:
    hasil = angka_pertama + angka_kedua
    operator = ['+', 'Penjumlahan']
elif operator == 2:
    hasil = angka_pertama - angka_kedua
    operator = ['-', 'Pengurangan']
elif operator == 3:
    hasil = angka_pertama * angka_kedua
    operator = ['x', 'Perkalian']
elif operator == 4:
    hasil = angka_pertama / angka_kedua
    operator = [':', 'Pembagian']
elif operator == 5:
    hasil = angka_pertama ** angka_kedua
    operator = ['**', 'Perpangkatan']
else :
    print("Aksi gagal, mohon coba kembali")
    exit()

print('Angka Pertama: ' + str(angka_pertama), '\n',
    'Angka Kedua: ' + str(angka_kedua), '\n',
    'Pilihan Operator : ' + operator[1], '\n',
    'Hasil Operator : ' + str(angka_pertama), operator[0], str(angka_kedua) + ' = ' + str(hasil) )