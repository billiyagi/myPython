# Tugas DDP - 08
# Febry Billiyagi Karsidi - TI 02
# Membuat baris bintang dengan pengulangan FOR

star_range = int(input('''
Baris bintang: '''))


print('''
====================
======> Hasil <=====
====================
-> baris: ''' + str(star_range))
for i in range(1, star_range+1):
    a = ''
    for j in range(i):
        a += '*'
    print(a)
