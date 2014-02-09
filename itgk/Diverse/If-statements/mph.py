# Håkon Ødegård Løvdal

print("Distance traveled while moving in 60 MPH, do you want to find out?")
answer = str(input('Yes or no? '))
go = "y" or "yes"
stop = "n" or "no"

speed = 60

if answer == go:
    time = int(input('How many hours have you been driving for? '))
    distance = (speed * time)
    print('Then you have driven', distance, 'miles :)')   
elif answer == stop:
    print('Okey, you are missing something, but okey, good bye! :D')    
    
    
        


