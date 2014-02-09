# Håkon Ødegård Løvdal

# Skal skrive om fra Celsius til Fahrenheit

celsius = float(input('Hvor mange grader celsius er det? ')) # input fra bruker, float for desimaltall

fahrenheit = ((9 / 5) * celsius) + 32 # formel for å regne om fra celsius til fahrenheit, bruker var celsius

print(format(celsius, '.2f'), 'grader celsius tilsvarer', \
    format(fahrenheit, '.2f'), 'grader fahrenheit!') 
