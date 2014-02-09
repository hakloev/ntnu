import random
import os

def main():
	os.system("clear")
	start()

def start():
	user = user_choice()
	comp = computer_choice()
	winner(user, comp)	

def computer_choice():
	computer = random.randint(1,3)
	if computer == 1:
		return 'rock'
	elif computer == 2:
		return'paper'
	else:
		return'scissors'

def user_choice():
	user = str(input('Enter your choice: '))
	return user

def winner(user, comp):
	print("The computer's choice is:", comp)

	if user == 'rock' and comp == 'scissors':
		print('Rock wins, congratulations!')
	elif user == 'scissors' and comp == 'paper':
		print('Scissors wins, congratulations!')
	elif user == 'paper' and comp == 'rock':
		print('Paper wins, congratulation!')
	elif user == comp:
		print("You must play again! It's a tie :)")
		start()
	else:
		print('Too bad, you lose!')

main() 

