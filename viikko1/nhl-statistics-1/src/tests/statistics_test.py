import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )
            
    def test_loytyyko_pelaaja_nimella(self):
        pelaaja = "Semenko"
        loytynytpelaaja = self.statistics.search(pelaaja)
        self.assertEqual(pelaaja, loytynytpelaaja.name)
        
    def test_vaara_nimella(self):
        pelaaja = "Piittala"
        eiloydy = self.statistics.search(pelaaja)
        self.assertEqual(eiloydy, None)

    def test_loytyyko_tiimeja_oikeamaara(self):
        tiimi = "EDM"
        loytyneetpelaajat = self.statistics.team(tiimi)
        self.assertEqual(len(loytyneetpelaajat),3)
        
    def test_loutaako_parhaimman_pelaajan_pisteet(self):
        paras = 1
        loutyneetpisteet = self.statistics.top_scorers(paras)
        self.assertEqual(loutyneetpisteet[0].goals,35)

    def test_hello_world(self):
        self.assertEqual("Hello world", "Hello world")
        
