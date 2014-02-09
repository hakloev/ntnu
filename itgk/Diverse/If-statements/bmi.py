# BMI - calculator
# Håkon Ødegård Løvdal

def main(): 
	weight = float(input('Enter weight: '))
	height = float(input('Enter height (in meters): '))
	bmi(weight, height)

def bmi(w, h):
	bmi = w / (h ** 2)
	out(bmi)
	# BMI = ( Weight in Kilograms / ( Height in Meters x Height in Meters ) )	


def out(bmi):
	if bmi < 18.5:
		print(bmi)
		print("You're underweight")
	elif bmi >= 18.5 and bmi <= 25:
		print(bmi)
		print("You're optimal")
	elif bmi > 25:
		print(bmi)
		print("You're overweight")
	
	# BMI = ( Weight in Kilograms / ( Height in Meters x Height in Meters ) )	

main()
