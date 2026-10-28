#Step 5: Two-Way Selection Statements (if-else)
#Write a program that accepts three integers and prints which one is the smallest.


x = int(input('Enter a number: '))
y = int(input('Enter another number: '))
z = int(input('Enter another number: '))

if x<=y and x<=z:
    min=x 
    print('Min value is x', x)
elif y<=x and y<=z:
    min = y
    print('Min value is y', y)
elif z<=x and z<=y:
    min = z
    print('Min value is z', z)
