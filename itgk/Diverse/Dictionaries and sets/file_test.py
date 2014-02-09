# 2012
# Håkon Ødegård Løvdal © 

import pickle

output_file = open('test.dat', 'wb')

dic = {'Håkon':'hakloev@gmail.com', 'Fredrik':'fredrikbnf@hotmail.com', 'Steinar': 'steinar.loevdal@gmail.com'}

pickle.dump(dic, output_file)

output_file.close()
