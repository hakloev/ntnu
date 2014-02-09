#!/usr/bin/env python
# -*- coding: utf8 -*- 

# 2012
# Håkon Ødegård Løvdal © 

infile = open('nummer.txt', 'r')

liste = []
numbers = dict()

line = infile.readline()
while line != '':
	line = line.rstrip('\n')
	liste.append(int(line))
	line = infile.readline()

for index in range(1, max(liste) + 1):
	numbers[index] = liste.count(index) 
	
print(numbers)

infile.close()