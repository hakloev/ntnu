# Stadium Seating
# Håkon Ødegård Løvdal
	
def main():
	income()

def income():
	total_soldA = int(input('How many Class A seats where sold? '))
	priceA = 15 
	total_incomeA = priceA * total_soldA
	
	total_soldB = int(input('How many Class B seats where sold? '))
	priceB = 12
	total_incomeB = priceB * total_soldB
	
	total_soldC = int(input('How many Class C seats where sold? '))
	priceC = 9
	total_incomeC = priceC * total_soldC
	
	total(total_incomeA, total_incomeB, total_incomeC)
	
def total(a, b, c):
	total = a + b + c
	print(total)

main()
	
