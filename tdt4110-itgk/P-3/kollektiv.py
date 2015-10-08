# Øving 3 - Oppgave 4
# Håkon Ødegård Løvdal

def ticket(): 
	alder = int(input('Hvor gammel er du? '))

	if alder < 5:
		print('Småbarn: Gratis')
	elif alder >= 5 and alder <= 15:
		print('Barn: 10 kr')
	elif alder >= 16 and alder <= 20:
		print('Ungdom: 20 kr')
	elif alder >= 21 and alder <= 25:
		print('Student: 30 kr')
	elif alder >= 26 and alder <= 60:
		print('Voksen: 40 kr')
	elif alder > 60:
		print('Honnør: Gratis')

ticket()
