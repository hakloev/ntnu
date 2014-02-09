def main():

	present_value = float(input("What's the present value: "))
	monthly_intrest = float(input("What's the monthly intrest: "))
	months = int(input('How many months will it be in the account: '))
	print('The future value will be', + \
		future_value(present_value, monthly_intrest, months))
		

def future_value(now, intrest, months):
	return (now * ((1 + intrest) ** months))

main()