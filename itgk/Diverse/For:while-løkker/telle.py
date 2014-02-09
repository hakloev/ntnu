endProg = True
x = 0

while endProg:
	print(x)
	stop = input('Fortsette? ')
	
	if stop == "n":
		endProg = False
	else:
		x += 1
