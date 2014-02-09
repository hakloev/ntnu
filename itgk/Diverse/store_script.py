#!/usr/bin/env python
# -*- coding: utf8 -*- 

# Håkon Ødegård Løvdal

import urllib
import hashlib
import time
import os

flag = True
url = "http://www.dhl.no/content/no/no/express/sporing.shtml?brand=DHL&AWB=4926701905%0D%0A"

def getPage(url):
	response = urllib.request.urlopen(url)
	return response.read()

def splitPage(site):
	head = site.find('4926701905')
	return hashlib.md5(site[26635:27980]).hexdigest()

count = 0
while flag:
	md = splitPage(getPage(url))
	if md == '4df48c2fa402bc8305ba0377687b7c6b':
		count += 1
		print('This is the', count, 'time and it will now sleep for 30 second')
		flag = True
		time.sleep(30)
	else:
		print(md)
		os.system("say It's here")
		flag = False