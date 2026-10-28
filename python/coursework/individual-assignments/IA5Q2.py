#Kike Otufale
#aotufale1@student.gsu.edu

chars = (input('Enter two characters: '))
digit = ''
letter = ''

if len(chars) != 2 or chars[0].isalpha() or chars[1].isdigit():
    print ('Invalid input')
    exit()

if chars[0] == '1':
        digit = ('Beginner')
elif chars[0] == '2':
        digit = ('Intermediate')
elif chars[0] == '3':
        digit = ('Advanced')
else: 
    print('Does not exist')
    exit()

if chars[1] in 'Tt':
        letter = ('Tennis')
elif chars[1] in 'Bb':
        letter = ('Basketball')
elif chars[1] in 'Ss':
        letter = ('Soccer')
else:
    print('Does not exist')
    exit()

print (digit, 'in', letter)





