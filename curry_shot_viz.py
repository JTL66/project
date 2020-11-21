# Some imports
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
sns.set_style("white")
sns.set_color_codes()
import urllib.request
# I pass in the link to the picture as the first argument
# urlretrieve will get the picture that I want at the second argument 
pic = urllib.request.urlretrieve("http://stats.nba.com/media/players/230x185/201939.png",
                                "201939.png") # this is the url where I get the pictures

# urlretrieve returns a tuple with the picture as the first element 
curry = plt.imread(pic[0]) # # ues imread reads Stephen Curry's picture

# use matplotlib to plot the picture
plt.imshow(curry)
plt.show()

## try to use request command to get Giannis's picture from the given url 
import urllib.request
# we pass in the link to the image as the 1st argument
# the second argument tells urlretrieve what we want to get
pic = urllib.request.urlretrieve("http://stats.nba.com/media/players/230x185/203507.png",
                                "203507.png") # this is the url where I get the pictures

# urlretrieve returns a tuple with the picture as the first element 
ante = plt.imread(pic[0]) # ues imread reads Giannis Antetokounmpo's picture

# use matplotlib to plot the picture
plt.imshow(ante)
plt.show()

## try to use request command to get Simmons's images from the given url 
import urllib.request
pic = urllib.request.urlretrieve("http://stats.nba.com/media/players/230x185/1627732.png",
                                "1627732.png") # this is the url where I get the pictures

# urlretrieve returns a tuple with the picture as the first element 
ben_pic = plt.imread(pic[0]) # ues imread reads Ben Simmons's picture

# plot the image
plt.imshow(ben_pic)
plt.show()

## use matplotlib to draw the basketball court
# import
from matplotlib.patches import Circle, Rectangle, Arc
# write def function
def draw_court(ax=None, color='black', lw=3, outer_lines=False):
    # If an axes object isn't provided to plot onto, just get current one
    if ax is None:
        ax = plt.gca()

    # Create the basketball hoop
    # The radius of the hoop is 9
    hoop = Circle((0, 0), radius=9, linewidth=lw, color=color, fill=False)

    # Create backboard
    backboard = Rectangle((-30, -9), 60, -1, linewidth=lw, color=color)

    # The paint
    # Create the outer box 0f the paint, width=16ft, height=19ft
    outer_box = Rectangle((-80, -49), 160, 190, linewidth=lw, color=color,
                          fill=False)
    # Create the inner box of the paint, widt=12ft, height=19ft
    inner_box = Rectangle((-60, -49), 120, 190, linewidth=lw, color=color,
                          fill=False)

    # Create free throw top arc
    top_free_throw = Arc((0, 142.5), 120, 120, theta1=0, theta2=180,
                         linewidth=lw, color=color, fill=False)
    # Create free throw bottom arc
    bottom_free_throw = Arc((0, 142.5), 120, 120, theta1=180, theta2=0,
                            linewidth=lw, color=color, linestyle='dashed')
    # Restricted Zone, it is an arc with 4ft radius from center of the hoop
    restricted = Arc((0, 0), 80, 80, theta1=0, theta2=180, linewidth=lw,
                     color=color)

    # Three point line
    # Create the side 3pt lines, they are 14ft long before they begin to arc
    corner_three_a = Rectangle((-220, -49), 0, 140, linewidth=lw,
                               color=color)
    corner_three_b = Rectangle((220, -49), 0, 140, linewidth=lw, color=color)
    # 3pt arc - center of arc will be the hoop, arc is 23'9" away from hoop
    # I just played around with the theta values until they lined up with the 
    # threes
    three_arc = Arc((0, 0), 475, 475, theta1=22, theta2=158, linewidth=lw,
                    color=color)

    # Center Court
    center_outer_arc = Arc((0, 422.5), 120, 120, theta1=180, theta2=0,
                           linewidth=lw, color=color)
    center_inner_arc = Arc((0, 422.5), 40, 40, theta1=180, theta2=0,
                           linewidth=lw, color=color)

    # List of the court elements to be plotted onto the axes
    court_elements = [hoop, backboard, outer_box, inner_box, top_free_throw,
                      bottom_free_throw, restricted, corner_three_a,
                      corner_three_b, three_arc, center_outer_arc,
                      center_inner_arc]

    if outer_lines:
        # Draw the half court line, baseline and side out bound lines
        outer_lines = Rectangle((-250, -49), 500, 470, linewidth=lw,
                                color=color, fill=False)
        court_elements.append(outer_lines)

    # Add the court elements onto the axes
    for element in court_elements:
        ax.add_patch(element)

    return ax

plt.figure(figsize=(13,10))
draw_court(outer_lines=True)
plt.xlim(-300,300)
plt.ylim(-100,500)
plt.show()
