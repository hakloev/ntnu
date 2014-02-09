g = 9.8

def main(): 
	for distance in range(1,11):
		print(format(falling_distance(distance), '.2f'), 'meters') 

def falling_distance(time):
	global g
	return (1 / 2) * g * (time ** 2)

main()