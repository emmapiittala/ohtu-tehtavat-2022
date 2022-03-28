

class Player:
    def __init__(self, name,nationality,assists,goals,penalties,team,games,summa):
        self.name = name
        self.nationality = nationality
        self.assists = assists 
        self.goals = goals 
        self.penalties = penalties 
        self.team = team 
        self.games = games
        self.summa = summa
    
    
    def __str__(self):
        return f'{self.name} {self.nationality} {self.goals} + {self.assists} = {self.summa}'
        


    def __lt__(self,muu):
        return int(self.summa) < int(muu.summa)