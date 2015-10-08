# Øving 5 - Oppgave 4
# Håkon Ødegård Løvdal

import day_start
import is_workday

def main():
	#year = int(input('Skriv inn år: ')) #Aktiv hvis man ønsker spesifikt år istedenfor (husk å lage korrekt funksjonskall)
	#workday = int(input('Skriv inn en ukedag representert ved heltall (0-6): ')) # Aktiv hvis oppgave b
	
	for x in range(1901, 2001): #Aktiv hvis oppgave a eller c
		print(x, day_start.weekday_newyear(x)) # Aktiv hvis oppgave a
		#is_workday.workdays_in_year(x) # Aktiv hvis oppgave c

	#print(is_workday.is_workday(workday)) # Aktiv hvis oppgave b
		
main()
