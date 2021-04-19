#Load in Statsbomb competition and match data
#This is a library for loading json files.
import json


my_path = 'C:/Users/victo/Desktop/Datascience/Projects/Football/SoccermaticsForPython-master/Wyscout/'
#Load the competition file
with open(my_path + 'Statsbomb/data/competitions.json') as f:
    competitions = json.load(f)
    
#Womens World Cup 2019 has competition ID 72
competition_id=11

#Load the list of matches for this competition
with open(my_path + 'Statsbomb/data/matches/'+str(competition_id)+'/42.json') as f:
    matches = json.load(f)

#Look inside matches
matches[0]
matches[0]['home_team']
matches[0]['home_team']['home_team_name']
matches[0]['away_team']['away_team_name']

#Print all match results
for match in matches:
    home_team_name=match['home_team']['home_team_name']
    away_team_name=match['away_team']['away_team_name']
    home_score=match['home_score']
    away_score=match['away_score']
    describe_text = 'The match between ' + home_team_name + ' and ' + away_team_name
    result_text = ' finished ' + str(home_score) +  ' : ' + str(away_score)
    print(describe_text + result_text)

#Now lets find a match we are interested in
home_team_required ="Real Madrid"
away_team_required ="Barcelona"

#Find ID for the match
for match in matches:
    home_team_name=match['home_team']['home_team_name']
    away_team_name=match['away_team']['away_team_name']
    if (home_team_name==home_team_required) and (away_team_name==away_team_required):
        match_id_required = match['match_id']
print(home_team_required + ' vs ' + away_team_required + ' has id:' + str(match_id_required))


for match in matches:
    if match['match_id'] == 303596:
        x = match 
        print(x)
#Find Sweden matches
team = 'Real Madrid'
for match in matches:
    home_team_name=match['home_team']['home_team_name']
    away_team_name=match['away_team']['away_team_name']
    home_score=match['home_score']
    away_score=match['away_score']
    if (home_team_name == team) or (away_team_name == team):
       describe_text = 'The match between ' + home_team_name + ' and ' + away_team_name
       result_text = ' finished ' + str(home_score) +  ' : ' + str(away_score)
       print(describe_text + result_text)
       















