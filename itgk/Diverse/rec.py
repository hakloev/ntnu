#!/usr/bin/env python
# -*- coding: utf8 -*- 

# 2012
# Håkon Ødegård Løvdal © 
z = 1

def run(n):
	global z
	text(z)
	if n > 0:
		run(n - 1)

def text(t):
	global z 
	word = ''
	text = ['This ', 'Is ', 'A ', 'Recursive ', 'Message']
	for x in range(0, t):
		word += text[x]
	print(word)
	z += 1
	
run(4)