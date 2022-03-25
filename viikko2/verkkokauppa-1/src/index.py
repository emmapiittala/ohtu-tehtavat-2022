from kauppa import Kauppa
from kirjanpito import Kirjanpito
from varasto import Varasto
from pankki import Pankki
from viitegeneraattori import Viitegeneraattori


def main():
    

    viitegeneraattori = Viitegeneraattori()
    kirjanpito = Kirjanpito()
    varasto = Varasto(kirjanpito)
    pankki = Pankki(kirjanpito)
    kauppa = Kauppa(varasto, pankki, viitegeneraattori)

    # seuraava asiakas
    kauppa.aloita_asiointi()

    for _ in range(0, 24):
        kauppa.lisaa_koriin(5)

    kauppa.tilimaksu("Arto Vihavainen", "3425-1652")

    # kirjanpito
    for tapahtuma in Kirjanpito().tapahtumat:
        print(tapahtuma)

kauppa = Kauppa(
  Varasto,
  Pankki,
  Viitegeneraattori()
)

if __name__ == "__main__":
    main()
