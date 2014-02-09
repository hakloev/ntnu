# Øving 7 - Oppgave 5b
# Håkon Ødegård Løvdal

def main():
	tall = [1, 2, 3, 4, 5, 10, 15, 20, 30, 35, 100]
	threshold = int(input('Enter threshold: '))
	print(separate(tall, threshold))

def separate(tall, threshold):
	less = []
	greather = []
	for num in tall:
		if num >= threshold:
			greather.append(num)
		else:
			less.append(num)
	return less, greather

main()	