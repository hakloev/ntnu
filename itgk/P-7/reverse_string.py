# Øving 7 - Oppgave 6b
# Håkon Ødegård Løvdal

def reverse_string(string):
	word = []
	for ch in string:
		word.append(ch)
	word.reverse()
	
	new_string = ""
	for ch in word:
		new_string += ch
	return new_string

