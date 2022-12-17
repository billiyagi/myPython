buah = ['mangga', 'melon', 'semangka', 'apel']
# menambah data
buah.append('jeruk')

# mengubah data
buah[0] = 'dukuh'

# menghapus data dengan del
del buah[1]

# mengambil data yang paling akhir => pop()
buah.pop()

# mengetahui jumlah data => len()
len(buah)

# menyisipkan data seletah index ke 1
buah.insert(1, 'kelengkeng')
print(buah)

for i in buah:
    print('Buah', i)
