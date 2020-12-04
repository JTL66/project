from stats import scrape_stats

def test_stats():
	assert scrape_stats("https://stats.nba.com/stats/shotchartdetail") == True
	






