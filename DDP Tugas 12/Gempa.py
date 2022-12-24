# Febry Billiyagi Karsidi - TI 02
# Tugas DDP 12

class Gempa:
    lokasi = ''
    skala = 0

    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala

    def dampak(self):
        if self.skala < 2:
            print('Dampak gempa tidak terasa.')
        elif self.skala >= 2 and self.skala < 4:
            print('Dampak gempa banguna retak-retak.')
        elif self.skala >= 4 and self.skala < 6:
            print('Dampak gempa bangunan roboh.')
        else:
            print('Dampak gempa bangunan roboh dan berpotensi Tsunami!.')
