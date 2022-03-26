import requests
from player import Player

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()

    #print("JSON-muotoinen vastaus:")
    #print(response)

    players = []
    suomalaiset = []

    for player_dict in response:
        player = Player(
            player_dict['name'],
            player_dict['nationality'],
            player_dict['assists'],
            player_dict['goals'],
            player_dict['penalties'],
            player_dict['team'],
            player_dict['games']
            
        )

        players.append(player)
        
        
        if player_dict['nationality'] == "FIN":
            suomalaiset.append(player)
        
    print("Oliot:")

    for player in suomalaiset:

        print(player.name, player.nationality,player.goals)
        

if __name__ == "__main__":
    main()
