# Sum of numbers

num_file = open('numbers.txt', 'r')

total = 0

for line in num_file:
	num = int(line)
	total += num

num_file.close()

print(total)