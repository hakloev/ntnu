import bruker 

def instruksjoner():
	print('********************************')
	print("""\nDu kan få hjelp om følgende funksjoner: ('avslutt' for å gå tilbake) """)
	print("""'inntekt' / 'utgift'\n'vis' / 'fjern' \n'save' / 'load' """)
	valg = str(input('\nHvilken funksjon ønsker du hjelp om? '))

	while valg != 'avslutt':
		if (valg == 'inntekt' or valg == 'utgift'):
			print()
		elif (valg == 'vis'): 
			print()
		elif (valg == 'fjern'):
			print()
		elif (valg == 'save' or valg == 'load'):
			print()
		else:
			bruker.melding('Ugyldig, ikke-eksisterende hjelpeemne')
		valg = str(input('\nHvilken funksjon ønsker du hjelp om? '))
	


	