# Tugas Dasar Dasar Pemgragraman - Tugas ke 5
# Oleh Febry Billiyagi Karsidi dari TI02
# Program menghitung Luas & Keliling dari Jajargenjang

print('''
Program menghitung Luas & Keliling Jajargenjang, pilih salah satu nomor
1). Luas
2). Keliling
''')
choosenMenu = int(input(': '))

if choosenMenu == 1:
    print("Operasi menghitung Luas jajargenjang")
    alas = int(input("Alas: "))
    tinggi = int(input("Tinggi: "))
    result = alas * tinggi
    print('hasilnya adalah: ', result)
elif choosenMenu == 2:
    print("Operasi menghitung Keliling jajargenjang")
    alas = int(input("Alas: "))
    tinggi = int(input("Sisi miring: "))
    result = 2 * (alas+tinggi)
    print('hasilnya adalah: ', result)
else: 
    print("Terjadi Kesalahan, Ulangi Program")