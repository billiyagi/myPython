from Animal import *


class Snake(Animal):
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
Kemampuan	: Berbisa, Bertaring
======================================
		''')

    def wrapsAround(self, mangsa):
        print(f'Ular sedang melilit {mangsa}..')

    def bite(self, mangsa):
        print(f'Gigit {mangsa} ..')


ular = Snake('Ular Piton', 'Rusa', 'Darat', 'Bertelur', True, True)
ular.bite('Rusa')
