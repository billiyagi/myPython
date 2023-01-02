from Animal import *


class Cheetah(Animal):
    berbisa = False
    bertaring = False

    def __init__(self, nama, makanan, hidup, berkembangBiak, berbisa, bertaring,):
        Animal.__init__(self, nama, makanan, hidup, berkembangBiak)
        self.berbisa = berbisa
        self.bertaring = bertaring
        print(f'''
======================================
Nama		: {nama}
Makanan		: {makanan}
Hidup		: {hidup}
Berkembang Biak	: {berkembangBiak}
Berbisa		: {'Ya' if berbisa else 'Tidak'}
Bertaring	: {'Ya' if bertaring else 'Tidak'}
Kemampuan	: Berlari cepat, Mengigit
======================================
		''')

    def sprint(self):
        print(f'Cheetah sedang berlari sangat kencang..')

    def bite(self, mangsa):
        print(f'Gigit {mangsa} ..')


ular = Cheetah('Cheetah', 'Madu', 'Darat', 'Melahirkan', False, True)
ular.sprint()
