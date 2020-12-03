# Project

## Installations
```commandline
pip install jupyter
pip install nba_api
```
```commandline
$ jupyter notebook
```
To run the project:
```commandline
$ jupyter notebook NBA_shot_chart.ipynb
```

Required packages:
- [setup.py](https://github.com/JTL66/project/blob/main/setup.py)
- [Jupyter Notebooks](https://github.com/JTL66/project/blob/main/NBA_shot_chart.ipynb) 
   
   -- Some plots and visulization of the players' shot details in Jupyter Notebook.
- [pandas](https://pandas.pydata.org/)
- [requests](https://requests.readthedocs.io/en/master/)
- [matplotlib](https://matplotlib.org/tutorials/introductory/sample_plots.html)
- [seaborn](https://seaborn.pydata.org/)

## Getting Started
- Table of Contents
- 1.1 some imports
    - Imports
        - import pandas as pd
        - import numpy as np
        - import requests
        - import os
        - import jso
        - import seaborn as sns
        - from urllib.request import urlopen
        - import matplotlib as mpl
        - import matplotlib.pyplot as plt
        - from nba_api.stats.endpoints import shotchartdetail
        
- 1.2 dataset
    - [stats.py](https://github.com/JTL66/project/blob/main/stats.py) --'nba_api' is an API Client for 'nba.com' website. We can access the NBA stats very easily by the the API Endpoints. Here calls the players' shot data from it.

After scraping the dataset I clean the data and get the variables that I need.
 
I choose some very typical players meanwhile they're my favorite NBA players. Then I plot the variables to visualize their shot details.

- 2.1
I use the seaborn function to plot players' shot details with LOC_X and LOC_Y two variables to see specific players' shot types.

- 2.2
First I draw the basketball court. Then use matplotlib function to plot the bball_court.

![alt text](https://github.com/JTL66/project/blob/main/bball_court.png "Logo Title Text 3")

- 2.3
Use the request command to get players' photos from the given url.

Stephen Curry: 

![alt text](https://github.com/JTL66/project/blob/main/201939.png "Logo Title Text 1")

Giannis Antetokounmpo: 

![alt text](https://github.com/JTL66/project/blob/main/203507.png "Logo Title Text 2")


- 3
Use joint shot to colormap the players' shot details
I've created two joint shot charts to show the frequenctly shooting area and field goals of Curry and Giannis. It's very easy to tell from the plots that they are two very distinctive players.


### Run the program
To get started developing, clone the repo and `cd` into it.
In an environment where you have not yet installed `nba_api`, then run
```bash
python -m pip install -e .
```
This command will install the package for development, such that any changes you make in the repo will be reflected the next time you import the package in Python.

### Testing
Run `pytest` to verify everything still works.
- [stats.py](https://github.com/JTL66/project/blob/main/stats.py)
- [test_stats.py](https://github.com/JTL66/project/blob/main/test_stats.py)
```bash
pytest
```