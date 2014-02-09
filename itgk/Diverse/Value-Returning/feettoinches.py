# One foot equals 12 inches
def main():
	feet = float(input('How many feet? '))
	print(feet, 'feet equals', format(feet_to_inches(feet), '.2f'), 'inches')

def feet_to_inches(feet):
	return feet * 12

main()