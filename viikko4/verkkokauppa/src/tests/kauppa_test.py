import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        # otetaan toteutukset käyttöön
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

####
    def test_tarkistetaan_etta_tuotetta_ja_saldoa_on(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()
        viitegeneraattori_mock.uusi.return_value = 42
        varasto_mock = Mock()
        
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
                
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "viinaa", 5)
            
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote
        
        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")
        
        pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)
        
    def test_testataan_kaksi_tuotetta(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()
        viitegeneraattori_mock.uusi.return_value = 15
        varasto_mock = Mock()
        
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 10
        
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "salmiakkia", 2)
            if tuote_id == 2:
                return Tuote(2, "Kaljaa", 5)
                        
            
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote
        
        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("pekka", "12345")
        
        pankki_mock.tilisiirto.assert_called_with("pekka", 15, "12345", "33333-44455", 7)
        
    def test_testataan_kaksi_samaa_tuotetta(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()
        viitegeneraattori_mock.uusi.return_value = 15
        varasto_mock = Mock()
        
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
                
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "salmiakkia", 2)
        
        
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote
        
        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")
        
        pankki_mock.tilisiirto.assert_called_with("pekka", 15, "12345", "33333-44455", 4)
        
    def test_koriin_tuote_jota_on_saldoilla_ja_mita_ei_ole(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()
        viitegeneraattori_mock.uusi.return_value = 15
        varasto_mock = Mock()
        
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 0
                
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "salmiakkia", 2)
            if tuote_id == 2:
                return Tuote(2, "Mielihyvää", 100)
            
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote
        
        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)
        
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("pekka", "12345")
        
        pankki_mock.tilisiirto.assert_called_with("pekka", 15, "12345", "33333-44455", 2)
        
        
        ###4
        
    def test_edelliset_ostot_ei_nay_korissa(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()
        viitegeneraattori_mock.uusi.return_value = 15
        varasto_mock = Mock()
        
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
                
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "salmiakkia", 2)
            
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote
        
        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)
        
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")
        
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("arto", "54321")
        
        
        pankki_mock.tilisiirto.assert_called_with("arto", 15, "54321", "33333-44455", 2)
        
        
    def test_uusi_viitenumero(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()
        viitegeneraattori_mock.uusi.return_value = 32
        varasto_mock = Mock()
        
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
                
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "salmiakkia", 2)
            
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote
        
        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)
        
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")
        pankki_mock.tilisiirto.assert_called_with("pekka", 32, "12345", "33333-44455", 2)  
        
        viitegeneraattori_mock.uusi.return_value = 66
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("arto", "54321")
        
        
        pankki_mock.tilisiirto.assert_called_with("arto", 66 , "54321", "33333-44455", 2)
        
        
    def test_testataan_poistaa_korista(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()
        viitegeneraattori_mock.uusi.return_value = 15
        varasto_mock = Mock()
        
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
        
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "salmiakkia", 2)
                        
            
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote
        
        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.poista_korista(1)
        
        kauppa.tilimaksu("pekka", "12345")
        
        pankki_mock.tilisiirto.assert_called_with("pekka", 15, "12345", "33333-44455", 0)
        