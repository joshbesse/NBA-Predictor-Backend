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

def convert_min_to_decimal(min_str):
    if pd.isna(min_str):
        return float('nan')
    else:
        minutes, seconds = min_str.split(':')
        new_min_format = f"{int(float(minutes))}.{seconds}"
        return float(new_min_format) 

def fetch_advance_team_stats(df):
    # df to store team advanced statistics for every team for every game
    team_adv_stats = pd.DataFrame()

    # get list of all games for the regular season
    all_games = df['Game_ID'].unique()

    for game in all_games:
        # get individual player advanced statistics -> need to aggregate and calculate team advanced statistics
        adv_boxscore = boxscoreadvancedv2.BoxScoreAdvancedV2(game_id=game)
        adv_stats_df = adv_boxscore.get_data_frames()[0]

        # convert MIN format from MM:SS string to MM.SS float
        adv_stats_df['MIN'] = adv_stats_df['MIN'].apply(convert_min_to_decimal)
        adv_stats_df = adv_stats_df[adv_stats_df['MIN'] > 0]

        # calculate team advanced statistics for both teams 
        current_teams_adv_stats_df = adv_stats_df.groupby(['GAME_ID', 'TEAM_ID']).apply(
            lambda x: pd.Series({
                'OFF_RATING': (x['OFF_RATING'] * x['MIN']).sum() / x['MIN'].sum(),
                'DEF_RATING': (x['DEF_RATING'] * x['MIN']).sum() / x['MIN'].sum(),
                'NET_RATING': (x['NET_RATING'] * x['MIN']).sum() / x['MIN'].sum(),
                'PACE': (x['PACE'] * x['MIN']).sum() / x['MIN'].sum(),
                'EFF_FG_PCT': (x['EFG_PCT'] * x['MIN']).sum() / x['MIN'].sum(),
                'TS_PCT': (x['TS_PCT'] * x['MIN']).sum() / x['MIN'].sum()
            })
        ).reset_index()

        team_adv_stats = pd.concat([team_adv_stats, current_teams_adv_stats_df])
        time.sleep(10)

    return team_adv_stats 

# fetch team id and name for each team
teams_df = fetch_team_data()

# fetch 2023-24 regular season game history for each team
team_ids = teams_df['id']
season_df = fetch_season_history(team_ids)

# merge teams_df and season_df (adding team full name to season history)
season_df = pd.merge(teams_df, season_df, left_on='id', right_on='Team_ID')
season_df.to_pickle('./season_hist.pkl')
print("Saved season history data.")

# fetch advance team statistics
adv_team_stats_df = fetch_advance_team_stats(season_df)
adv_team_stats_df.to_pickle('./adv_team_stats.pkl')
print("Saved advance team statistics data.")

# merge season_df and adv_team_stats_df (adding advance team stats to basic team stats)
#merged_df = season_df.merge(adv_team_stats_df, left_on=['Game_ID', 'Team_ID'], right_on=['GAME_ID', 'TEAM_ID'])
#print(merged_df)
#print(merged_df.info())
#merged_df.to_pickle('./data.pkl')
#print("Saved merged data")