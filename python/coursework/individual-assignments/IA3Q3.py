#Kike Otufale
#aotufale1@student.gsu.edu


x = int(input('Enter an odd number between 2 and 20: '))

if x%2 != 0 and 2 <= x <= 20:
    print('Criteria Met!')
    y = int(input('Now enter a second number: '))

    if y%x == 0:
        print('Yes!', y , 'is a multiple of',x)
    else:
        print('Oops!', y ,'is not a multiple of 15')
else:
    print('Oops! That’s not an odd number between 2 and 20. Try again.')


