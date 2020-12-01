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

- Table of Contents
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
    - [setup.py](https://github.com/JTL66/project/) -- Some required packages and imports.
    - [scrape.py](https://github.com/JTL66/project/) --'nba_api' is an API Client for 'nba.com' website. We can access the NBA stats very easily by the the API Endpoints. Here calls the players' shot data from it.
    - [Jupyter Notebooks](https://github.com/JTL66/project/) -- Some plots and visulization of the
players' shot details in Jupyter Notebook.

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
# I've created two joint shot charts to show the frequenctly shooting area and field goals of Curry and Giannis. It's easily to tell from the plots that they are two very distinctive players.


