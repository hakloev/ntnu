debug = True

def add(tall1, tall2):
	global debug
	if(debug == True): # legg merke til syntax for å skrive if-setning
		print('Tall1 er', tall1)
		print('Tall2 er', tall2)
	sum = tall1 + tall2
	print(sum)

add(5, 6)

