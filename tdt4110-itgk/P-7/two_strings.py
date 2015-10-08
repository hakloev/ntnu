# Øving 7 - Oppgave 6d
# Håkon Ødegård Løvdal

def in_string(string1, string2):
	position = string1.find(string2)
	if position != -1:
		return position
	else:
		return False



print(in_string('jeg er julenissen', 'julenissen'))
