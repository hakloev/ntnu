from skumleskogen import *

valg = int(input('Hva vil du? '))

while valg != 100:
	
	if valg == 1:
		gaa_venstre()
		n = nummer()
		print('Du er på', n)
	elif valg == 2:
		gaa_hoyre()
		n = nummer()
		print('Du er på', n)
	elif valg == 3:
		gaa_tilbake()
		n = nummer()
		print('Du er på', n)

	valg = int(input('Hva vil du? '))
