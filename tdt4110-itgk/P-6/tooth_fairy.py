# Øving 6 - Oppgave 4
# Håkon Ødegård Løvdal

teeth = [
		95, 103, 71, 99, 114, 64, 95, 53, 97, 114,
		109, 11, 2, 21, 45, 2, 26, 81, 54, 14,
		118, 108, 117, 27, 115, 43, 70, 58, 107]

def totalCoinsPerChild():
	global teeth
	child = 0
	for weight in teeth:
		value = weight * 0.50
		childList = calcCoins(value)
		print('Child', child + 1, 'needs:')
		print('20-coin: {0}\n10-coin: {1}\n5-coin: {2}'.format(childList[0], childList[1], childList[2]))
		print('1-coin: {0}\n0.5-coin: {1}\n'.format(childList[3], childList[4]))
		child += 1

def totalCoins():
	global teeth
	listChilds = []
	for weight in teeth:
		value = weight * 0.50
		listChilds += calcCoins(value)
	
	total20 = 0
	for x in listChilds[0:len(listChilds):5]:
		total20 += x
	
	total10 = 0
	for x in listChilds[1:len(listChilds):5]:
		total10 += x

	total5 = 0
	for x in listChilds[2:len(listChilds):5]:
		total5 += x

	total1 = 0
	for x in listChilds[3:len(listChilds):5]:
		total1 += x

	total05 = 0
	for x in listChilds[4:len(listChilds):5]:
		total05 += x

	print('TOTAL NEED FOR COINS:\n*********************\n')
	print('20-coin: ', total20, '\n', '10-coin: ', total10, '\n', '5-coin: ', total5, sep = '')
	print('1-coin: ', total1, '\n', '0.5-coin: ', total05, '\n', sep = '')
	
def calcCoins(value):
	coins = []
	coin_unit = [20, 10, 5, 1, 0.5]
	for coin in coin_unit:
		coins.append(int(value // coin))
		value %= coin 
	return coins
	
totalCoins()
