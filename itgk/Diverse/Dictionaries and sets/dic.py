# 2012
# Håkon Ødegård Løvdal © 

dic = {'Kyle':'940', 'Ross':'50', 'Chandler': '008'}

dic['rolf'] = '000'

print(dic)

x = dic.pop('Kyle', 'not there')

print(x)

k,y = dic.popitem()

print(k, y)
