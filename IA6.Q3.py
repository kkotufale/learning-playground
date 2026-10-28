string = input('Enter a string: ')
vowels = 0 
random = 0
lower = 0
upper = 0
digits = 0

for i in range (0, (len(string))):

    char = string[i]

    if char.lower() in 'aeiou':
        vowels += 1
    elif char.isupper():
        upper += 1
    elif char.islower():
        lower += 1
    elif char.isdigit():
        digits += 1    
    elif char in ('.', ',', '?', '!'):
        random += 1
        

print('Number of lowercase letters: ', lower)
print('Number of uppercase letters: ', upper)
print('Number of digits: ', digits)
print('Number of vowels: ', vowels)
print('Number of punctuation marks: ', random)