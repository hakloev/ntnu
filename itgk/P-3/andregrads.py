# Øving 3 - Oppgave 5
# Håkon Ødegård Løvdal

def main():
	a = int(input('Skriv inn a: '))
	b = int(input('Skriv inn b: '))
	c = int(input('Skriv inn c: '))
	calc(a, b, c)

def calc(a, b, c):
	d = (b ** 2) - (4 * a * c)

	if d < 0:
		print('Likningen {}x^2 + {}x + {} = 0 har to imaginære løsninger.' .format(a, b, c))
	elif d > 0:
		print('Likningen {}x^2 + {}x + {} = 0 har to reelle løsninger.' .format(a, b, c))
	elif d == 0:
		print('Likningen {}x^2 + {}x + {} = 0 har én reell dobbeltrot .' .format(a, b, c))

main()

