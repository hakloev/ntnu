# Distance traveled
# Håkon Ødegård Løvdal

def main():
	print()
	speed = int(input('What is the speed of the vehicle in km/h? '))
	hours = int(input('How many hours has it traveled? '))
	distance(speed, hours)

def distance(speed, hours):
	print()
	print('Hour\tDistance Traveled')
	print('-------------------------')

	for hour in range(1, hours + 1):
		distance = hour * speed
		print(hour, '\t', distance)

main()
