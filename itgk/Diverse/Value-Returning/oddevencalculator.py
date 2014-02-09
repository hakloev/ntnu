import random

def main():

	count = 0
	even = 0
	odd = 0

	while count <= 99:
		num = random.randint(0, 500)
		if is_even(num):
			even += 1
		else:
			odd += 1
		count += 1
	print(even, odd)

def is_even(num):
	if (num % 2) == 0:
		status = True
	else: 
		status = False
	return status

main()
