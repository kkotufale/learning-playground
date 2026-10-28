# Name: Kike Otufale
# Email Address: aotufale1@student.gsu.edu


year = int(input('Enter year: '))
month = str(input('Enter month (three letters:) '))
day = int(input('Enter day (1-31): '))


maxday = 31
maxdays = 30
febdays = 0

if year % 4 == 0:
    febdays = 29
    print(year, 'is a leap year.')
else:
    febdays = 28    
    print(year, 'is not a leap year')
     

    
daysindex = 0                

if month == 'Jan' and 1 <= day <= maxday:
    print ('The date is valid')
    daysindex = day
    print ('That date is day', (daysindex) , 'of the year')
elif month == 'Feb' and 1 <= day <= febdays:
    print('The date is valid')
    daysindex = 31 + day
    print('That date is day', (daysindex), 'of the year')
elif month == 'Mar' and 1 <= day <= maxday:
    print('The date is valid')
    daysindex = 31 + febdays + day
    print ('That date is day', (daysindex) , 'of the year')
elif month == 'Apr' and 1 <= day <= maxdays:
    print('The date is valid')
    daysindex = 31 + febdays + 31 + day
    print ('That date is day', (daysindex) , 'of the year')       
elif month == 'May' and 1 <= day <= maxday:
    print('The date is valid')
    daysindex = 31 + febdays + 31 + 30 + day
    print ('That date is day', (daysindex) , 'of the year')          
elif month == 'Jun'and 1 <= day <= maxdays:
    print('The date is valid')
    daysindex = 31 + febdays + 31 + 30 + 31 + day
    print ('That date is day', (daysindex) , 'of the year')
elif month == 'Jul' and 1 <= day <= maxday:
    print('The date is valid')
    daysindex = 31 + febdays + 31 + 30 + 31 + 30 + day 
    print ('That date is day', (daysindex) , 'of the year')
elif month == 'Aug' and 1 <= day <= maxday:
    print('The date is valid')
    daysindex = 31 + febdays + 31 + 30 + 31 + 30 + 31 + day
    print ('That date is day', (daysindex) , 'of the year')     
elif month == 'Sep' and 1 <= day <= maxdays: 
    print('The date is valid')
    daysindex = 31 + febdays + 31 + 30 + 31 + 30 + 31 + 31 + day
    print ('That date is day', (daysindex) , 'of the year')     
elif month == 'Oct' and 1 <= day <= maxday: 
    print('The date is valid')
    daysindex = 31 + febdays + 31 + 30 + 31 + 30 + 31 + 31 + 30 + day
    print ('That date is day', (daysindex) , 'of the year')     
elif month == 'Nov' and 1 <= day <= maxdays:
    print('The date is valid')
    daysindex = 31 + febdays + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + day
    print ('That date is day', (daysindex) , 'of the year')
elif month == 'Dec' and 1 <= day <= maxday:
    print('The date is valid')
    daysindex = 31 + febdays + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + day
    print ('That date is day', (daysindex) , 'of the year')
else:
    print('Invalid date entered')
