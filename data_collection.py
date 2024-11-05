from nba_api.stats.static import teams
from nba_api.stats.endpoints import teamgamelog, boxscoreadvancedv2
import pandas as pd 

# team id and names 
teams = teams.get_teams()
team_df = pd.DataFrame(teams)[['id', 'full_name']]

# season game history for the Hawks -> basic team statistics & game context & team recent performance & target variable 
games = teamgamelog.TeamGameLog(season='2023-24', season_type_all_star='Regular Season', team_id=1610612737).get_dict()['resultSets']
games_columns = games[0]['headers']
games_rows = games[0]['rowSet']
games_df = pd.DataFrame(data=games_rows, columns=games_columns)
print(games_df)

# get individual player advanced statistics -> need to aggregate -> advanced team statistics & team recent performance  
boxscore = boxscoreadvancedv2.BoxScoreAdvancedV2(game_id='0022301188')
advanced = boxscore.get_data_frames()[0]
#print(advanced[['OFF_RATING', 'DEF_RATING', 'NET_RATING']])

# key player information -> manually collect 