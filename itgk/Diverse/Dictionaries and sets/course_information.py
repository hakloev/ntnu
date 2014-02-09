# 2012
# Håkon Ødegård Løvdal © 

roomNumber = {'CS101':'3004', 'CS102':'4501', 'CS103':'6755', 'NT110':'1244', 'CM241':'1411'}
instructor = {'CS101':'Haynes', 'CS102':'Alvarado', 'CS103':'Rich', 'NT110':'Burke', 'CM241':'Lee'}
meetingTime = {'CS101':'8:00 a.m.', 'CS102':'9.00 a.m.', 'CS103':'10 a.m.m', 'NT110':'11:00 a.m.', 'CM241':'1:00 p.m.'}

course = str(input('Enter your course number: '))

print(roomNumber[course], instructor[course], meetingTime[course])