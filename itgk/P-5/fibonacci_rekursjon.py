# Øving 5 - Oppgave 5b
# Håkon Ødegård Løvdal

def main():
	n = int(input('Enter n: '))
	print(fib(n))

def fib(n):
	if n > 2:
		return fib(n - 1) + fib(n - 2)
	elif n == 1:
		return 0
	elif n == 2:
		return 1

main()

