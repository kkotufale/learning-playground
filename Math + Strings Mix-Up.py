# Problem 1: Math + Strings Mix-Up
#Write a Python program that:
#Asks the user for a radius (as a float).
#Uses the math module to calculate:
#The area of a circle
#The circumference of the circle
#Prints the results with 2 decimal places.
#Then, ask the user for their name, and use the string repetition operator * to print a decorative banner like this:
#*********************
#*   Welcome, Kike!  *
#*********************
#(the number of * should match the length of “Welcome, name!” + 4)

import math

radius = float(input('Please enter the radius: '))

area = math.pi * (radius ** 2)
circum = 2 * math.pi * radius

print ('The area of the circle is: ', round(area,2) , 'and the circumference of the circle is: ', round(circum,2) )

name =input ('What is your name? ')

print ('*' * (len('Welcome, ') + len(name) + len('!') + 7))
print ('*   Welcome',name, '!  *')
print ('*' * (len('Welcome, ') + len(name) + len('!') + 7))
