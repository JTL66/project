# Please have these command installed and import 
import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt
import os
import json
import seaborn as sns 

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