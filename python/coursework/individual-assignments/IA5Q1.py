#Kike Otufale
#aotufale1@student.gsu.edu

print('Select a category: ')
print ('1. Electronics')
print ('2. Furniture')

category = int(input('Enter your choice (1 or 2): '))

code = input('Now enter the product code: ')

if category == 1:
    if code[0] != 'E' or len(code) != 10 or code[-1] != 'X':
        print('Error! The entered product code is invalid')
    else: 
        print('Next')
elif category == 2: 
    if code[0] != 'F' or len(code) != 9 or code[-1] != 'W':
        print('Error! The entered product code is invalid')
    else: 
        print('Next')
