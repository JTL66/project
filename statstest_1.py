import pandas as pd
import numpy as np
import requests
import os
import json 

# Scrape Curry's dataset


url = 'https://stats.nba.com/stats/shotchartdetail'
class Player:

    def scrape_stats(self):
        try:
            response = requests.get(url, params=features, headers=headers)
            if response.status_code == 200:
                content = json.loads(response.content)
                return content
            return None
        except ConnectionError:
            return None

headers = {
		'Host': 'stats.nba.com',
		'Connection': 'keep-alive',
		'Accept': 'application/json, text/plain, */*',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
		'Referer': 'https://stats.nba.com/',
		"x-nba-stats-origin": "stats",
		"x-nba-stats-token": "true",
		'Accept-Encoding': 'gzip, deflate, br',
		'Accept-Language': 'en-US,en;q=0.9',
	}

features = {
	'ContextMeasure': 'FGA',
	'LastNGames': 0,
	'LeagueID': '00',
	'Month': 0,
	'OpponentTeamID': 0,
	'Period': 0,
	'PlayerID': 201939, # Stephen Curry's ID
	'SeasonType': 'Regular Season',
	'TeamID': 0,
	'VsDivision': '',
	'VsConference': '',
	'SeasonSegment': '',
	'Season': '2018-19',
	'RookieYear': '',
	'PlayerPosition': '',
	'Outcome': '',
	'Location': '',
	'GameSegment': '',
	'GameId': '',
	'DateTo': '',
	'DateFrom': ''
}

response = requests.get(url, params=features, headers=headers)
content = json.loads(response.content)
# transform contents into df
results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
df = pd.DataFrame(rows)
df.columns = headers


print(Player.scrape_stats)