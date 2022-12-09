def biodata(nama, alamat, tanggal, umur, bb, tb):

    meter = tb / 100
    bmi = bb / (meter * meter)

    if bmi < 18.5:
        ideal = 'Kurus'
    elif bmi <= 24.9:
        ideal = 'Normal'
    else:
        ideal = 'Gemuk'

    return f'''
    =================
    ===> Biodata <===
    =================

    Nama         : {nama}
    Alamat       : {alamat}
    Tanggal      : {tanggal}
    Usia         : {str(umur)}
    Tinggi Badan : {str(tb)} cm
    Berat badan  : {str(bb)}kg - {ideal}
    '''


print(
    biodata('Febry Billiyagi Karsidi',
            'Jl.Pabrik Kulit RT05/RW03, Cibinong - Bogor', '19 Februari 2003',
            19, 51, 170))
