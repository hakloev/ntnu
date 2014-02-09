# Areas of Rectangles 
# Håkon Ødegård Løvdal

def main(): 
	print()
	print('In this program you type in the length and width \n'
		'of two rectangles, and it tells you which is greater \n'
		'or if they are equal!')
	rectangles()

def rectangles():
	print()
	length1 = float(input('Length of the first rectangle: '))
	width1 = float(input('Width of the first rectangle: '))
	print()
	length2 = float(input('Length of the second rectangle: '))
	width2 = float(input('Width of the second rectangle: '))
	calculate(length1, length2, width1, width2)

def calculate(l1, l2, w1, w2):
	rectangle1 = l1 * w1
	rectangle2 = l2 * w2
	area(rectangle1, rectangle2)

def area(first, second):
	print()
	if first > second:
		print('The first rectangle is the greatest!')
		print(first)
	elif first < second:
		print('The second rectangle is the greatest!')
		print(second)
	elif first == second:
		print('They are equal!')
		print(first, '=', second)

main()
