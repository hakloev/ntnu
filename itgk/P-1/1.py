import math #importerer modulen math

print('I programmet regnes det ut kartistiske koordinater for tre gitte\n'
      'koordinater i polarkoordinatsystemet!')
print('\n')

pi = 3.1415 # Variabelen pi

# Regner ut første koordinat
print('Først la oss regne ut koordinatet:\n'
      '\n'
      '\t (3, (π / 2))')
firstX = format(3 * math.cos(pi / 2), '.0f') #Def
firstY = format(3 * math.sin(pi / 2), '.0f')
print('\n')
print('Som i det kartistiske koordinatsystemet blir: ')
print('\n')
print('\t', '(', firstX, ',', firstY, ')')
print('\n')

#Regner ut andre koordinat
print('Så kan vi regne ut koordinatet:\n'
      '\n'
      '\t (2.3, (π / 3))') 
secondX = format(2.3 * math.cos(pi / 3), '.0f')
secondY = format(2.3 * math.sin(pi / 3), '.0f')
print('\n')
print('Som i det kartistiske koordinatsystemet blir: ')
print('\n')
print('\t', '(', secondX, ',', secondY, ')')
print('\n')

#Regner ut tredje koordinat
print('Og sist men ikke minst, koordinatet:\n'
      '\n'
      '\t (5, 0)')
thirdX = format(5 * math.cos(0), '.0f')
thirdY = format(5 * math.sin(0), '.0f')
print('\n')
print('Som i det kartistiske koordinatsystemet blir: ')
print('\n')
print('\t', '(', thirdX, ',', thirdY, ')')


