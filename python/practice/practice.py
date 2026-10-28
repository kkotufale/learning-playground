'''
Ask the user for the length and width of a rectangle, then calculate and print:
The area
The perimeter

'''

x = int(input('Enter the length of the rectangle: '))
y = int(input('Enter the width of the rectangle: '))

area = x * y 
perimeter = (x+y) * 2
print('The area of the rectangle is', area)
print('The perimeter of the rectangle is', perimeter)