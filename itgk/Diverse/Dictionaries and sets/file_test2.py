# 2012
# Håkon Ødegård Løvdal © 

import pickle

inputfile = open('test.dat', 'rb')

dic = pickle.load(inputfile)

inputfile.close()

print(dic)

