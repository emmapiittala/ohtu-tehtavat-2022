from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.tavaroidenMaara = 0
        self.ostoksetLista = []
        
    def tavaroita_korissa(self):
        
        return self.tavaroidenMaara
    
    def hinta(self):
        
        yhteishinta = 0
        
        for ostos in self.ostoksetLista:
            ostos.hinta()
            yhteishinta += ostos.hinta()
            
        
        return yhteishinta
      
    def lisaa_tuote(self, lisattava: Tuote):
        lisattavaOstos = Ostos(lisattava)

        
        if len(self.ostoksetLista) == 0:
            self.ostoksetLista.append(lisattavaOstos)
            
            self.tavaroidenMaara += 1
            return
        else:
            for ostos in self.ostoksetLista:
                
                if ostos.tuotteen_nimi() == lisattavaOstos.tuotteen_nimi():
                    ostos.muuta_lukumaaraa(1)
                    self.tavaroidenMaara += 1
                    return
                
        self.ostoksetLista.append(lisattavaOstos)
        self.tavaroidenMaara += 1
   
        
    def poista_tuote(self, poistettava: Tuote):
        
        for ostos in self.ostoksetLista:
            if ostos.tuotteen_nimi() == poistettava.nimi():
                self.tavaroidenMaara -= 1
                if ostos.lukumaara() <= 0:
                    self.ostoksetLista.remove(ostos)
            
                
    def tyhjenna(self):
        self.ostoksetLista.clear()

    def ostokset(self):
        return self.ostoksetLista