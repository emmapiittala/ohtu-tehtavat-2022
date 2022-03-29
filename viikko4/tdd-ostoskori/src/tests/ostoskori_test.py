import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()
        self.maito = Tuote("Maito",3)
        self.viina = Tuote("Viina", 7)
    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)
        
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_on_oikea_hinta(self):
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(self.kori.hinta(),3)
        
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskorissa_on_kaksituotetta(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.viina)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
        
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_sama_kun_tuotteiden_hinta(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.viina)
        self.assertEqual(self.kori.hinta(), 10)
        
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorissa_on_kaksi_tavaraa(self):
        self.kori.lisaa_tuote(self.viina)
        self.kori.lisaa_tuote(self.viina)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
        
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_sama_kuin_kaks_kertaa_tuotteen_hinta(self):
        self.kori.lisaa_tuote(self.viina)
        self.kori.lisaa_tuote(self.viina)
        self.assertEqual(self.kori.hinta(), 14)
        
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)
        
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(),"Maito")
        self.assertEqual(self.kori.tavaroita_korissa(), 1)
        
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskori_sisaltaa_kaksi_ostosta(self):
        self.kori.lisaa_tuote(self.viina)
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(self.kori.tavaroita_korissa(),2)