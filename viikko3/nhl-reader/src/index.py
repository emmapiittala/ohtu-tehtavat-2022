import requests

from player import Player
from playerReader import PlayerReader
from playerStats import PlayerStats


def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    # players = stats.top_scorers_by_nationality("FIN")
    #print("JSON-muotoinen vastaus:")
    #print(response)
    
    # suomalaiset = []
    
#    # for player_dict in response:
#     #    player = Player(
#             player_dict['name'],
#             player_dict['nationality'],
#             player_dict['assists'],
#             player_dict['goals'],
#             player_dict['penalties'],
#             player_dict['team'],
#             player_dict['games'],
            
#             summa = player_dict['assists'] + player_dict['goals']
        # )

        # players.append(player)
        #########
        
    #     if player_dict['nationality'] == "FIN":
    #         suomalaiset.append(player)
        
    # print("Oliot:")
    
    # suomalaiset.sort(reverse=True)
    # for player in suomalaiset:
    #     summa =  player.goals + player.assists
        
    #     print(player.name, player.nationality,player.goals, " + ", player.assists, " = ", summa)
        
    for player in players:
        print(player)

if __name__ == "__main__":
    main()
