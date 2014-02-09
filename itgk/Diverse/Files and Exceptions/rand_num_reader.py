# Random Number File Reader

rand_file = open('rand_nums.txt', 'r')

total = 0
number_of_randint = 0

for line in rand_file:
	number_of_randint += 1
	num = int(line)
	total += num

rand_file.close()

print('The total of the random integeres is:', total)
print('It was', number_of_randint, 'random integeres in the file')