def velkommen():
	print('Info til brukeren: ')
	print('Velkommen til hybelregnskap v.0.1 \n*********************************\n')
	print('Her vil du få følgende valg: ')
	print("""'inntekt' / 'utgift'\n'vis' / 'fjern' \n'save' / 'load' \n'avslutt' / 'hjelp' """)

def melding(tekst):
	print('\n>>>', tekst)

def registrer(db, dbid, valg):
	print('\nRegistrer valg: ')
	dato = str(input('Dato: åååå-mm-dd '))
	beløp = float(input('Beløp: 111.11 [kr] '))
	beskr = str(input('Beskriv oppføringen: '))

	if valg == 'utgift':
		beløp = beløp * -1

	db[dbid] = (dato, beløp, beskr)

	melding('Data er registrert')

	return db

def vis(db):
	balanse = 0
	for entry in db:
		entrytupple = db[entry]
		print('\nID', entry, 'Dato:', entrytupple[0], 'Beløp:', entrytupple[1], 'Beskrivelse', entrytupple[2], '\n')
		balanse += entrytupple[1]

	print('Balanse:', balanse)

def fjern(db):
	print('\nID-er vi har i databasen:', db.keys())
	dbid = int(input('Hvilken vil du fjerne? '))
	
	try:
		del db[dbid]
		melding('ID:', dbid, 'er fjernet')
	except KeyError:
		melding('ID finnes ikke i databasen')

	return db

def velgfilnavn():
	navn = str(input('Velg filnavn: '))
	return navn