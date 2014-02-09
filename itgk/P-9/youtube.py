#!/usr/bin/env python
# -*- coding: utf8 -*- 

# 2012
# Håkon Ødegård Løvdal © 

links = ['http://www.youtube.com/watch?v=oKI-tD0L18A',
 	'http://www.youtube.com/watch?v=82LCKBdjywQ',
	'http://www.youtube.com/watch?v=GpNSip5gyKo', 
	'http://www.youtube.com/watch?v=rHG-JO8gIGk', 
	'http://www.youtube.com/watch?v=ZFngtBIxRPk', 
	'http://www.youtube.com/watch?v=OZBWfyYtYQY']

def main():
	for element in convertLink(links):
		print(element)
		
def convertLink(link):
	#"youtu.be/<id>"
	#"http://www.youtube.com/watch?v=<id>" 
	convertedLink = []
	for element in link:
		idNum = element[31:]
		convertedLink.append('youtu.be/' + idNum)
	return convertedLink
	
main()