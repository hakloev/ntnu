import urllib.request
import hashlib
import time
import os

flag = True
url = "http://www.tollpost.no/wwwappl/send_foresp.epl?ref_type=kolli_id&lang=no&ref=00370702055095631054"

response = urllib.request.urlopen(url).read()
where = response.find('0')

count = 0
while flag:
	md = str(hashlib.md5(response[0:]).hexdigest())
	if md == 'd41d8cd98f00b204e9800998ecf8427e':
		count += 1
		print('This is the', count, 'time and it will now sleep for 5 minutes')
		flag = True
		time.sleep(1)
	else:
		# os.system("say Youve got mail")
		print(md)
		print(response[0:])
		flag = False


    
      