#!/usr/bin/env python
# -*- coding: utf8 -*- 

# 2012
# Håkon Ødegård Løvdal © 

points = dict()
infile = open('poenggrenser_2011.csv', 'r')
line = infile.readline()
while line != '':
	line = line.strip('\n').split(',')
	points[line[0].strip('"')] = line[1].strip('"')
	line = infile.readline()	
infile.close()

def all_students(points):
	total = 0
	for x in points:
		if points[x] == 'Alle':
			total += 1
	return total 

def ntnu_snitt(points):
	total = 0
	studier = 0	
	for x in points:
		if x.startswith('NTNU'):
			if points[x] != 'Alle':
				total += float(points[x])
				studier += 1
	return total / studier

def lower_higher(points):
	liste = []
	maxmin = []
	for x in points:
		if x.startswith('NTNU'):
			if points[x] != 'Alle':
				liste.append(points[x])
	maxmin.append(min(liste))
	maxmin.append(max(liste))
	return tuple(maxmin)
	
				
	
#print(all_students(points))
#print(format(ntnu_snitt(points), '.2f'))
print(lower_higher(points))





	

