from skumleskogen import *

hukommelse = {}
node_typer = [er_vanlig, er_laas, er_superlaas, er_inngang, er_utgang, er_stank, er_nokkel]
n = nummer() # current node
siste_vei = "venstre"

def main():
	global n
	n = nummer()
	print(n) # aktiver for node-nr debug 
	husk(n)
	bevegelse(node_type(), n)

def husk(n):
	global hukommelse
	if n not in hukommelse:
		hukommelse[n] = {"venstre": True, "hoyre": True}

def node_type():
	for x in node_typer:
		if x(): 
			return str(x)[10:(str(x).find("at") - 1)]

def bevegelse(nodeType, n):
	global hukommelse
	global siste_vei
	if nodeType == "er_nokkel":
		print('Fant nøkkel, plukker den opp, og går tilbake')
		plukk_opp()
		gaa_tilbake()
		n = nummer()
		hukommelse[n]["venstre"] = False
		hukommelse[n]["hoyre"] = False
		main()
	elif nodeType == "er_laas" or nodeType == "er_superlaas":
		print('Fant en lås, prøver å låse opp')
		if laas_opp():
			print('Låst opp!')
			hukommelse = {}
			n = nummer()
			husk(n)
			try:
				main()
			except RuntimeError:
				print('RUNTIME ERROR')
			# FYLL INN HER; TERMINERER HER		

		else:
			print('Fikk ikke låst opp lås, går tilbake')
			gaa_tilbake()
			n = nummer()
			hukommelse[n][siste_vei] = False
			main()
	elif nodeType == "er_stank":
		print('Er på en stank-node, går tilbake til parent-node')
		gaa_tilbake()
		n = nummer()
		husk(n)
		hukommelse[n][siste_vei] = False
	elif nodeType == "er_utgang":
		print('Går ut!')
		gaa_ut()
	else: # er_vanlig og er_inngang
		if hukommelse[n]["venstre"] == True:
			venstre()
		elif hukommelse[n]["hoyre"] == True:
			hoyre()	
		else:
			print('Ingen vei, går enda en tilbake')
			gaa_tilbake()
			hukommelse = {}
			main()			

def venstre():
	global n
	global hukommelse
	global siste_vei
	print('Går mot venstre..')
	n_gammel = nummer()
	if gaa_venstre():
		hukommelse[n_gammel][siste_vei] = True
		siste_vei = "venstre"
		main()
	else:
		gaa_tilbake()
		n = nummer()
		hukommelse[n]["venstre"] = False
		print('Gikk en tilbake pga blindvei')
		main()

def hoyre():
	global n
	global hukommelse
	global siste_vei
	print('Går mot høyre..')
	n_gammel = nummer()
	if gaa_hoyre():
		hukommelse[n_gammel][siste_vei] == True
		siste_vei = "hoyre"
		main()
	else:
		gaa_tilbake()
		n = nummer()
		hukommelse[n]["hoyre"] = False
		print('Gikk en tilbake pga blindvei')
		main()
		
main()

print(hukommelse)