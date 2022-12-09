# Tugas Kondisi cuaca berangkat kuliah
# Febry Billiyagi Karsidi - TI 02


def cek_kondisi_cuaca(cuaca):
    if cuaca == 'hujan':
        return 'Naik Gocar'
    else:
        return 'Naik motor'


print(cek_kondisi_cuaca('hujan'))