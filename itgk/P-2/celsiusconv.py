# Øving 2 - Oppgave 4
# Håkon Ødegård Løvdal
count = []

while True:
	def main():
		# Leser inn temperatur i fahrenheit
		fahren = float(input('Hvor mange grader fahrenheit er det? '))
		conversion(fahren)

	def conversion(temp):
		celsius = float((temp - 32) / (9/5))
		til_liste = float(temp), float(format(celsius, '.2f'))
		print(format(temp, '.2f'), 'fahrenheit tilsvarer', format(celsius, '.2f'), "celsius!")
		count.append(til_liste)

	main()

	endProg = str(input('Slutte? '))
	if endProg == "y":
		break

print()
print(count)
