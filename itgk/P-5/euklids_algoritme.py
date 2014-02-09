# Øving 5 - Oppgave 3
# Håkon Ødegård Løvdal

def main():
	a, b = reduce_fraction()
	print(a, '/', b, sep = '')
	


def gcd(a, b): # greatest common divisor
	while b != 0: 
		gammel_b = b
		b = (a % b)
		a = gammel_b
	return gammel_b
	

def reduce_fraction():
	a = int(input('Teller: '))
	b = int(input('Nevner: '))
	devisor = gcd(a, b)
	return int((a / devisor)), int((b / devisor))

main()
