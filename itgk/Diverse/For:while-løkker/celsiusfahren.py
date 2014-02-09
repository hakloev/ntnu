# Fahrenheit --> Celsius 0-20
# Håkon Ødegård Løvdal

# fahren = ((9/5)*celsius)+32

print('Celsius\tFahrenheit')
print('-------------------')

for celsius in range(0, 21, 1):
	fahrenheit = ((9/5)*celsius)+32
	print(celsius, '\t', format(fahrenheit, '.2f'))

