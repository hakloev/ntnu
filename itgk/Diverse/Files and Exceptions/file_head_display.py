# File head display

file_name = input("What's the name of the file? ")

user_file = open(file_name, 'r')

count = 1

line = user_file.readline()

while line != '':
	if count <= 5:
		line = line.rstrip('\n')
		print(line)
		count += 1
		line = user_file.readline()
	else:
		break

user_file.close()