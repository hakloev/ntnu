# Øving 6 - Oppgave 3
# Håkon Ødegård Løvdal

from math import sqrt

def main():
	vec1 = getVector() # Leser inn vec1
	printVector(vec1) # Printer vec1
	print('Lengde før skalar:', format(vectorLengde(vec1), '.2f')) # Regner vec1's lengde
	vec1Pre = vectorLengde(vec1) # Tilegner lengde av vec1 før skalering til variabel
	vec1 = skalarMultiplikasjon(vec1, getSkalar()) # Skalarmultipliserer vec1 og skaffer skalar
	printVector(vec1) # Printer skalarmultiplisert vektor
	print('Lengde etter skalar:', format(vectorLengde(vec1), '.2f')) # Printer vektor lengde etter skalarmultiplikasjon
	print('Forholdet mellom vec1 før og etter skalering:', vec1Pre / vectorLengde(vec1)) # Printer forhold mellom lengde av vec1 før og etter skalering
	vec2 = getVector() # Leser inn vec2
	print('Indreproduktet av de to vektorene ', vec1, ' og ', vec2, ': ', indreProdukt(vec1, vec2), sep = '') # Printer indreprodukt av vec1 etter skalering og vec2
	
def printVector(vec):
	x = vec[0]
	y = vec[1]
	z = vec[2]
	print('Vektoren er: ({0}, {1}, {2})'.format(x,y,z))

def getSkalar():
	return int(input('Skalar: '))

def getVector():
	vector = input('Skriv inn vektoren x,y,z: ')
	vector = vector.split(',')
	vectorInt = []
	for num in vector:
		vectorInt.append(int(num))
	return vectorInt

def skalarMultiplikasjon(vec, skalar):
	index = 0
	while index < len(vec):
		vec[index] = vec[index] * skalar
		index += 1
	return vec
	
def vectorLengde(vec):
	return sqrt((vec[0] ** 2) + (vec[1] ** 2) + (vec[2] ** 2))

def vectorLengdeForhold(vec, vecSkalert):
	return vec / vecSkalert

def indreProdukt(vec1, vec2):
	index = 0
	indreProd = 0
	while index < len(vec1):
		uv = vec1[index] * vec2[index]
		indreProd += uv
		index += 1
	return indreProd 


main()
