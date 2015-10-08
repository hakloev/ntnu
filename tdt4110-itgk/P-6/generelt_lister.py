# Øving 6 - Oppgave 2
# Håkon Ødegård Løvdal

def main():
	li = [2, 3, 4, 5, 6]

	index = 0
	while index < len(li):
		if li[index] % 2 == 0:
			li[index] = (int(li[index] * -1))
			index += 1
		else:
			index += 1

	li.sort()
	li.reverse()
	print(li)
	
main()

