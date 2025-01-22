from requests.exceptions import ReadTimeout
from nba_api.stats.endpoints import boxscoreadvancedv2, boxscoresummaryv2, boxscorescoringv2, teamgamelog
from nba_api.stats.static import teams
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
        time.sleep(10)
    
    return season_df

#def fetch_starters_inactives(games):
    #starters_inactives_df = pd.DataFrame()

    #for game in games:
        #starters = boxscorescoringv2.BoxScoreScoringV2(game_id=game).get_data_frames()[0]




teams_df = fetch_team_data()
team_ids = teams_df['id']
season_df = fetch_season_history(team_ids)
all_games = season_df['Game_ID'].unique()



# ------
starts_df = pd.DataFrame()
inactive_df = pd.DataFrame()
for game in all_games:
    for attempt in range(3):
        try:
            starts = boxscorescoringv2.BoxScoreScoringV2(game_id=game).get_data_frames()[0]
            starts = starts[['GAME_ID', 'TEAM_ID', 'TEAM_ABBREVIATION', 'PLAYER_NAME', 'START_POSITION']]
            starts['IS_STARTER'] = starts['START_POSITION'].apply(lambda x: 1 if x != '' else 0)
            starts.drop(columns=['START_POSITION'], inplace=True)
            starts_df = pd.concat([starts_df, starts])
            time.sleep(10)

            inactive = boxscoresummaryv2.BoxScoreSummaryV2(game_id=game).get_data_frames()[3]
            inactive['GAME_ID'] = game
            inactive['PLAYER_NAME'] = inactive.apply(lambda row: row['FIRST_NAME'] + ' ' + row['LAST_NAME'], axis=1)
            inactive = inactive[['GAME_ID', 'TEAM_ID', 'TEAM_ABBREVIATION', 'PLAYER_NAME']]
            inactive_df = pd.concat([inactive_df, inactive])
            time.sleep(10)
        except ReadTimeout:
            print(f'Attempt {attempt + 1}: Request timed out. Retrying...')
            time.sleep(10)

starts_df = starts_df.sort_values('GAME_ID')
starts_df['CUMULATIVE_STARTS'] = starts_df.groupby(['TEAM_ABBREVIATION', 'PLAYER_NAME'])['IS_STARTER'].cumsum()
starts_df['RANK'] = starts_df.groupby(['GAME_ID', 'TEAM_ABBREVIATION'])['CUMULATIVE_STARTS'].rank(method='first', ascending=False)
starts_df.to_pickle('./Test/starts.pkl')

top_5_players = starts_df[starts_df['RANK'] <= 5].sort_values(['GAME_ID', 'TEAM_ABBREVIATION', 'RANK'])
top_5_players.to_pickle('./Test/top5.pkl')

print(starts_df.head(50))
print(inactive_df.head(50))

test = pd.merge(top_5_players, inactive_df, on=['GAME_ID', 'TEAM_ID', 'PLAYER_NAME'])
test.to_pickle('./Test/test.pkl')
print(test.head(50))

#df = df.sort_values('GAME_ID')
#df['CUMULATIVE_STARTS'] = df.groupby(['TEAM_ABBREVIATION', 'PLAYER_NAME'])['IS_STARTER'].cumsum()

#df['RANK'] = df.groupby(['GAME_ID', 'TEAM_ABBREVIATION'])['CUMULATIVE_STARTS'].rank(method='first', ascending=False)
#top_5_players = df[df['RANK'] <= 5].sort_values(['GAME_ID', 'TEAM_ABBREVIATION', 'RANK'])
#print(top_5_players.head(50))


# retrieve inactive players for a game
#inactive = boxscoresummaryv2.BoxScoreSummaryV2(game_id='0022400577').get_data_frames()[3]
#print(inactive)




# ------
# retrieve latest games (game id, teams, score, win/losses)
#scoreboard = scoreboard.ScoreBoard().get_dict()
#games = scoreboard['scoreboard']['games']
#for game in games:
    #print(f"Game ID: {game['gameId']}, {game['homeTeam']['teamName']}: {game['homeTeam']['score']} ({game['homeTeam']['wins']} W {game['homeTeam']['losses']} L) vs. {game['awayTeam']['teamName']}: {game['awayTeam']['score']} ({game['awayTeam']['wins']} W {game['awayTeam']['losses']} L)")

