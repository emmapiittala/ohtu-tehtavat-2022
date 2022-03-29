from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.tavaroidenMaara = 0
        self.ostokset = []
        
    def tavaroita_korissa(self):
        
        return self.tavaroidenMaara
    
    def hinta(self):
        
        yhteishinta = 0
        
        for ostos in self.ostokset:
            ostos.hinta()
            yhteishinta += ostos.hinta()
            
        
        return yhteishinta
      
    def lisaa_tuote(self, lisattava: Tuote):
        lisattavaOstos = Ostos(lisattava)

        
        if len(self.ostokset) == 0:
            self.ostokset.append(lisattavaOstos)
            
            self.tavaroidenMaara += 1
            return
        else:
            for ostos in self.ostokset:
                
                if ostos.tuotteen_nimi() == lisattavaOstos.tuotteen_nimi():
                    ostos.muuta_lukumaaraa(1)
                    self.tavaroidenMaara += 1
                    return
                
        self.ostokset.append(lisattavaOstos)
        self.tavaroidenMaara += 1
   
        
    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        pass
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on