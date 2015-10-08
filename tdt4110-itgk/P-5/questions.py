# Øving 5 - Oppgave 2 - modul med spørsmål
# Håkon Ødegård Løvdal

# Modul med alle spørsmål som skal kjøres i while-løkka i undersokelse.py

import os

def kjonn(): 
	return input('Kjønn? (svar med k for kvinne og m for mann): ')

def alder():
	return int(input('Alder? '))
	
    
def sosmedie():
	print()
	print('Benytter du deg av ett eller flere sosiale medier?')
	return str(input('Svar ja eller nei: '))

def facebook(kjonn):
	if kjonn == 'm':
		print("Mellom 40-45% av Facebook sine brukere er menn.")
		return str(input('Er du en av disse? '))
	else: 
		print("Mellom 55-60% av Facebook sine brukere er kvinner.")
		return str(input('Er du en av disse? '))

def tidsforbruk():
	return int(input('Hvor mange (hele) timer bruker på sosiale medier daglig? '))
	
def nybruker():
	os.system("clear")
	return str(input('Er det en ny bruker tilstede (skal vi gjenta' + \
		' undersøkelsen)? '))
