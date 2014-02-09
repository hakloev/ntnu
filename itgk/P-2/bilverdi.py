# Øving 2 - Oppgave 3
# Håkon Ødegård Løvdal
while True:
	def main():
		navn = str(input('Navnet på bilen? ')) #Navn på bilen
		brutto = int(input('Hva er bruttopris på bilen (kr)? ')) #Bruttopris på bilen
		vekt = int(input('Hvor mye veier bilen (kg)? ')) #Vekt på bilen
		hester = int(input('Antall hestekrefter på bilen? ')) #Hestekrefter på bilen
		co2 = int(input('Antall gram Co2-utslipp på bilen (gram)? ')) #Co2-utslipp
		motor = int(input('Motorvolum på bilen (antall liter)? ')) #Motorvolum
		# Kaller funksjonen beregn_avgift og sender argumentene til funksjonen 
		beregn_avgift(brutto, vekt, hester, co2, motor, navn)

	
	# beregn_avgift mottar argumentene og lager parameter variabler 
	def beregn_avgift(brutto, vekt, hester, co2, motor, navn):
		vekt_p = brutto * vekt * 0.00034 #Vektpris
		hk_p = brutto * hester * 0.00015 #Hestekrefte-pris
		co2_p = brutto * co2 * 0.004 #Co2-pris
		volum_p = brutto * motor * 0.00055 #Volumpris
		nettopris = vekt_p + hk_p + co2_p + volum_p #Beregner nettoprisen 
		utsalg = nettopris + brutto # Beregner utsalgspris
		# Printer navn på bilen og dens nettopris/utsalgspris)
		print('Utsalgspris på en', navn, 'blir:', utsalg, 'kr')
	
	# Kaller main funksjonen
	main()

	endProg = str(input('Vil du beregne en ny bil, eller avslutte? (y or n) '))
	if endProg == "n":
		break
