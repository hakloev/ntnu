from skumleskogen2 import *

fortsett = True
hukommelse = {}

while fortsett:
	n = nummer()
	# print(n) # node-debug 
	if n not in hukommelse:
		hukommelse[n] = {"venstre": False, "hoyre": False}

	if hukommelse[n]["venstre"] == False:
		hukommelse[n]["venstre"] = True
		if gaa_venstre():
			print('Går venstre')
			if er_laas() == True or er_superlaas() == True:
				if laas_opp():
					hukommelse = {}
					print('Låser opp')
				else:
					gaa_tilbake()
					print('Har ikke nøkkel, går tilbake')
			elif er_nokkel():
				plukk_opp()
				print('Fant nøkkel, tar opp, og går en tilbake')
				n = nummer()
				hukommelse[n] = {"venstre": False, "hoyre": False}
				gaa_tilbake()
			elif er_stank():
				gaa_tilbake()
				print('Går tilbake, kanin i nærheten')
			elif er_utgang():
				gaa_ut()
				fortsett = False
			else:
				print('Vanlig node')
		else:
			gaa_tilbake()
			n = nummer()
			hukommelse[n]["venstre"] = True
			print('Går tilbake, pga blindvei')
			if hukommelse[n]["venstre"] == True and hukommelse[n]["hoyre"] == True:
				gaa_tilbake()
				print('Går enda en tilbake')
	elif hukommelse[n]["hoyre"] == False:
		hukommelse[n]["hoyre"] = True
		if gaa_hoyre():
			print('Går høyre')
			if er_laas() == True or er_superlaas() == True:
				if laas_opp():
					hukommelse = {}
					print('Låser opp')
				else:
					gaa_tilbake()
					print('Har ikke nøkkel, går tilbake')
			elif er_nokkel():
				plukk_opp()
				print('Fant nøkkel, tar opp, og går en tilbake')
				n = nummer()
				hukommelse[n] = {"venstre": False, "hoyre": False}
				gaa_tilbake()
			elif er_stank():
				gaa_tilbake()
				print('Går tilbake, kanin i nærheten')
			elif er_utgang():
				gaa_ut()
				fortsett = False
			else:
				print('Vanlig node')
		else:
			gaa_tilbake()
			n = nummer()
			hukommelse[n]["hoyre"] = True
			print('Går tilbake pga blindvei')
			if hukommelse[n]["venstre"] == True and hukommelse[n]["hoyre"] == True:
				gaa_tilbake()
				print('Går enda en tilbake')		
	elif hukommelse[n]["venstre"] == True and hukommelse[n]["hoyre"] == True:
		gaa_tilbake()
		print('Går enda enda en tilbake')

print('\n********************************************************')	
print('INNI HELVETE Å FLINK JEG ER, KLARTE DEN JÆVLA LABERYNTEN')
	


