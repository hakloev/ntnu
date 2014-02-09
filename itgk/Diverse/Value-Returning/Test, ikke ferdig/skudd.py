def year_test(year):
	if year % 4 == 0 and year % 100 == 0: 
		if year % 400 == 0:
			return True
	elif year % 4 == 0: 
		return True
	else:
		return False

def leap_year(end): 
	leap_years = []
	for year in range(0, end + 1):
		if year_test(year):
			leap_years.append(year)
	return leap_years
