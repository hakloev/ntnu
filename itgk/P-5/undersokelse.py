# Øving 5 - Oppgave 2
# Håkon Ødegård Løvdal

# Importerer modulen questions.py
import questions
# Importerer os, for å kunne klarere terminal ved start av undersøkelsen
import os

#Globale tellere 
ANTALL_KVINNER = 0
ANTALL_MENN = 0
ANTALL_SOSMEDIER = 0 
ANTALL_FACEBOOK = 0 
ANTALL_TIMER_SOSMEDIER = 0

def main():
	os.system("clear")
	print('INFO TIL BRUKEREN:')
	print()
	print('\nDu svarer på spørsmålene med henholdsvis ja/nei\n' + \
			'eller heltall der hvor det kreves!')
	print('Du kan når som helst avslutte ved å skrive "hade"' + \
		'\nsom svar på et spørsmål!')
	print()
	print('Tiltenkt aldersgruppe er: 16 til 25 år')
	print()
	klar = str(input('Klar til å starte? '))
	if klar == 'ja':
		undersokelse()
		resultat()
	else:
		print('Den er grei, da avslutter vi ;)')

def undersokelse(): 
	# Gjør det mulig å hente/endre de globale i scopet til funksjonen 
	global ANTALL_KVINNER
	global ANTALL_MENN
	global ANTALL_SOSMEDIER 
	global ANTALL_FACEBOOK 
	global ANTALL_TIMER_SOSMEDIER
	# Variabel for å kontrollere while-løkke
	stopp_undersøkelse = True
	os.system("clear")
	while stopp_undersøkelse:
		# Skaffer kjønn og alder fra brukeren
		kjonn = questions.kjonn()
		if kjonn == 'hade':
			break
		try:	
			alder = questions.alder()
		except ValueError:
		 	break
		# Sjekker om brukeren kvalifiserer for tiltenkt aldersgruppe
		# og hvis ikke kreves kjønn og alder på nytt (overskriver forrige variabel verdi)
		if alder < 16 or alder > 25:
			os.system("clear")
			print('Du er dessverre utenfor tiltenkt aldersgruppe')
			continue
		# Legger til i telle-variabel her, slik at de utenfor aldersgruppe
		# ikke blir registrert i undersøkelsen
		if kjonn == 'k':
			ANTALL_KVINNER += 1
		else:
			ANTALL_MENN += 1
		# Spør om brukeren er aktiv på sosiale medier
		aktiv_sosmedier = questions.sosmedie()
		if aktiv_sosmedier == 'hade':
			break
		if aktiv_sosmedier == 'ja':
			ANTALL_SOSMEDIER += 1
		# Hvis brukeren er aktiv sjekker vi om bruk av Facebook og tidsforbruk
		if aktiv_sosmedier == 'ja':
			medlem_facebook = questions.facebook(kjonn)
			if medlem_facebook == 'hade':
				break
			if medlem_facebook == 'ja':
				ANTALL_FACEBOOK += 1
			try:
				timer_sosmedier = questions.tidsforbruk()
				ANTALL_TIMER_SOSMEDIER += timer_sosmedier
			except ValueError:
				break
		
				ANTALL_TIMER_SOSMEDIER += timer_sosmedier
		# Undersøker om det er ny bruker tilstede
		ny_bruker = questions.nybruker()
		# Tilordner false til stopp_undersøkelse hvis nei og motsatt 
		if ny_bruker == 'ja':
			os.system("clear")
			stopp_undersøkelse = True
		else:
			stopp_undersøkelse = False

def resultat():
	os.system("clear")
	print('Resultater fra undersøkelsen:\n-----------------------------')
	print(ANTALL_KVINNER, 'kvinner deltok i undersøkelsen')
	print(ANTALL_MENN, 'menn deltok i undersøkelsen')
	print(ANTALL_SOSMEDIER, 'av deltagerene er på sosiale medier')
	print(ANTALL_FACEBOOK, 'av deltagerene bruker Facebook')
	print('Deltagerene bruker tilsammen', ANTALL_TIMER_SOSMEDIER, 'timer' + \
	' på sosiale medier')

main()