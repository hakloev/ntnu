hender = 2598960 # antall mulige pokerhender

print('Resultatene fra "2test.py" gir oss at de ulike verdiene for \n'
        'binomialkoeffisientene gitt i oppgaven blir: \n')

print('\t 78, 36, 11 og 4\n')

totalt = 78 + 36 + 11 + 4

print('Dette gir oss totalt:', totalt, 'mulige hender for to par \n')

print('Vi har oppgitt at antall mulige poker hender er: ', hender, '\n')

delt = totalt / hender

print('Dette betyr at det er ', format(delt, '.6%'), 'sjanse for å få to par!')







