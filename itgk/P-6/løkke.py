# Øving 6 - Oppgave 1
# Håkon Ødegård Løvdal

n = int(input('Skriv inn et heltall: '))
x = 1
total = 0

while (total + (x ** 2)) <= n:
	z = x ** 2
	total += z
	x += 1

print('Antall elementer i rekke:', x - 1)
print('Svar:', total)
	
