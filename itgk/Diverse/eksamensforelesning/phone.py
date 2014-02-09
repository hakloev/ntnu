telefonbok = {}
file = open("telefonbok.txt", "r+") # Would normally use "r" for reading, but we need "r+" in order to create the file if it doesn't exist
for line in file:
	line = line.strip()
	if line[0] == "@":
		navn = line[1:]
		telefonbok[navn] = []
	else:
		nummer = line[1:]
		telefonbok[navn].append(nummer)
file.close()
print("Lastet %i navn fra fil." % len(telefonbok))

while True:
	choice = input("Trykk N for aa legge til et nytt nummer; trykk S for aa soeke; trykk L for aa lagre; trykk X for aa avslutte: ").lower()
	if choice == "n":
		navn = input("Skriv inn navnet: ")
		nummer = input("Skriv inn nummer: ")
		#if navn in telefonbok:
		#	telefonbok[navn].append(nummer)
		#else:
		#	telefonbok[navn] = [nummer]
		result = telefonbok.get(navn, [])
		result.append(nummer)
		telefonbok[navn] = result
		
	elif choice == "s":
		navn = input("Skriv inn navnet: ")
		if navn in telefonbok:
			for nummer in telefonbok[navn]:
				print("   ", nummer)
		else:
			print("Navnet finnes ikke")
	
	elif choice == "l":
		file = open("telefonbok.txt", "w")
		for navn in telefonbok:
			file.write("@" + navn + "\n")
			for nummer in telefonbok[navn]:
				file.write("#" + nummer + "\n")
		file.close()
		
	elif choice == "x":
		break
