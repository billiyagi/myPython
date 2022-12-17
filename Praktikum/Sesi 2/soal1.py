hasil_akhir = [
    {'nama': 'Reza', 'nilai': 70},
    {'nama': 'Ciut', 'nilai': 63},
    {'nama': 'Dian', 'nilai': 80},
    {'nama': 'Badu', 'nilai': 40}
]


def lulus_saja(hasil_akhir):
    result = []
    for mhs in hasil_akhir:
        if mhs['nilai'] >= 65:
            result.append(mhs['nama'])
    return result


print(lulus_saja(hasil_akhir))
