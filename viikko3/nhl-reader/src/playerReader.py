import player
from player import Player
import requests
class PlayerReader:
    
    def __init__(self,url):
        self._url = url
        

    def get_players(self):
             
        response = requests.get(self._url).json()    
        players = []
        
    
        for player_dict in response:
            player = Player(
                player_dict['name'],
                player_dict['nationality'],
                player_dict['assists'],
                player_dict['goals'],
                player_dict['penalties'],
                player_dict['team'],
                player_dict['games'],
                summa = player_dict['assists'] + player_dict['goals']

            )
           
            players.append(player)
            
        return players