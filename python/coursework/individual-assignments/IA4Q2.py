# Name: Kike Otufale
# Email Address: aotufale1@student.gsu.edu


letter = (input('Enter a letter: '))


if len(letter) != 1 or letter in '0123456789' :
    print(letter, 'is an invalid input')
elif letter in 'AaEeIiOoUu':
            print(letter, 'is a vowel')
elif letter not in 'AaEeIiOoUu':
            print(letter, 'is a consonant')