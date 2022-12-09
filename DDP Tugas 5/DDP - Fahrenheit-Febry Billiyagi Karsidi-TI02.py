# Tugas Dasar Dasar Pemgragraman - Tugas ke 5
# Oleh Febry Billiyagi Karsidi dari TI02
# Program menghitung konversi Fahrenheit ke Celcius & Reamur

print('''
Program menghitung Fahrenheit ke Celcius & Reamur, pilih salah satu nomor
1). Fahrenheit ke Celcius
2). Fahrenheit ke Reamur
''')
choosenMenu = int(input(': '))

if choosenMenu == 1:
    print("Operasi menghitung Fahrenheit ke Celcius")
    fahrenheit = int(input("Suhu Fahrenheit: "))
    result = (fahrenheit - 32) * 5/9
    print('hasilnya adalah: ', result)
elif choosenMenu == 2:
    print("Operasi menghitung Fahrenheit ke Reamur")
    fahrenheit = int(input("Suhu Fahrenheit: "))
    result = 4/9 * (fahrenheit - 32)
    print('hasilnya adalah: ', result)
else: 
    print("Terjadi Kesalahan, Ulangi Program")