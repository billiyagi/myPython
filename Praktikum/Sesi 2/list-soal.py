list_makanan = [
    ['bakwan', 'tempe', 'tahu'],
    ['nasi uduk', 'nasi pecel', 'sate padang']
]

# bagaimana memprint nasi pecel
print('print:', list_makanan[1][1])

# Print semua data
for makanan in list_makanan:
    for jenis_makanan in makanan:
        print(jenis_makanan)
