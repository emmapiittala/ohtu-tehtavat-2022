class TennisGame:
    def __init__(self, pelaaja1_nimi, pelaaja2_nimi):
        self.pelaaja1_nimi = pelaaja1_nimi
        self.pelaaja2_nimi = pelaaja2_nimi
        self.pelaaja1_pisteet = 0
        self.pelaaja2_pisteet = 0

    def won_point(self, pelaajan_nimi):
        if pelaajan_nimi == "player1":
            self.pelaaja1_pisteet = self.pelaaja1_pisteet + 1
        else:
            self.pelaaja2_pisteet = self.pelaaja2_pisteet + 1
    
    
    def tasapeli(self):
            
        if self.pelaaja1_pisteet == self.pelaaja2_pisteet:
            if self.pelaaja1_pisteet == 0:
                return "Love-All"
            elif self.pelaaja1_pisteet == 1:
                return "Fifteen-All"
            elif self.pelaaja1_pisteet == 2:
                return "Thirty-All"
            elif self.pelaaja1_pisteet == 3:
                return "Forty-All"
            else:
                return "Deuce"

    def johtaa(self):
        
        
        if self.pelaaja1_pisteet >= 4 or self.pelaaja2_pisteet >= 4:
            minus_result = self.pelaaja1_pisteet - self.pelaaja2_pisteet

            if minus_result == 1:
                return  "Advantage player1"
            elif minus_result == -1:
                return "Advantage player2"
            elif minus_result >= 2:
                return "Win for player1"
            else:
                return "Win for player2"
         
       
    
    def get_score(self):
        pisteet = ""
        vpisteet = 0

        if self.pelaaja1_pisteet == self.pelaaja2_pisteet:
            return self.tasapeli()

        if self.pelaaja1_pisteet >= 4 or self.pelaaja2_pisteet >= 4:
            return self.johtaa()
          
        else:
            for i in range(1, 3):
                if i == 1:
                    vpisteet = self.pelaaja1_pisteet
                else:
                    pisteet = pisteet + "-"
                    vpisteet = self.pelaaja2_pisteet

                if vpisteet == 0:
                    pisteet = pisteet + "Love"
                elif vpisteet == 1:
                    pisteet = pisteet + "Fifteen"
                elif vpisteet == 2:
                    pisteet = pisteet + "Thirty"
                elif vpisteet == 3:
                    pisteet = pisteet + "Forty"

        return pisteet


