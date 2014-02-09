# Average of Numbers 
total = 0
num_lines = 0
try:
	num_file = open('numbers.txt', 'r')
	for line in num_file:
		num_lines += 1
		integer = int(line)
		total += integer
	num_file.close()
	average = total / num_lines
	print(average)
except IOError:
	print('This caused an IOError')
except ValueError:
	print('This caused an ValueError')