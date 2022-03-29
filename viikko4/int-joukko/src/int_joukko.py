import itertools

class IntJoukko:
    def __init__(self, kapasiteetti=0, kasvatuskoko=0):
        self.kapasiteetti = 5 if kapasiteetti <= 0 else kapasiteetti
        self.kasvatuskoko = 5 if kasvatuskoko <= 0 else kasvatuskoko
        self.ljono = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def kuuluu(self, loytyyko):
        apu = 0

        for i in range(self.alkioiden_lkm):
            if loytyyko == self.ljono[i]:
                apu = apu + 1

        return apu > 0

    def lisaa(self, lisays):
        if self.alkioiden_lkm == 0:
            self.ljono[0] = lisays
            self.alkioiden_lkm = self.alkioiden_lkm + 1
            return True
        if not self.kuuluu(lisays):
            self.ljono[self.alkioiden_lkm] = lisays
            self.alkioiden_lkm = self.alkioiden_lkm + 1

            if self.alkioiden_lkm % len(self.ljono) == 0:
                taulukko_old = self.ljono
                self.kopioi_taulukko(self.ljono, taulukko_old)
                self.ljono = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_taulukko(taulukko_old, self.ljono)

            return True

        return False
    
    
    def poista(self, poistaa):
        for indeksi in range(self.alkioiden_lkm):
            if poistaa == self.ljono[indeksi]:
                self.ljono[indeksi] = 0

                for joukko in range(indeksi, self.alkioiden_lkm - 1):
                    apu = self.ljono[joukko]
                    self.ljono[joukko] = self.ljono[joukko + 1]
                    self.ljono[joukko + 1] = apu
                self.alkioiden_lkm = self.alkioiden_lkm - 1
                return True

        return False

    def kopioi_taulukko(self, joukko1, joukko2):
        for i in range(len(joukko1)):
            joukko2[i] = joukko1[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = [0] * self.alkioiden_lkm

        for i in range(len(taulu)):
            taulu[i] = self.ljono[i]

        return taulu

    @staticmethod
    def yhdiste(joukko1, joukko2):
        joukkio = IntJoukko()
        ykkonenT = joukko1.to_int_list()
        kakkonenT = joukko2.to_int_list()

        for i in range(len(ykkonenT)):
            joukkio.lisaa(ykkonenT[i])

        for i in range(len(kakkonenT)):
            joukkio.lisaa(kakkonenT[i])

        return joukkio

    @staticmethod
    def leikkaus(joukko1, joukko2):
        joukkio = IntJoukko()
        ykkonenT= joukko1.to_int_list()
        kakkonenT = joukko2.to_int_list()

        for i, joukko in itertools.product(range(len(ykkonenT)), range(len(kakkonenT))):
            if ykkonenT[i] == kakkonenT[joukko]:
                joukkio.lisaa(kakkonenT[joukko])

        return joukkio

    @staticmethod
    def erotus(joukko1, joukko2):
        joukkio = IntJoukko()
        ykkonenT = joukko1.to_int_list()
        kakkonenT = joukko2.to_int_list()

        for i in range(len(ykkonenT)):
            joukkio.lisaa(ykkonenT[i])

        for i in range(len(kakkonenT)):
            joukkio.poista(kakkonenT[i])

        return joukkio

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.ljono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.ljono[i])
                tuotos = f'{tuotos}, '
            tuotos = tuotos + str(self.ljono[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
