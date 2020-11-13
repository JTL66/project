#Some imports
import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt
import os
import json
import seaborn as sns 

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

## get Giannis's data
data1 = data[data['PLAYER_NAME'] == 'Giannis Antetokounmpo']
data1.head()

## get Simmons's data
data2 = data[data['PLAYER_NAME'] == 'Ben Simmons']
data2.head()

## plot the LOC_X and LOC_Y to see the Curry' shot area details
sns.set_style("whitegrid")
sns.set_color_codes()
plt.figure(figsize=(13,10))
plt.scatter(data.LOC_X, data.LOC_Y)
plt.show()

## get the 'Right Side' column from data and plot the LOC_X and LOC_Y to see the players' shot area details
right = data[data.SHOT_ZONE_AREA == "Right Side(R)"]
plt.figure(figsize=(13,10))
plt.scatter(right.LOC_X, right.LOC_Y)
plt.xlim(-300,300)
plt.ylim(-100,500)
plt.show()

## plot the LOC_X and LOC_Y to see the Giannis' shot area details
sns.set_style("whitegrid")
sns.set_color_codes()
plt.figure(figsize=(13,10))
plt.scatter(data1.LOC_X, data1.LOC_Y)
plt.show()

## plot the LOC_X and LOC_Y to see the Simmons' shot area details
sns.set_style("whitegrid")
sns.set_color_codes()
plt.figure(figsize=(13,10))
plt.scatter(data2.LOC_X, data2.LOC_Y)
plt.show()

## try to use request command to get Curry's images from the given url 
import urllib.request
# we pass in the link to the image as the 1st argument
# the second argument tells urlretrieve what we want to get
pic = urllib.request.urlretrieve("http://stats.nba.com/media/players/230x185/201939.png",
                                "201939.png")

# urlretrieve returns a tuple with our image as the first 
# element and ues imread reads then the matplotlib can plot the picture
curry = plt.imread(pic[0])

# plot the picture
plt.imshow(curry)
plt.show()

## try to use request command to get Giannis's images from the given url 
import urllib.request
# we pass in the link to the image as the 1st argument
# the second argument tells urlretrieve what we want to get
pic = urllib.request.urlretrieve("http://stats.nba.com/media/players/230x185/203507.png",
                                "203507.png")

# urlretrieve returns a tuple with our image as the first 
# element and ues imread reads then the matplotlib can plot the picture
ante = plt.imread(pic[0])

# plot the image
plt.imshow(ante)
plt.show()

## try to use request command to get Simmons's images from the given url 
import urllib.request
# we pass in the link to the image as the 1st argument
# the second argument tells urlretrieve what we want to get
pic = urllib.request.urlretrieve("http://stats.nba.com/media/players/230x185/1627732.png",
                                "1627732.png")

# urlretrieve returns a tuple with our image as the first 
# element and ues imread reads then the matplotlib can plot the picture
ben_pic = plt.imread(pic[0])

# plot the image
plt.imshow(ben_pic)
plt.show()

##
