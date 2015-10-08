# Øving 5 - Oppgave 5c
# Håkon Ødegård Løvdal

fib_liste = []

def main():
	global fib_liste
	n = int(input('Enter n: '))
	for x in range(1, n + 1):
		fib_liste.append(fib(x))
	print(fib_liste)

def fib(n):
	if n > 2:
		return fib(n - 1) + fib(n - 2)
	elif n == 1:
		return 0
	elif n == 2:
		return 1

main()