# File display

num_file = open('numbers.txt', 'r')

line = num_file.readline()

while line != '':
	num = int(line)
	print(num)
	line = num_file.readline()

num_file.close()