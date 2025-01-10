from nba_api.stats.static import teams
from nba_api.stats.endpoints import teamgamelog, boxscoreadvancedv2
import pandas as pd 
import time 

def fetch_team_data():
    teams_list = teams.get_teams()
    teams_df = pd.DataFrame(teams_list)[['id', 'full_name']]
    
    return teams_df 

def fetch_season_history(teams):
    season_df = pd.DataFrame()
    for team_id in teams:
        season_history = teamgamelog.TeamGameLog(season='2023-24', season_type_all_star='Regular Season', team_id=team_id).get_data_frames()[0]
        season_df = pd.concat([season_df, season_history])
        # add delay to requests to nba_api otherwise error 
        time.sleep(10)

    return season_df

def fetch_advanced_stats(df):
    # df to store team advanced statistics for every team for every game
    adv_stats = pd.DataFrame()

    # get list of all games for the regular season
    all_games = df['Game_ID'].unique()

    for game in all_games:
        # get team advanced statistics
        adv_boxscore = boxscoreadvancedv2.BoxScoreAdvancedV2(game_id=game)
        adv_boxscore = adv_boxscore.get_data_frames()[1]

        # filter for wanted columns
        adv_boxscore = adv_boxscore[['GAME_ID', 'TEAM_ID', 'OFF_RATING', 'DEF_RATING', 'NET_RATING', 'EFG_PCT', 'TM_TOV_PCT', 'AST_TOV', 'OREB_PCT', 'DREB_PCT', 'REB_PCT']] 
        
        adv_stats = pd.concat([adv_stats, adv_boxscore])
        # add delay to requests to nba_api otherwise error 
        time.sleep(10)

    return adv_stats 

# fetch team id and name for each team
teams_df = fetch_team_data()

# fetch 2023-24 regular season game history for each team
team_ids = teams_df['id']
season_df = fetch_season_history(team_ids)

# merge teams_df and season_df (adding team full name to season history)
season_df = pd.merge(teams_df, season_df, left_on='id', right_on='Team_ID')
season_df.to_pickle('./Datasets/season_hist.pkl')
print("Saved season history data.")

# fetch advance team statistics
adv_stats_df = fetch_advanced_stats(season_df)
adv_stats_df.to_pickle('./Datasets/adv_stats.pkl')
print("Saved advanced statistics data.")

# merge season_df and adv_team_stats_df (adding advance team stats to basic team stats)
merged_df = pd.merge(season_df, adv_stats_df, left_on=['Game_ID', 'Team_ID'], right_on=['GAME_ID', 'TEAM_ID'])
print(merged_df)
print(merged_df.info())
merged_df.to_pickle('./Datasets/merged.pkl')
print("Saved merged data")