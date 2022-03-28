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


    for player in players:
        print(player)

if __name__ == "__main__":
    main()
