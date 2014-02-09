# Øving 5 - Oppgave 5a
# Håkon Ødegård Løvdal

def main():
	n = int(input('Enter n: '))
	print(fib(n))

def fib(n):
	a = 1
	b = 0
	if n > 2:
		for x in range(2, n + 1):
			c = b + a
			a = b
			b = c
		return c
	elif n == 1:
		return 0
	elif n == 2:
		return 1 

main()