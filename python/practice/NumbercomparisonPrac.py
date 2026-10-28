'''
Ask the user for two numbers.
Print which number is larger.
If the numbers are equal, print "The numbers are equal".

'''

a = int(input('Enter a number: '))
b = int(input('Enter a number: '))

if a > b:
    print (a)
elif b > a:
    print (b)
else:
    if a == b:
        print ('The numbers are equal')
