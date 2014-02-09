# Item Counter

name_file = open('names.txt', 'r')

items = 0

line = name_file.readline()

while line != '':
	items += 1
	line = name_file.readline()

name_file.close()

print('names.txt contains', items, 'names')


