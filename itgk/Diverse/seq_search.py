#!/usr/bin/env python
# -*- coding: utf8 -*- 

# 2012
# Håkon Ødegård Løvdal © 

liste = [2, 7, 1, 4, 3, 5, 10, 6, 9, 8]

def seq_search(liste, item):
	for element in liste:
		if element == item:
			return True
	return False 

def insertion_search(liste):
	for i in range(1, len(liste)):
		element = liste[i]
		hull = i 
		while hull > 0 and liste[hull - 1] > element:
			liste[hull] = liste[hull - 1]
			hull = hull - 1
		liste[hull] = element 
	return liste
	
	





	
	