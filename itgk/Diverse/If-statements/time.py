# Time Calculator
# Håkon Ødegård Løvdal	

def main():
	second = int(input('Enter a number of seconds: '))
	calc(second)

def calc(time):
	if time >= 60 and time < 3600:
		minutes = time / 60
		print(minutes, 'minutes')
	elif time >= 3600 and time < 86400:
		hour = time / 3600
		print(hour, 'hours')
	elif time >= 86400:
		days = time / 86400
		print(days, 'days')
	else: 
		print(time, 'seconds')

main()


