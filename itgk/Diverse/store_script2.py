#!/usr/bin/env python
# -*- coding: utf8 -*- 

# Håkon Ødegård Løvdal

import urllib
import hashlib
import time
import os

flag = True
url = "http://store.apple.com/no/"

def getPage(url):
	req = urllib
	response = urllib
	return response

def splitPage(site): 
	return hashlib.md5(site[26635:27980]).hexdigest()

count = 0
while flag:
	md = splitPage(getPage(url))
	if md == 'f24b3b7399afab5f062d00dc88984819':
		count += 1
		print('This is the', count, 'time and it will now sleep for 30 second')
		flag = True
		time.sleep(30)
	else:
		print(md)
		os.system("say It's here")
		flag = False