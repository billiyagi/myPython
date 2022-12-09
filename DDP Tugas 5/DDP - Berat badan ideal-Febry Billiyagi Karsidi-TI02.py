# Tugas Dasar Dasar Pemgragraman - Tugas ke 5
# Oleh Febry Billiyagi Karsidi dari TI02
# Program menghitung berat badan ideal untuk Wanita & Pria

print('''
Program menghitung Berat Badan Ideal, pilih salah satu nomor
1). Berat badan ideal Wanita
2). Berat badan ideal Pria
''')
choosenMenu = int(input(': '))

if choosenMenu == 1:
    print("Operasi menghitung berat badan Wanita")
    tinggi = int(input('Tinggi badan (cm): '))

    result = (tinggi - 100) - (tinggi - 100) / 15
    print('berat badan ideal kamu adalah: ', result)
elif choosenMenu == 2:
    print("Operasi menghitung berat badan Pria")
    tinggi = int(input('Tinggi badan (cm): '))
    result = (tinggi - 100) - (tinggi - 100) / 10
    print('berat badan ideal kamu adalah: ', result)
else: 
    print("Terjadi Kesalahan, Ulangi Program")