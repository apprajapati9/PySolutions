import os
import sys
import pandas as pd
from collections import defaultdict

teams_map = {
    "CLE": "Cleaveland Cavaliers",
    "DET": "Detroit Pistons",
    "SAS": "San Antanio Spurs",
    "ATL": "Atlanta Hawks",
    "MIL": "Milwaukee Bucks",
    "CHA": "Charlotte Hornets",
    "MEM": "Memphis Grizzlies",
    "TOR": "Toronto Raptors",
    "MIA": "Miami Heat",
    "PHI": "Philadeplhia 67ers",
    "WAS": "Washington Wizards",
    "NJN": "Brooklyn Nets",
    "CHI": "Chicago Bulls",
    "MIN": "Minnesota Timberwolves",
    "GSW": "Golden State Warriors",
    "UTA": "Utah Jazz",
    "NOH": "New Orleans Pelicans",
    "DEN": "Denver Nuggets",
    "PHO": "Phoenix Suns",
    "OKC": "Oklahoma City Thunders",
    "ORL": "Orlando Magic",
    "SAC": "Sacramanto Kings",
    "HOU": "Houston Rockets",
    "DAL": "Dallas Mavericks",
    "IND": "Indiana Pacers",
    "LAL": "Los Angeles Lakers",
    "BOS": "Boston Celtics",
    "POR":"Portland Trail Blazers"
}

def replace_delim(output_file, delim = ""):
    with open(output_file, "r") as f:
        content = f.read().replace('\t', delim)

    with open(output_file, "w") as f:
        f.write(content)

# {
#   "game": {
#     "team1": "DAL",
#     "team2": "HAL"
#   },
#   "game": {
#     "team1": "DAL",
#     "team2": "HAL"
#   },
#   "game": {
#     "team1": "DAL",
#     "team2": "HAL"
#   }
# }

class Team:
    def __init__(self, team_data, player_data):
        self.team = team_data
        self.player = player_data

class Game:
    def __init__(self, team1_id ="", team2_id =""):
        self.team1_id = team1_id
        self.team2_id = team2_id
        

        
#pd.set_option('display.max_columns', None)
pd.set_option('display.encoding', 'utf-8')
#print(sys.getdefaultencoding())

team_file_names = os.listdir('./files/teams')
player_file_names = os.listdir('./files/players')
all_players_file_names = os.listdir('./files/allplayers')
all_teams_file_names = os.listdir('./files/allteams')

# print(team_file_names)
# print(player_file_names)

games = []

#C-k is like cut, C-y is paste

file_path = os.path.dirname(os.path.abspath(__file__))

team_paths = []
player_paths = []
all_player_paths = []
all_teams_paths = []
#print("Teams file paths-->  \n")
# for team files
for i in team_file_names:
    path = file_path + "\\files\\teams\\{}".format(i)
    team_paths.append(path)
    #print(path)

#print("Players file paths--> \n")
# for players files
for i in player_file_names:
    path = file_path + "\\files\\players\\{}".format(i)
    player_paths.append(path)
    #print(path)

for i in all_players_file_names:
    path = file_path + "\\files\\allplayers\\{}".format(i)
    all_player_paths.append(path)

for i in all_teams_file_names:
    path = file_path + "\\files\\allteams\\{}".format(i)
    all_teams_paths.append(path)

assert len(player_paths) == len(team_paths), "Don't have all data about the games" 

# xls_file = pd.ExcelFile(files[0], engine='openpyxl')

for index, name in enumerate(team_file_names):
    team_file_names[index] = name[0:3]

for index, name in enumerate(player_file_names):
    player_file_names[index] = name[0:3]

print("\nCurrently Available team data and their ids from 1 to {}\n".format(len(team_paths)))
available_teams_map = {}
for index, name in enumerate(team_file_names):
    current = index + 1
    available_teams_map[current] = name
    print("ID:",current, "| Team:", teams_map[available_teams_map[current]])
      
assert len(team_file_names) == len(player_file_names), "Either Player or Team data is missing."

#print("Avail maps -> ", available_teams_map)

team_data_map = {}
player_data_map = {}

