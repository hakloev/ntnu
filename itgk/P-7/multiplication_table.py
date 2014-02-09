#!/usr/bin/env python
 # Øving 7 - Oppgave 5c
# Håkon Ødegård Løvdal

def main():
	n = int(input('Enter n: '))

	for rad in multiplication_table(n):
		print(rad)


def multiplication_table(n):
	table = []
	faktor = 0
	for rad in range(n):
		faktor += 1
		liste = []
		for kolonne in range(n):
			tall = (kolonne + 1) * faktor
			liste.append(tall)	
		table.append(liste)
	return table

main()