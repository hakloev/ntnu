# Øving 5 - Oppgave 4
# Håkon Ødegård Løvdal

# 52*7 = 364
# 52 uker + en dag = 365

# Skuddår er år som er delige med 4, med unntak av århundrer, som må
# være delige med 400

import skudd

WEEK_DAY = 0

def day_start():
	global WEEK_DAY
	year = int(input('Skriv inn ett årstall: '))
	print(WEEK_DAY)
	print(is_leapyear(year))
	for year_user in range(1900, year + 1):
		if is_leapyear(year):
			WEEK_DAY += 2
		else:
			WEEK_DAY += 1
	print(WEEK_DAY)


def is_leapyear(year):
	leap_yearlist = skudd.leap_year(year)
	if year in leap_yearlist:
		return True
	else:
		return False

day_start()
