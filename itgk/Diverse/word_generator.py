from random import randint

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','æ','ø','å']
numbers = [0,1,2,3,4,5,6,7,8,9]

def generator(length, let, num):
	word = ''
	possibility = {0: 'let', 1: 'num'}
	for x in range(length):
		index = randint(0, 1)
		if possibility[index] == 'let':
			word += let[randint(0, len(let) - 1)]
		elif possibility[index] == 'num':
			word += str(num[randint(0, len(num) - 1)])
		else:
			print('Something wrong with index')
	return word		

def make_file():
	global letters
	global numbers
	f = open('words.txt', 'w')
	for x in range(1000):
		word = generator(randint(1, 11), letters, numbers)
		f.write(str(word) + '\n')
	f.close()

make_file()
