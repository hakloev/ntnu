# importerer moduler
import bruker
import fil
import hjelp

db = dict() # tom dictionary 
dbid = 0 # unik id for dictionary key (øker underveis)

bruker.velkommen() # printer intro-tekst

valg = input('\nHva ønsker du å gjøre? ')

while (valg != 'avslutt'): 
	if (valg == 'inntekt') or (valg == 'utgift'):
		dbid += 1
		db = bruker.registrer(db, dbid, valg)
	elif (valg == 'vis'):
		bruker.vis(db)
	elif (valg == 'fjern'):
		db = bruker.fjern(db)
	elif (valg == 'save'):
		filnavn = bruker.velgfilnavn()
		db = fil.save(db, filnavn)
	elif (valg == 'load'):
		filnavn = bruker.velgfilnavn()
		db = fil.load(filnavn)
	elif (valg == 'hjelp'):
		hjelp.instruksjoner()
	else:
		bruker.melding('Ugyldig valg, prøv ommattatt')

	valg = input('\nHva ønsker du å gjøre? ')
		
	


