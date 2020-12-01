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

## Select Curry's data 
Curry_data = pd.read_csv("curry.csv")
Curry_data.head()
## non-missing value
Curry_data =  curry_data[curry_data['SHOT_MADE_FLAG'].notnull()]


## Select Giannis's data
Giannis_data = pd.read_csv("giannis.csv")
Giannis_data.head()
## non-missing value
Giannis_data = Giannis_data[Giannis_data['SHOT_MADE_FLAG'].notnull()]


