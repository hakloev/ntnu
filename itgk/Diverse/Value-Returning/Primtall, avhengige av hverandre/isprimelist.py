import isprime

primtall = []

def primenumberlist(): 
	for prim in range(0, 101):
		tall = prim, isprime.is_prime(prim)
		primtall.append(tall)
		
primenumberlist()

for plass in primtall:
	print(plass, '\n')