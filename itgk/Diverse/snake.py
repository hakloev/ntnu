#!/usr/bin/env python
# -*- coding: utf8 -*- 

# 2012
# Håkon Ødegård Løvdal © 
import random 

#n = int(input('Enter n: '))

def lag_tomt_brett(n):
	brett = []
	for i in range(n):
		rad = []
		for j in range(n):
			rad.append(1)
		brett.append(rad)
	return brett 
	
def legg_ut_epler(brett, antall):
	N = len(brett)
	while(antall > 0):
		x = random.randint(0, N - 1)
		y = random.randint(0, N - 1)
		if brett[x][y] != 5:
			brett[x][y] = 5
			antall = antall - 1
	
	return brett 

def sjekk_eple(brett, x, y):
	if brett[x][y] == 5:
		return True
	return False

def tegn_orm(brett, orm_x, orm_y):
	N = len(orm_x)
	for i in range(N):
		x = orm_x[i]
		y = orm_y[i]
		brett[x][y] = 0
	hale_x = orm_x[N - 1]
	hale_y = orm_y[N - 1]
	brett[hale_x][hale_y] = 1
	return brett

def sjekk_krasj(orm_x, orm_y, retning):
	N = len(orm_x)
	sjekk_x = orm_x[0]
	sjekk_y = orm_y[0]
	if retning == 'n':
		sjekk_y = sjekk_y - 1
	elif retning == 's':
		sjekk_y = sjekk_y  + 1
	elif retning == 'w':
		sjekk_x  = sjekk_x - 1
	elif retning == 'e':
		sjekk_x = sjekk_x + 1
	else:
		print('Feil input')
	for i in range(N):
		if sjekk_x == orm_x[i] and sjekk_y == orm_y[i]:
			krasj = True
	return krasj
	
def flytt_orm(orm_x, orm_y, retning):
	N = len(orm_x)
	for i in range(N -1, 0, -1):
		orm_x[i] = orm_x[i - 1]
		orm_y[i] = orm_y[i -1]
	if retning == 'n':
		orm_y[0] = orm_y[0] - 1
	elif retning == 's':
		orm_y[0] = orm_y[0] + 1
	elif retning == 'w':
		orm_x[0] = orm_x[0] - 1
	elif retning == 'e':
		orm_x[0] = orm_x[0] + 1
	else:
		print('Feil input')
	return orm_x, orm_y
	
brett = lag_tomt_brett(5)
orm_x = [3, 2, 1]
orm_y = [4, 4, 4]
brett = legg_ut_epler(brett, 4)
brett = tegn_orm(brett, orm_x, orm_y)

for liste in brett:
	print(liste)
#print(brett)
#print(legg_ut_epler(lag_tomt_brett(n), 3))
#print(lag_tomt_brett(n))