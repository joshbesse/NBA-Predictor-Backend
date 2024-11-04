import pandas as pd 
from nba_api.live.nba.endpoints import scoreboard

# today's score board
scoreboard = scoreboard.ScoreBoard()
scoreboard_dict = scoreboard.get_dict()

# date
date = scoreboard_dict['scoreboard']['gameDate']
print(f"date: {date}")

# games
games = scoreboard_dict['scoreboard']['games']
print(games)