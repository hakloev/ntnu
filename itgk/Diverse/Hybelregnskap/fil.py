import pickle
import bruker

def save(db, filnavn):
	f = open(filnavn, 'bw')
	pickle.dump(db, f)
	f.close()

def load(filnavn):
	try:
		f = open(filnavn, 'br')
		db = pickle.load(f)
		f.close()
		return db
	except FileNotFoundError:
		bruker.melding('Filnavnet eksisterer ikke')

	