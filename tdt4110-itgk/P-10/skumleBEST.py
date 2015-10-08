# encoding: utf-8
from skumleskogen2 import *

husk = {}
Q = [nummer()]

while Q:
	curr = Q.pop()
	print 'Ny iterasjon, er på node:', curr
	if curr not in husk:
			husk[curr] = {'venstre': False, 'hoyre': False}
	if er_nokkel():
		husk = {}
		plukk_opp()
		gaa_tilbake()
		print 'Fant nøkkel, går tilbake!'
	elif er_laas() or er_superlaas():
		if laas_opp():
			print 'Laaste opp!'
		else:
			gaa_tilbake()
	elif er_stank():
		gaa_tilbake()
		print 'Stank her, må gå tilbake...'
	elif er_utgang():
		gaa_ut()
		print 'DU ER VANVITTIG FLINK LØVDAL!'
		break
	else:
		if not husk[curr]['venstre']:
			if gaa_venstre():
				husk[curr]['venstre'] = True
				print 'Går venstre!'
			else: 
				gaa_tilbake()
				print 'Går tilbake...'
		elif not husk[curr]['hoyre']:
			if gaa_hoyre():
				husk[curr]['hoyre'] = True
				print 'Går høyre!'
			else:
			 	gaa_tilbake()
			 	print 'Går tilbake...'
		else:
			gaa_tilbake()	
			print 'Må gå enda lenger tilbake...'			
	Q.append(nummer())