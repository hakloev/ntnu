# Color Mixer
# Håkon Ødegård Løvdal
print()

def main():
	print('In this program you type in red, blue or yellow\n')
	first = str(input('Type the first primary color: '))
	second = str(input('Type the second primary color: '))
	
	if first == "red" or first == "blue" or first == "yellow":
		if second == "red" or second == "blue" or second == "yellow":
			mixer(first, second)
		else:
			print('The second color was no primary color!')
	else:
		print('The first color was no primary color!')

def mixer(first,second):
	print()

	if first == "red" or second == "red":
		if first == "blue" or second == "blue":
			print('Purple')
		elif first == "yellow" or second == "yellow":
			print('Orange')
	elif first == "blue" or second == "blue":
		if first == "yellow" or second == "yellow":
			print('Green')


main()
