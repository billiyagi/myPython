# Program menghitung jarak tempuh
# Febry Billiyagi Karsidi - TI 02

import math

# input Kendaraan
vehicle = input('Kendaraan (cth: Motor): ')

# input tipe bensin
fuel_type = int(input('''
Pilih jenis bensin:
1. pertalite
2. pertamax
3. pertamax turbo

ketik angka dari jenis bensin diatas: '''))

# Cek jenis bensin yang di input oleh user
if fuel_type not in [1,2,3]:
    # Jika jenis bensin tidak tertera dalam array maka hentikan program dan kirim feedback
    print('Jenis bensin tidak termasuk, mohon ulang kembali')
    exit()

# input kota tujuan
city = int(input('''
Pilih kota tujuan:
1. Jakarta
2. Bekasi
3. Depok
4. Tangerang
5. Bogor

ketik angka dari jenis bensin diatas: '''))


# Cek tujuan kota yang di input oleh user
if city not in [1,2,3,4,5]:
    # Jika tujuan tidak tertera dalam array maka hentikan program dan kirim feedback
    print('Tujuan kota tidak termasuk, mohon ulang kembali')
    exit()


# Cek dan hitung pemakaian bensin di setiap tujuan kota

# Jakarta: 20 KM
if city == 1:
    # pertalite
    if fuel_type == 1:
        fuel_usage = 20 / 12
        fuel_price = math.ceil(fuel_usage) * 10000
    # pertamax
    elif fuel_type == 2:
        fuel_usage = 20 / 13
        fuel_price = math.ceil(fuel_usage) * 14000
    # Pertamax Turbo
    elif fuel_type == 3:
        fuel_usage = 20 / 13.5
        fuel_price = math.ceil(fuel_usage) * 17000

# Bekasi: 35.7KM
elif city == 2:
    # pertalite
    if fuel_type == 1:
        fuel_usage = 35.7 / 12
        fuel_price = math.ceil(fuel_usage) * 10000
    # pertamax
    elif fuel_type == 2:
        fuel_usage = 35.7 / 13
        fuel_price = math.ceil(fuel_usage) * 14000
    # Pertamax Turbo
    elif fuel_type == 3:
        fuel_usage = 35.7 / 13.5
        fuel_price = math.ceil(fuel_usage) * 17000

# Depok: 5KM
elif city == 3:
    # pertalite
    if fuel_type == 1:
        fuel_usage = 5 / 12
    # pertamax
    elif fuel_type == 2:
        fuel_usage = 5 / 13
        fuel_price = math.ceil(fuel_usage) * 14000
    # Pertamax Turbo
    elif fuel_type == 3:
        fuel_usage = 5 / 13.5
        fuel_price = math.ceil(fuel_usage) * 17000

# Tangerang: 99KM
elif city == 4:
    # pertalite
    if fuel_type == 1:
        fuel_usage = 99 / 12
        fuel_price = math.ceil(fuel_usage) * 10000
    # pertamax
    elif fuel_type == 2:
        fuel_usage = 99 / 13
        fuel_price = math.ceil(fuel_usage) * 14000
    # Pertamax Turbo
    elif fuel_type == 3:
        fuel_usage = 99 / 13.5
        fuel_price = math.ceil(fuel_usage) * 17000

# Bogor: 120.6KM
elif city == 5:
    # pertalite
    if fuel_type == 1:
        fuel_usage = 120.6 / 12
        fuel_price = math.ceil(fuel_usage) * 10000
    # pertamax
    elif fuel_type == 2:
        fuel_usage = 120.6 / 13
        fuel_price = math.ceil(fuel_usage) * 14000
    # Pertamax Turbo
    elif fuel_type == 3:
        fuel_usage = 120.6 / 13.5
        fuel_price = math.ceil(fuel_usage) * 17000
else:
    print('Terjadi kesalahan, mohon ulang kembali')
    exit()


print('Nama kendaraan: ', vehicle + '\n',
    'Jenis bensin: ', str(fuel_type) + '\n',
    'Pemakaian: ', str(math.ceil(fuel_usage)) + 'KM \n',
    'Harga: ', 'Rp ' + str(fuel_price))

