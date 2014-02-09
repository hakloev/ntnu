#Rainfall Statistics

MONTHS = 12

def rainfall():
	global MONTHS
	rainfallInMonths = []
	index = 0
	total = 0

	# Get user input
	while index < 12:
		index += 1
		print('Enter the rainfall for the ', index, ' month: ', sep='', end='')
		rain_user = float(input())
		rainfallInMonths.append(rain_user)

	# Calculate total rainfall
	for rain in rainfallInMonths:
		total += rain

	print('Total rainfall:', total)
	print('Average rainfall:', total / index)
	print('Highest rainfall:', max(rainfallInMonths))
	print('Lowest rainfall:', min(rainfallInMonths))




rainfall()
