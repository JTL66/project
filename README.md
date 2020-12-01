# project Discription
# Monitor and visualize the NBA player shot with python
# I've tried to scrape NBA players dataset from either stats.nba.com or https://www.basketball-reference.com.
# Clean the data and then extract the variables that I need.
# Plotting the data and analyzing the player.

# Dataset nbashot_19.csv was uploaded. The csv file needs to be downloaded before running the codes below.
# This dataset covers NBA games that played between Season 2018 to 2019.

# Run the program

## Installations
```commandline
pip install jupyter
pip install nba_api
```
Required packages:
- [pandas](https://pandas.pydata.org/) (optional)
- [requests](https://requests.readthedocs.io/en/master/)
- [matplotlib] 
- [seaborn] 

## Project

- [Table of Contents]
- 1.1 some imports
    - Imports
        - [setup.py]
        - import pandas as pd
        - import numpy as np
        - import requests
        - import os
        - import json
        - import seaborn as sns
        - from urllib.request import urlopen
        - import matplotlib as mpl
        - import matplotlib.pyplot as plt
        - from nba_api.stats.endpoints import shotchartdetail
        

- 1.2 dataset
    - [scrape.py]()
'nba_api' is an API Client for 'nba.com' website. We can access the NBA stats very easily by the the API Endpoints.

After scraping the dataset I clean the data and get the variables that I need.
 
I choose some very typical players meanwhile they're my favorite NBA players. Then I plot the variables to visualize their shot details.

# 2.1.
# use use seaborn function to plot players' shot details with LOC_X and LOC_Y two variables to see specific players' shot area details

# 2.2
# draw the basketball court

# 2.3
# use the request command to get players' photos from the given url

# 3
# use joint shot to colormap the players' shot details
# I've created two joint shot charts to show the frequenctly shooting area and field goals of Curry and Giannis. It's easily to tell they are two very distinctive players.

# 4
# I would also want to get their field goal rate and plot them onto thr courts to trace the way they shoot and how good they are in the specific areas.
