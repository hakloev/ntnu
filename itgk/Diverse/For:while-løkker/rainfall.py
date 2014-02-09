# Average Rainfall
# Håkon Ødegård Løvdal

MONTHS = 12 # Global constant (always 12 months in a year)
months_total = 0
# Get's number of years to calculate average from
num_years = int(input('How many years? '))
print() # Seperate input and first itteration

# Determine each years average
for year in range(num_years):
	# Initialize an accumulator for average 
	total = 0.0

	print('Year', year + 1)
	print('------------------')	
	# Get each years monthly rain
	for month in range(MONTHS):
		print('Month', month + 1, end='')
		rained = float(input(': '))
		total += rained # total = total + rained

	# Calculate average
	average = total / MONTHS

	# Display average 
	print('The average =', average)
	print()

