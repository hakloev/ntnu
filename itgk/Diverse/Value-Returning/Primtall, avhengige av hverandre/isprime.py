def is_prime(tall):
	
	if tall <= 1:
		isprime = False
	elif tall > 1 and tall <= 3:
		isprime = True
	else:
		for kontrolltall in range(2, int(tall/2)+1):
			if (tall % kontrolltall) == 0:
				isprime = False
				break
			else: 
				isprime = True

	return isprime	
