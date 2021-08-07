game = {'color' : 'green' , 'points':1}
print(game['color'])
print(game['points'])
print("_____________________________\n")

#Strating with an empty dictonary
game_new = {}
game_new['points'] = 1
game_new['color'] = 'yellow'
game_new['player'] = 'maaitrayo'
print(game_new)
print("_____________________________\n")

#The alien game
alien_game = {'x_position':0, 'y_position':0,'speed':'medium'}
print("The original speed of the alien is: "+alien_game['speed'])

if alien_game['speed'] == 'slow':
    x_increment = 1
elif alien_game['speed'] == 'medium':
    x_increment = 5
else:
    x_increment = 10

alien_game['x_position'] = alien_game['x_position']+x_increment
print("New alien speed: "+str(alien_game['x_position']))
