total = ''
f = open('total.srt', 'r')
line = f.readline()
while line != '':
	total += line
	line = f.readline()
f.close()

where = total.find('1413')
where_to = total.find('1414')
print(total[where:where_to - 1])