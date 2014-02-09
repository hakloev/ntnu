# 2012
# Håkon Ødegård Løvdal © 

import pickle

FIND = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

def main(): 
	infile = open('test.dat', 'rb')
	database = pickle.load(infile)
	infile.close()
	
	choice = 0
	while choice != QUIT:
		choice = menu()
		if choice == 1:
			find(database)
		elif choice == 2:
			database = add(database)
		elif choice == 3:
			database = change(database)
		elif choice == 4: 
			database = delete(database)
		
	outfile = open('test.dat', 'wb')
	pickle.dump(database, outfile)
	outfile.close()
	
def menu():
	print()
	print('MENU:')
	print('----------------------')
	print('1. Find person')
	print('2. Add person and email')
	print('3. Change email')
	print('4. Delete person and email')
	print('5. Quit')
	print()
	choice = int(input('What would you like to do: '))
	
	while choice < FIND or choice > QUIT:
		choice = int(input('Enter a valid choice: '))
	
	return choice 

def find(db):
	person = str(input('Who do you want to find: '))
	print(db.get(person, 'The person is not in the file'))
	
def add(db):
	person = str(input('Enter the new persons name: '))
	email = str(input('And the email-address: '))
	db[person] = email 
	return db

def change(db):
	person = str(input('Whos do you want to change: '))
	if person in db:
		db[person] = str(input('Enter the new email: '))
	else:
		print('That name was not found')
	
	return db 

def delete(db):
	person = str(input('Who do you want to delete: '))
	db.pop(person, 'The person is not in the list')
	
	return db
	
main()

