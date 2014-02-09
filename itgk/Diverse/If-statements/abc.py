# ABC-formel 
# Håkon Ødegård Løvdal

from math import sqrt

def main():
	tall()
	
def tall():
	a = float(input('Enter a: '))
	b = float(input('Enter b: '))
	c = float(input('Enter c: '))
	d = b ** 2 - (4 * a * c)
	abc(a,b,c,d)

def abc(a,b,c,d):
	if d < 0:
		print('No solutions')
	elif d == 0:
		result = (-b + sqrt(d)) / (2 * a)
		print(result)
	else: 
		result1 = (-b + sqrt(d)) / (2 * a)
		result2 = (-b - sqrt(d)) / (2 * a)
		print(format(result1, '.2f'))
		print(format(result2, '.2f'))

main()
