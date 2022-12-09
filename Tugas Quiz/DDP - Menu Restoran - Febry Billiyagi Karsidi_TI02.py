# Program menghitung menu restoran
# Febry Billiyagi Karsidi - TI 02


# Data pelanggan
costumer_name = input('Nama pembeli: ')
costumer_number = int(input('No HP pembeli: '))

# Pilih menu makanan/minuman
menu_type = int(input('''
Pilih menu:
1. Makanan
2. Minuman

ketik angka pada menu: '''))


# Data makanan
foods = [
    [1, 'Nasi Goreng', 15000],
    [2, 'Mie Goreng', 12000],
    [3, 'Ayam Geprek', 18000]
]

# Data minuman
drinks = [
    [1, 'Aneka Jus', 15000],
    [2, 'Soft Drink', 10000],
    [3, 'Sweet Ice Tea', 5000]
]


# Menampilkan tipe menu yang dipilih
if menu_type == 1:
    ordered = int(input('''
    Pilih makanan yang ingin dipesan:
    1. Nasi Goreng
    2. Mie Goreng
    3. Ayam Geprek
    
    Ketik angka pada menu: '''))

    if menu_type not in [1,2,3]:
        print('Terjadi kesalahan, mohon ulang kembali')
        exit()
    else:
        choosen_orders = foods[ordered-1]
elif menu_type == 2:
    ordered = int(input('''
    Pilih minuman yang ingin dipesan:
    1. Aneka Jus
    2. Soft Drink
    3. Sweet Ice Tea
    
    Ketik angka pada menu: '''))

    if menu_type not in [1,2,3]:
        print('Terjadi kesalahan, mohon ulang kembali')
        exit()
    else:
        choosen_orders = drinks[ordered-1]
else:
    print('Menu tidak termasuk, mohon ulang kembali.')
    exit()


# Total pesanan
order_quantity = int(input('Jumlah pesanan: '))

print('Pembeli: ', costumer_name + '\n',
        'No HP: ', str(costumer_number) + '\n',
        'Pesanan: ', choosen_orders[1] + '\n',
        'Jumlah: ', str(order_quantity) + '\n',
        'Total Harga: Rp ', order_quantity * choosen_orders[2])