# Some imports
import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt
import os
import json
import seaborn as sns 

## Read data

data = pd.read_csv("nbashot19.csv")
print(data.shape)
data.head() #head the first 5 rows

## non-missing value
data =  data[data['SHOT_MADE_FLAG'].notnull()]
print(data.shape)

## get Curry's data
data = data[data['PLAYER_NAME'] == 'Stephen Curry']
data.head()

## get Giannis's data
data1 = data[data['PLAYER_NAME'] == 'Giannis Antetokounmpo']
data1.head()
