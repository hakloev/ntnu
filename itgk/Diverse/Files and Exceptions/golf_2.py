# Golf scores 

golf_file = open('scores.txt', 'r')

line = golf_file.readline()

while line != '':
	score = int(golf_file.readline())
	player = line.rstrip('\n')
	

	print('Player:', player)
	print('Score:', score)

	line = golf_file.readline()

golf_file.close()



