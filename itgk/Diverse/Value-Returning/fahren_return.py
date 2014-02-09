def celFar(c):
	return (c * (9 / 5)) + 32

def main():
	c = float(input('Hvor mange celsius: '))
	print(celFar(c), 'fahrenheit')

main()