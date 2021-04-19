# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 15:48:00 2020

@author: victo

Homeworks for the online course of Laurie Shaw (@EightyFivePoint)
"""

import Metrica_IO as mio
import Metrica_Viz as mviz
import numpy as np
import pandas as pd
import Metrica_Velocities as mvel

"""
The modules Metrica_IO. ,metrica_Viz, and Metrica_velocities are taken from 
Laurie Shaw (@EightyFivePoint)

Data can be found at: https://github.com/metrica-sports/sample-data
"""


# set up initial path to data
DATADIR = r"C:\Users\victo\Desktop\Datascience\Projects\Football\LaurieOnTracking-master\sample-data-master\data"
game_id = 2 # let's look at sample match 2

# read in the event data
events = mio.read_event_data(DATADIR,game_id)

# count the number of each event type in the data
print( events['Type'].value_counts() )

# Bit of housekeeping: unit conversion from metric data units to meters
events = mio.to_metric_coordinates(events)

# Get events by team
home_events = events[events['Team']=='Home']
away_events = events[events['Team']=='Away']

# Frequency of each event type by team
home_events['Type'].value_counts()
away_events['Type'].value_counts()

# Get all shots
shots = events[events['Type']=='SHOT']
home_shots = home_events[home_events.Type=='SHOT']
away_shots = away_events[away_events.Type=='SHOT']

# Look at frequency of each shot Subtype
home_shots['Subtype'].value_counts()
away_shots['Subtype'].value_counts()

# Look at the number of shots taken by each home player
print( home_shots['From'].value_counts() )

# Get the shots that led to a goal
home_goals = home_shots[home_shots['Subtype'].str.contains('-GOAL')].copy()
away_goals = away_shots[away_shots['Subtype'].str.contains('-GOAL')].copy()

# Add a column event 'Minute' to the data frame
home_goals['Minute'] = home_goals['Start Time [s]']/60.
away_goals['Minute'] = away_goals['Start Time [s]']/60.
# Plot the first goal
fig,ax = mviz.plot_pitch()
ax.plot( events.loc[198]['Start X'], events.loc[198]['Start Y'], 'ro' )
ax.annotate("", xy=events.loc[198][['End X','End Y']], xytext=events.loc[198][['Start X','Start Y']], alpha=0.6, arrowprops=dict(arrowstyle="->",color='r'))

# plot passing move in run up to goal
mviz.plot_events( events.loc[190:198], indicators = ['Marker','Arrow'], annotate=True )

#### TRACKING DATA ####

# READING IN TRACKING DATA
tracking_home = mio.tracking_data(DATADIR,game_id,'Home')
tracking_away = mio.tracking_data(DATADIR,game_id,'Away')

# Look at the column namems
print( tracking_home.columns )

# Convert positions from metrica units to meters 
tracking_home = mio.to_metric_coordinates(tracking_home)
tracking_away = mio.to_metric_coordinates(tracking_away)

# Plot some player trajectories (players 11,1,2,3,4)
fig,ax = mviz.plot_pitch()
ax.plot( tracking_home['Home_11_x'].iloc[:1500], tracking_home['Home_11_y'].iloc[:1500], 'r.', MarkerSize=1)
ax.plot( tracking_home['Home_1_x'].iloc[:1500], tracking_home['Home_1_y'].iloc[:1500], 'b.', MarkerSize=1)
ax.plot( tracking_home['Home_2_x'].iloc[:1500], tracking_home['Home_2_y'].iloc[:1500], 'g.', MarkerSize=1)
ax.plot( tracking_home['Home_3_x'].iloc[:1500], tracking_home['Home_3_y'].iloc[:1500], 'k.', MarkerSize=1)
ax.plot( tracking_home['Home_4_x'].iloc[:1500], tracking_home['Home_4_y'].iloc[:1500], 'b.', MarkerSize=1)

# plot player positions at ,atckick-off
KO_Frame = events.loc[0]['Start Frame']
fig,ax = mviz.plot_frame( tracking_home.loc[KO_Frame], tracking_away.loc[KO_Frame] )

# PLOT POISTIONS AT GOAL
fig,ax = mviz.plot_events( events.loc[198:198], indicators = ['Marker','Arrow'], annotate=True )
goal_frame = events.loc[198]['Start Frame']
fig,ax = mviz.plot_frame( tracking_home.loc[goal_frame], tracking_away.loc[goal_frame], figax = (fig,ax) )


# READING IN TRACKING DATA
tracking_home = mio.tracking_data(DATADIR,game_id,'Home')
tracking_away = mio.tracking_data(DATADIR,game_id,'Away')
tracking_home = mvel.calc_player_velocities(tracking_home, smoothing = True)
tracking_away = mvel.calc_player_velocities(tracking_away, smoothing = True)

# PLOT THE PASSES AND SHOT LEADING UP TO THE SECOND AND THIRD GOALS IN THE MATCH
fig,ax = mviz.plot_pitch()
ax.plot( events.loc[823]['Start X'], events.loc[823]['Start Y'], 'ro' )
ax.annotate("", xy=events.loc[823][['End X','End Y']], xytext=events.loc[823][['Start X','Start Y']], alpha=0.6, arrowprops=dict(arrowstyle="->",color='r'))
mviz.plot_events( events.loc[819:823], indicators = ['Marker','Arrow'], annotate=True )


# PLOT ALL THE SHOTS BY PLAYER 9 OG TH E HOME TEAM. USE A DIFFERENT SYMBOL AND TRANSPARENCY FOR SHOTS THAT RESULTED IN GOALS
home_events = events[events['Team']=='Home']
shots = events[events['Type']=='SHOT']
home_shots = home_events[home_events.Type=='SHOT']


plot_9 = home_shots[home_shots.From == 'Player9']

fig,ax = mviz.plot_pitch()
for i,shot in plot_9.iterrows():
    if 'GOAL' in shot['Subtype']:
        ax.plot(shot['Start X'], shot['Start Y'], 'bo' )
        ax.annotate("", xy = shot[['End X', 'End Y']], xytext = shot[['Start X','Start Y']],alpha= 0.9, arrowprops=dict(arrowstyle="->",color='b'))
    else:
        ax.plot( shot['Start X'], shot['Start Y'], 'bo', alpha = 0.2)
        

# PLOT THE POSITION OF ALL PLAYERS AT PLAYER 9'S GOAL 
# Convert positions from metrica units to meters 
tracking_home = mio.to_metric_coordinates(tracking_home)

fig,ax = mviz.plot_events( events.loc[1118:1118], indicators = ['Marker','Arrow'], annotate=True )
goal_frame = events.loc[1118]['Start Frame']
fig,ax = mviz.plot_frame( tracking_home.loc[goal_frame], tracking_away.loc[goal_frame], figax = (fig,ax) )


# CALCULATE HOW FAR EACH PLAYER RUN
teams = ['Home','Away']
data = [tracking_home, tracking_away]
for name,data in zip(teams, data):
    team_players = np.unique([c.split('_')[1] for c in data.columns if c[:4] == name])
    team_summary = pd.DataFrame(index=team_players)

distance = [] 
for player in team_summary.index:
    column = name + '_' + player + '_speed'
    player_distance = data[column].sum()/25./1000
    distance.append(player_distance)

team_summary['Distance in kms'] = distance
team_summary = team_summary.sort_values(['Distance in kms'], ascending=False)



print('****** ' + name + " team sumary  *************")
team_summary


