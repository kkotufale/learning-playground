#Kike Otufale
#aotufale1@student.gsu.edu


x = int(input('Enter the total number of attendees: '))
base = 400
y = base



if x > 15: 
    y = ((x - 15 ) * 8.50) + base
    
print('The total cost of the event is: $', round(y, 2))