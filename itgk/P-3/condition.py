# Øving 3 - Oppgave 2
# Håkon Ødegård Løvdal

debug = True #boolsk variabel (flag)

def main():
	first = int(input('Skriv ett heltall: '))
	second = int(input('Skriv ett heltall til: '))
	add(first, second)

def add(first, second):
	total = first + second
	if debug: #hvis debug er sann
		print('Tallene som summeres er {} og {}.' .format(first, second))
		print(total)
	else: #hvis debug er falsk
		print(total)

main()
