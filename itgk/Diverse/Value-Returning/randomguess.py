import random

def game_turns():
	turn = 0
	game = True
	while game == True:
		rand_guess()
		turn += 1
		if turn == 1:
			print('You have played', turn, 'time!')
		else: 
			print('You have played', turn, 'times!')			
		end = str(input('Do you wanna quit? '))
		if end == "y" or end == "Y":
			game = False



def rand_guess():
	secret_number = random.randint(0,100)
	numberOfGuesses = 0
	guess = False

	while guess == False:
		print()
		guess_user = int(input('Guess a number: '))
		if guess_user > secret_number:
			print('Too high, try again!')
		elif guess_user < secret_number:
			print('Too low, try again!')
		elif guess_user == secret_number:
			print()
			print('Congratulations')
			guess = True 
		numberOfGuesses += 1
	print('You used', numberOfGuesses, 'tries to find the number!')

game_turns()