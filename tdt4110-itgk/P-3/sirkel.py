# Øving 3 - Oppgave 3
# Håkon Ødegård Løvdal

from math import pi 

def main(): 
	radius = float(input('Hva er radiusen av sirkelen? '))
	sirkel(radius)

def sirkel(r):
	a = pi * (r ** 2)	
	o = 2 * pi * r
	print('Areal:', format(a, '.2f'))
	print('Omrekts:', format(o, '.2f'))

main()
