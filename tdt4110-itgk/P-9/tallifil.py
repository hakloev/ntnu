#!/usr/bin/env python
# -*- coding: utf8 -*- 

# 2012
# Håkon Ødegård Løvdal © 

def main():
	infile = open('nummer.txt', 'r')
	print(number_of_lines(infile))
	infile.close()	
	
	infile = open('nummer.txt', 'r')
	numbers = number_frequency(infile)
	infile.close()
	for x in numbers:
		print(x, ': ', numbers[x], sep = '')
	

def number_of_lines(filename):
	all_numbers = filename.readlines()
	return len(all_numbers)
	
def number_frequency(filename):
	all_numbers = []
	numbers = dict()

	line = filename.readline()
	while line != '':
		line = line.rstrip('\n')
		all_numbers.append(int(line))
		line = filename.readline()
		
	for index in range(0, max(all_numbers) + 1):
		numbers[index] = all_numbers.count(index) 
		
	return numbers

main()