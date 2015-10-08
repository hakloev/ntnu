# Øving 5 - Oppgave 4 - modul
# Håkon Ødegård Løvdal

days = ["man", "tir", "ons", "tor", "fre", "lør", "søn"]

def weekday_newyear(year):
	day = week_day_year_start(year) 
	return days[day]

def week_day_year_start(year):
	SUM_DAYS = 0
	for total_years in range(1900,year):
		if is_leap_year(total_years):
			SUM_DAYS += 2
		else: 
			SUM_DAYS += 1
	return SUM_DAYS % 7

def is_leap_year(year):
	if year % 400 == 0:
		return True
	elif year % 100 == 0:
		return False
	elif year % 4 == 0:
		return True

	return False
