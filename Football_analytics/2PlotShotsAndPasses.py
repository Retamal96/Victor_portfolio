#Make a shot map and a pass map using Statsbomb data
#Set match id in match_id_required.

#Function to draw the pitch
import matplotlib.pyplot as plt
import numpy as np

my_path = 'C:/Users/victo/Desktop/Datascience/Projects/Football/SoccermaticsForPython-master/Wyscout/'

#Size of the pitch in yards (!!!)
pitchLengthX=120
pitchWidthY=80

#ID for Real Madrid" vs Barcelona
match_id_required = 303470
home_team_required ="Real Madrid"
away_team_required ="Barcelona"

# Load in the data
# I took this from https://znstrider.github.io/2018-11-11-Getting-Started-with-StatsBomb-Data/
file_name=str(match_id_required)+'.json'

#Load in all match events 
import json
with open(my_path + 'Statsbomb/data/events/'+file_name) as data_file:
    #print (mypath+'events/'+file)
    data = json.load(data_file)

#get the nested structure into a dataframe 
#store the dataframe in a dictionary with the match id as key (remove '.json' from string)
from pandas.io.json import json_normalize
df = json_normalize(data, sep = "_").assign(match_id = file_name[:-5])

#A dataframe of shots
shots = df.loc[df['type_name'] == 'Shot'].set_index('id')
    
#Draw the pitch
from FCPython import createPitch
(fig,ax) = createPitch(pitchLengthX,pitchWidthY,'yards','gray')

#Plot the shots
for i,shot in shots.iterrows():
    x=shot['location'][0]
    y=shot['location'][1]
    
    goal=shot['shot_outcome_name']=='Goal'
    team_name=shot['team_name']
    
    #circleSize=2
    circleSize=np.sqrt(shot['shot_statsbomb_xg'])*12

    if (team_name==home_team_required):
        if goal:
            shotCircle=plt.Circle((x,pitchWidthY-y),circleSize,color="red")
            plt.text((x+1),pitchWidthY-y+1,shot['player_name']) 
        else:
            shotCircle=plt.Circle((x,pitchWidthY-y),circleSize,color="red")     
            shotCircle.set_alpha(.2)
    elif (team_name==away_team_required):
        if goal:
            shotCircle=plt.Circle((pitchLengthX-x,y),circleSize,color="blue") 
            plt.text((pitchLengthX-x+1),y+1,shot['player_name']) 
        else:
            shotCircle=plt.Circle((pitchLengthX-x,y),circleSize,color="blue")      
            shotCircle.set_alpha(.2)
    ax.add_patch(shotCircle)
    
    
plt.text(5,75,away_team_required + ' shots') 
plt.text(80,75,home_team_required + ' shots') 
     
fig.set_size_inches(10, 7)
fig.savefig('Output/shots.pdf', dpi=100) 
plt.show()


#Create a dataframe of passes which contains all the passes in the match
passes = df.loc[df['type_name'] == 'Pass'].set_index('id')

#Plot the start point of every Real Madrid pass. Attacking left to right.
from FCPython import createPitch
(fig,ax) = createPitch(pitchLengthX,pitchWidthY,'yards','gray')

for i, pax in passes.iterrows():
    x = pax['location'][0]
    y = pax['location'][1]
    team_name = pax['team_name']
    if (team_name=='Real Madrid'):
       PassCircle=plt.Circle((x,pitchWidthY-y),0.05,color="red")     
       PassCircle.set_alpha(1)
    ax.add_patch(PassCircle)
    
    
fig.set_size_inches(10, 7)
fig.savefig('Output/Passes.pdf', dpi=100) 
plt.show()

#Plot only passes made by Casemiro (he is Carlos Henrique Casimiro in the database)
#Draw the pitch
(fig,ax) = createPitch(pitchLengthX,pitchWidthY,'yards','gray')
for i,thepass in passes.iterrows():
    #if thepass['team_name']==away_team_required: #
    if thepass['player_name']=='Carlos Henrique Casimiro':
        x=thepass['location'][0]
        y=thepass['location'][1]
        passCircle=plt.Circle((x,pitchWidthY-y),2,color="blue")      
        passCircle.set_alpha(.2)   
        ax.add_patch(passCircle)
        dx=thepass['pass_end_location'][0]-x
        dy=thepass['pass_end_location'][1]-y

#Draw arrows
        passArrow=plt.Arrow(x,pitchWidthY-y,dx,-dy,width=3,color="blue")
        ax.add_patch(passArrow)

fig.set_size_inches(10, 7)
#fig.savefig('Output/passes.pdf', dpi=100) 
plt.text(80,75,  'Carlos Henrique Casimiro passes') 
    
    
fig.set_size_inches(10, 7)
fig.savefig('Output/Casemiro_passes.pdf', dpi=100) 
plt.show()









