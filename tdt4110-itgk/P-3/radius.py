# Øving 3 - Oppgave 3d
# Håkon Ødegård Løvdal

import math

def main(): 
	areal = float(input('Hva er arealet av sirkelen? '))
	omkrets = float(input('Hva er omkretsen av sirkelen? '))
	if omkrets > 0: 
		convert_o(omkrets)
	else: 
		convert_a(areal) 

def convert_o(o):
	r = o / (2 * math.pi)
	print('Radiusen er:', format(r, '.2f'))

def convert_a(a):
	r = math.sqrt(a / math.pi)
	print('Radiusen er:', format(r, '.2f'))

main()