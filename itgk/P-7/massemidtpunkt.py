# Øving 7 - Oppgave 2
# Håkon Ødegård Løvdal

import random

def main():
	print(masseMidtPunkt(genListe()))

def masseMidtPunkt(stang):
	hm = sum(stang) / 2 # halvemassen av stanga
	masse_midt = 0 # teller, holder styr på vekt i massemidtpunktet 
	mp = 0 # teller, holder styr på hvor massemidtpunktet er
	for punkt in stang: # punkt peker på antall kg på meteren 
		if masse_midt + punkt < hm: 
			masse_midt += punkt
			mp += 1
		else:
			dp = hm - masse_midt # delpunkt, andel av punkt som gir mp i kg
			masse_midt += dp # teller, for å sjekke om mp er nådd
			mp += dp / punkt # legger til andel av punkt i meter til mp
			if masse_midt == hm: 
				return mp # returnerer midtpunktet 

def genListe():
	n = int(input('Hvor lang liste? '))
	stang = [0] * n
	index = 0
	while index < len(stang):
		stang[index] = random.randint(1, 10)
		index += 1
	return stang

main()