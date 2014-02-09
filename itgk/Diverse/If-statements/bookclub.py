# Book club points
# Håkon Ødegård Løvdal

def main():
	books = int(input('How many books did you buy this month? '))
	points(books)

def points(book):
	if book == 0:
		print('0 points')
	elif book == 1:
		print('5 points')
	elif book == 2:
		print('15 points')
	elif book == 3: 
		print('30 points')
	elif book >= 4:
		print('60 points')


main()