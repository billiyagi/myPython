gorengan = ('Bakwan', 'Combro', 'Misro')
sop = ('Sop Iga', 'Sop Buntut', 'Sop Kaki')
nasi = ('Nasi Uduk', 'Nasi Goreng', 'Nasi Remes')

# nested Tuple
makanan = (gorengan, sop, nasi)

print('-----Cetak Gorengan-----')
print(makanan[0])
print('-----Cetak per item-----')
print(makanan[1][1])  # sop Buntut
print(makanan[2][2])  # Nasi Remes
print('----Cetak all makanan----')
for jenis_makanan in makanan:
    for detail_makanan in jenis_makanan:
        print(detail_makanan)
