import bruker
import fil 

db = dict()

bruker.velkommen()
valg = input('Hva ønsker du å gjøre? ')

while valg.lower() != 'end':
	if valg == 'AddPhil': 
		db = bruker.add(db)
	elif valg == 'DeletePhil':
		db = bruker.delete(db)
	elif valg == 'AveragePhil':
		bruker.average(db)
	elif valg == 'AddToPhil':
		db = bruker.addToPhil(db)
	elif valg == 'Save':
		filnavn = bruker.filnavn()
		fil.save(db, filnavn)
	elif valg == 'Load':
		filnavn = bruker.filnavn()
		db = fil.load(filnavn)
	else:
		bruker.melding('Ugyldig valg, prøv på nytt')
	valg = input('\nHva ønsker du å gjøre? ')

