"""
This project it jupyter notebook based. Open with Github Desktop and open in 
Visual Studio Code. 
"""
"""
#Some installments
pip install jupyter
pip install pandas
pip intsall requests
pip install matplotlib
pip install seaborn
pip install nba_api
"""
# Please have these commands installed and import 
import pandas as pd
import numpy as np
import requests
import os
import json
import seaborn as sns
from urllib.request import urlopen
import matplotlib as mpl
import matplotlib.pyplot as plt
from nba_api.stats.endpoints import shotchartdetail 

## Read data
data = pd.read_csv("nbashot19.csv")
data.head() #head the first 5 rows

## non-missing value
data =  data[data['SHOT_MADE_FLAG'].notnull()]

## Select Curry's data 
Curry_data = data[data['PLAYER_NAME'] == 'Stephen Curry']
Curry_data.head()

## Select Giannis's data
Giannis_data = data[data['PLAYER_NAME'] == 'Giannis Antetokounmpo']
Giannis_data.head()

## Select Simmons's data
Simmons_data = data[data['PLAYER_NAME'] == 'Ben Simmons']
Simmons_data.head()