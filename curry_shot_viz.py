## some imports

import pandas as pd
import numpy as np

## Read data

data = pd.read_csv("nba_shotchartdetail_18_19.csv")
print(data.shape)
data.head() #head the first 5 rows

## non-missing value
data =  data[data['SHOT_MADE_FLAG'].notnull()]
print(data.shape)

## get Curry's data
data = data[data['PLAYER_NAME'] == 'Stephen Curry']
data.head()