# storing data in team_file_data for all paths in file_paths
for team_path in team_paths:
    team_id = team_path.split('\\')[-1][0:3]
    #print(team_id)
    team_data = pd.read_html(team_path, flavor='lxml', encoding ='utf-8', header=1, keep_default_na=True, converters=defaultdict(lambda: str))
    team_data[0] = team_data[0].rename(columns = {"Unnamed: 4":''})
    team_data[0] = team_data[0].rename(columns = {"Date▼":'Date    '})
    team_data[0] = team_data[0].rename(columns = {"Result":' Result'})    
    team_data_map[team_id] = team_data 

for player_path in player_paths:
    team_id = player_path.split('\\')[-1][0:3]
    #print(team_id)
    player_data = pd.read_html(player_path, flavor='lxml', encoding ='utf-8', header=0, keep_default_na=True, converters=defaultdict(lambda: str))
    player_data[0] = player_data[0].rename(columns = {"Player":'Player    '})    
    player_data_map[team_id] = player_data


all_players_output_file = "allplayers.txt"
all_players_data = []

for path in all_player_paths:
    players_data = pd.read_html(path, flavor='lxml', encoding ='utf-8', header=1, keep_default_na=True, converters=defaultdict(lambda: str))    
    all_players_data.append(players_data)

with open(all_players_output_file, "w") as f:
    pass

with open(all_players_output_file, "w") as f:
        f.write(f"\nData of All players \n\n")
    
for i in all_players_data:
    i[0].to_csv(all_players_output_file, mode = 'a', sep = '\t', index= False, header = True, encoding='utf-8')

all_teams_output_file = "allteams.txt"
all_teams_data = []

for index, path in enumerate(all_teams_paths):
    if index == 0:
        teams_data = pd.read_html(path, flavor='lxml', encoding ='utf-8', header=1, keep_default_na=True, converters=defaultdict(lambda: str))
    else:
        teams_data = pd.read_html(path, flavor='lxml', encoding ='utf-8', header=2, keep_default_na=True, converters=defaultdict(lambda: str))        
    all_teams_data.append(teams_data)

with open(all_teams_output_file, "w") as f:
    pass

with open(all_teams_output_file, "w") as f:
        f.write(f"\nData of All teams games \n\n")
    
for i in all_teams_data:
    i[0].to_csv(all_teams_output_file, mode = 'a', sep = '\t', index= False, header = True, encoding='utf-8')

    
game_size = len(team_file_names)//2

assert len(team_file_names)%2 == 0, "Data files are missing for certain teams. Please check."

games = []

i = 1
while game_size != 0:   
    team1_id, team2_id = input("\nEnter Game_{}'s team1 vs team2 ids using \",\" separator\n".format(i)).split(',')

    key1 = available_teams_map[int(team1_id)]
    key2 = available_teams_map[int(team2_id)]
    games.append(Game(key1, key2))
    game_size -= 1
    i += 1

for index, game in enumerate(games):
    #print(game.team1_id, game.team2_id)
    output_file = "Game {}.txt".format(index+1)

    with open(output_file, mode = 'w') :
        pass
    
    team1 = team_data_map[game.team1_id]
    player1 = player_data_map[game.team1_id]

    team2 = team_data_map[game.team2_id]
    player2 = player_data_map[game.team2_id]

    with open(output_file, mode = 'a', newline ='') as f:
        f.write(f"Players data of \"{teams_map[game.team1_id]}\"\n\n")
    player1[0].to_csv(output_file, mode = 'a', sep = '\t', index= False, header = True, encoding='utf-8')

    
    with open(output_file, mode = 'a', newline ='') as f:
        f.write(f"\n\n\nPlayers data of \"{teams_map[game.team2_id]}\"\n\n")
    player2[0].to_csv(output_file, mode = 'a', sep = '\t', index= False, header = True, encoding='utf-8')

    
    with open(output_file, mode = 'a', newline ='') as f:
        f.write(f"\n\n\nTeam data of \"{teams_map[game.team1_id]}\"\n\n")
    team1[0].to_csv(output_file, mode = 'a', sep = '\t', index= False, header = True, encoding='utf-8')

    
    with open(output_file, mode = 'a', newline ='') as f:
        f.write(f"\n\n\nTeam data of \"{teams_map[game.team2_id]}\"\n\n")
    team2[0].to_csv(output_file, mode = 'a', sep = '\t', index= False, header = True, encoding='utf-8')

    

#data.to_string(output_file, index= False, header = True, encoding='utf-8') #This works but cannot have delimiter
