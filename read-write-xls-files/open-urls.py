import webbrowser

param_map = {
    "cavaliers" : "CLE", 
    "pistons" : "DET",
    "spurs" : "SAS",
    "hawks" : "ATL",
    "bucks" : "MIL", 
    "hornets": "CHA", 
    "grizzlies" :"MEM", 
    "raptors" : "TOR", 
    "heat" :"MIA", 
    "67ers" :"PHI", 
    "wizards" :"WAS", 
    "nets" :"NJN", 
    "bulls" :"CHI", 
    "timberwolves" :"MIN", 
    "warriors" :"GSW", 
    "jazz" :"UTA", 
    "pelicans" :"NOH", 
    "nuggets" :"DEN", 
    "suns" : "PHO", 
    "thunder" :"OKC", 
    "magic" :"ORL", 
    "kings" :"SAC", 
    "rockets" :"HOU", 
    "mavericks" :"DAL", 
    "pacers" :"IND", 
    "lakers" :"LAL", 
    "celtics" :"BOS", 
    "blazers" :"POR", 
    "knicks":"NYK",
    "clippers": "LAC"
}


number_of_games = input("How many games?")

number_of_games = int(number_of_games)

current_teams_urls = []
current_players_urls = []

for x in range(1,number_of_games*2+1):
    team_name = input("Team name: ")
    team_name = str(team_name).lower()
    if team_name in param_map:
        game_id = param_map[team_name]
        current_teams_urls.append("https://stathead.com/basketball/team-game-finder.cgi?request=1&order_by=diff_off_rtg&timeframe=seasons&year_min=2025&year_max=2025&team_id=" + game_id)
        current_players_urls.append("https://stathead.com/basketball/player-season-finder.cgi?request=1&order_by=name_display_csk&year_min=2025&year_max=2025&team_id=" + game_id) 
    else:
        print("Couldn't find game id, Please check name or update ids.")
    
for url in current_teams_urls:
    webbrowser.open(url)

for url in current_players_urls:
    webbrowser.open(url)


print("hello world")

