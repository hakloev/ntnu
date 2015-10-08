# Øving 5 - Oppgave 4 - modul
# Håkon Ødegård Løvdal

import day_start

days = ["man", "tir", "ons", "tor", "fre", "lør", "søn"]

def is_workday(weekday):
	if weekday < 5:
		return True
	else:
		return False

def workdays_in_year(year):
	days = 0
	if day_start.is_leap_year(year):
		for x in range(day_start.week_day_year_start(year), (366 + day_start.week_day_year_start(year))):
			day = x % 7
			if is_workday(day):
				days += 1
	else:
		for x in range(day_start.week_day_year_start(year), (365 + day_start.week_day_year_start(year))):
			day = x % 7
			if is_workday(day):
				days += 1
	print(year, 'har', days, 'arbeidsdager')