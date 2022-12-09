# Penghitung Luas & Keliling (Layang-layang & Trapesium)
# Oleh Febry Billiyagi Karsidi

nim = input("Masukkan NIM: ")

parse_nim = list(nim);

angka_terakhir = int(parse_nim[len(parse_nim) - 1]) % 2

# Layang-layang (Ganjil)
if angka_terakhir == 1:
    operasi = int(input('''pilih menu hitung Layang-layang: 
            1. Keliling
            2. Luas
            
            Pilih dari no diatas: '''))

    diagonal_kanan = int(input('Sisi Kanan: '))
    diagonal_kiri = int(input('Sisi Kiri: '))

    # Hitung keliling Layang-layang
    if operasi == 1:
        print('\n', 'Hasil: ', 2*(diagonal_kanan+diagonal_kiri))
        exit()

    # Hitung Luas Layang-layang
    elif operasi == 2:
        print('\n', 'Hasil: ', .5 * diagonal_kanan * diagonal_kiri)
        exit()
    else:
        print('operasi gagal, mohon coba kembali.')
        exit()

# Trapesium (Ganjil)
else:
    operasi = int(input('''pilih menu hitung Trapesium: 
            1. Keliling
            2. Luas
            
            Pilih dari no diatas: '''))
    
    # Keliling Trapesium
    if operasi == 1:
        sisi_a = int(input('Sisi A: '))
        sisi_b = int(input('Sisi B: '))
        sisi_c = int(input('Sisi C: '))
        sisi_d = int(input('Sisi D: '))

        print('\n', 'Hasil: ', sisi_a + sisi_b + sisi_c + sisi_d)
        exit()

    # Luas Trapesium
    elif operasi == 2:
        sisi_a = int(input('Sisi A: '))
        sisi_b = int(input('Sisi B: '))
        tinggi = int(input('Tinggi: '))

        print('\n', 'Hasil: ', .5 * tinggi * (sisi_a+sisi_b))
        exit()
    else:
        print('operasi gagal, mohon coba kembali.')
        exit()
# print(angka_terakhir)