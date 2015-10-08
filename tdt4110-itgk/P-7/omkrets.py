# Øving 7 - Oppgave 4
# Håkon Ødegård Løvdal
import math

x = [1, 2, 4, 5, 3]
y = [2, 4, 5, 4, 1]

def perimeter(x, y): 
	lengde = 0
	for i in range(0, len(x)): # i er index
		if i == (len(x) - 1):
			lengde += pytagoras(x[i], x[0], y[i], y[0])
		else:
			lengde += pytagoras(x[i], x[i + 1], y[i], y[i + 1])
	print(lengde) 
			

def pytagoras(xi, xii, yi, yii):
	return math.sqrt(((xi - xii) ** 2) + ((yi - yii) ** 2))

perimeter(x, y)