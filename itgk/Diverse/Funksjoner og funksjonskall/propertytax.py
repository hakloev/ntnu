def main():
	# Get actual value from user
	actual_value = float(input('Type in the value of your property: '))
	# Pass argument to assessment function
	assessment(actual_value)

def assessment(value):
	# Calculate assessment value
	assessment_value = value * 0.6
	# Print assessment value
	print('Its assessment value is:', assessment_value)
	# Pass argument to tax function
	tax(assessment_value)

def tax(value):
	# Calculate tax
	tax_value = ((0.64 * value)/100)
	# Print tax value
	print('and the tax value is', tax_value)

main()