# Øving 7 - Oppgave 6a
# Håkon Ødegård Løvdal

def main():
	string1 = 'elementer'
	string2 = 'elementer'
	print(same_string(string1, string2))

def same_string(string1, string2):
	index = 0
	while index < len(string1):
		if string1[index] == string2[index]:
			index += 1
		else:
			return False
	return True

main()

#evnt liste vs liste
#evnt string1 is string2