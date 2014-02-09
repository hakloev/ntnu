# Golf scores 

another = 'y'

golf_file = open('scores.txt', 'a')

while another == 'y' or another == 'Y':
	print('Enter player name and score: \n')
	player = input('Player name: ')
	score = input('What is his/her score: ')

	golf_file.write(player + '\n')
	golf_file.write(score + '\n')

	another = input('Any more players to add? ')

golf_file.close()
print('Data appended to scores.txt')

