# Random Number File Writer 

import random

rand_file = open('rand_nums.txt', 'w')

total_randints = int(input('How many random integers to add: '))

for i in range(1, total_randints + 1):
	rand = random.randint(1, 101)
	rand_file.write(str(rand) + '\n')

rand_file.close()
 
print('Random integers added to rand_nums.txt')