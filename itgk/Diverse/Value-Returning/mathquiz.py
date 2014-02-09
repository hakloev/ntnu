import random

def main():
	a, b = randomnumber()
	print('  ', a, '\n', '+', b)
	answer = int(input(' = '))
	answer_true = a + b 
	if answer == answer_true:
		print('Congratulations')
	else:
		print('Sorry, the correct answer is', answer_true)

def randomnumber():
	a = random.randint(0, 300)
	b = random.randint(0, 300)
	return a, b

main()