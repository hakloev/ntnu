# Calories Burned
# Håkon Ødegård Løvdal

CAL_BURN = 3.9 

def main():
	print()
	print('This program will tell you how many calories you burn!')
	calories()

def calories():
	print()
	print('Minutes\tCalories')
	print('---------------')

	for minutes in range(10, 31, 5):
		cal = minutes * CAL_BURN
		print(minutes, '\t', cal)

main()