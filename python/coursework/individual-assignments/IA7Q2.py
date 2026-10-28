#Kike Otufale
#aotufale1@student.gsu.edu


s = input('Please enter a string: ')


def remove_letters(s):
    new_string = ''
    for i in range(len(s)):
        if not s[i].isalpha():
            new_string = new_string + s[i]
        else:
            continue
    print(new_string) 
    

remove_letters(s)