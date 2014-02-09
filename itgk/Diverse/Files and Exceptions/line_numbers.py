# Line numbers 

nameOfFile = input("What's the name of the file? ")

user_file = open(nameOfFile, 'r')

line = user_file.readline()

line_number = 1

while line != '':
	line = line.rstrip('\n')
	print('Line ', line_number, ': ', line, sep = '')
	line_number += 1
	line = user_file.readline()

user_file.close()
