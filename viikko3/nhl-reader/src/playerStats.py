from player import Player

class PlayerStats:
    def __init__(self,reader):
        self.reader = reader
        self._players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):

        suomalaiset = []
        for player in self._players:
            if nationality == player.nationality:
                suomalaiset.append(player)
                
        suomalaiset.sort(reverse=True)
        return suomalaiset

