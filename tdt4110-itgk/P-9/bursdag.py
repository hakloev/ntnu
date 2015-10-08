#!/usr/bin/env python
# -*- coding: utf8 -*- 

# 2012
# Håkon Ødegård Løvdal © 

birthdays = {
"22 nov": ["Lars", "Mathias"], 
"10 des": "Elle",
"30 okt": ["Veronica", "Rune"],
"12 jan": "Silje",
"31 okt": "Willy",
"8 jul": ["Brage", "Øystein"], 
"1 mar": "Nina"
}

def add_birthday_to_date(date, name):
	try:
		birthdays[date].append(name)
	except AttributeError:
		before = birthdays.pop(date)
		names = [before, name]
		birthdays[date] = names
	except KeyError:
		birthdays[date] = name
		
add_birthday_to_date('9 feb', 'Lillian')

print(birthdays)

