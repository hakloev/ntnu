import pickle
from bruker import melding

def save(db, filnavn):
	fil = open(filnavn, 'bw')
	pickle.dump(db, fil)
	fil.close()

def load(filnavn):
	try:
		f = open(filnavn, 'br')
		db = pickle.load(f)
		f.close()
		return db
	except FileNotFoundError:
		melding('Filnavn ikke funnet, prøv på nytt')
