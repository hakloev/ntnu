# Øving 7 - Oppgave 5a
# Håkon Ødegård Løvdal

def main():
	n = int(input('Skriv inn tall: '))
	print(is_prime(n))

def is_prime(tall):
	
	if tall <= 1:
		return False
	elif tall > 1 and tall <= 3:
		return True
	else:
		for x in range(2, tall):
			if tall % x == 0:
				return False
		else:	
			return True		

	# for 0 til seg selv 	

main()