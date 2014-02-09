# Total Sales

WEEKDAYS = 6
salesList = []
day = 1
saleTotal = 0

for x in range(1, WEEKDAYS + 1):
	print('Salg for dag ', day, ': ', sep = '', end = '')
	sale = int(input())
	salesList.append(sale)
	day += 1

for sale_value in salesList:
	saleTotal += sale_value

print(saleTotal)

