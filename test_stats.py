import requests
from stats import scrape_stats

def test_stats():
	url = 'https://stats.nba.com/stats/shotchartdetail'
	response = requests.get(url)
	assert response.status_code == 200
	






