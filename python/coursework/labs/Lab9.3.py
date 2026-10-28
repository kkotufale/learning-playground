string = input('Enter a string: ')
vowels = 0
cons = 0

for char in string:
    
    if char.lower() in 'aeio':
        vowels = vowels + 1
    elif char.isalpha():
        cons = cons + 1

        
print('The number of vowels is: ', vowels, 'The number of constants is: ', cons)

