x = int(input('Enter the total number of attendees: '))
y = 400
z = ((x - 15 ) * 8.50) + y

if x <= 15:
    print('The total cost of the event is $400.')

if x > 15: 
    print('The total cost of the event is: ', round(z, 2))