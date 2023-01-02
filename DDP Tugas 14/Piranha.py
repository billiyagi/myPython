from Animal import *


class Piranha(Animal):
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
Kemampuan	: Menyerang secara berkerumun, Mengigit
======================================
		''')

    def powerClustered(self):
        print(f'Piranha bersama kawanannya mengejarmu!')

    def bite(self, mangsa):
        print(f'Gigit {mangsa} ..')


ular = Piranha('Piranha', 'Ikan kecil dan Daging potongan',
               'Air', 'Bertelur', False, True)
ular.powerClustered()
