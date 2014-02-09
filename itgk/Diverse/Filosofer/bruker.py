def melding(tekst):
	print('\n>>>', tekst)

def velkommen():
	print('Velkommen til "Gjennomsnittelig filosof v.0.1\n***************************************\n')
	print('Her har du følgende valg:\n-------------------------\n1. AddPhil 2. DeletePhil\n3. AveragePhil' + \
	 ' 4. AddToPhil\n5. Save 6. Load\n\n(For å avslutte skriv "end")\n')

def add(db):
	print('\nRegistrer filosof: ')
	filosof = input('Hva heter filosofen: ')
	db[filosof] = 0
	melding('Filosof registrert')
	return db

def delete(db):
	print('\nFilosofer tilgjengelig er:', db.keys())
	dbid = input('\nHvem ønsker du å fjerne? ')
	try:
		del db[dbid]
		melding('Filosof fjernet')
	except KeyError:
		melding('Filosof finnes ikke, prøv på nytt')
	return db

def filnavn():
	fil = input('\nFilnavn: ')
	return fil

def addToPhil(db):
	filosof = input('Hvilken filosof: ')
	ganger = int(input('Antall ganger på eksamen: '))
	try:
		db[filosof] += ganger
		return db
	except KeyError:
		melding('Filosofen eksisterer ikke, prøv på nytt')

def average(db):
	for key in db:
		if db[key] == 1:
			print(key, 'har vært:', db[key], 'gang til eksamen')
		else:
			print(key, 'har vært:', db[key], 'ganger til eksamen')





