# Charge Account Validation

accounts_file = open('charge_accounts.txt', 'r')

accounts_list = accounts_file.readlines()

accounts_file.close()

index = 0
while index < len(accounts_list):
	accounts_list[index] = accounts_list[index].rstrip('\n')
	index += 1

search  = int(input('Enter your account number: '))

if str(search) in accounts_list:
	print('Valid')
else:
	print('Unvalid')