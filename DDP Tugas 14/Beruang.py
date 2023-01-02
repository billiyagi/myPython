from Animal import *


class Beruang(Animal):
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
Kemampuan	: Mencakar, Mengigit
======================================
		''')

    def scratch(self, mangsa):
        print(f'Beruang sedang mencakar {mangsa}..')

    def bite(self, mangsa):
        print(f'Gigit {mangsa} ..')


ular = Beruang('Beruang', 'Madu', 'Darat', 'Melahirkan', False, True)
ular.scratch('Manusia')
