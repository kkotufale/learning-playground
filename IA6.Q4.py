#Kike Otufale
#aotufale1@student.gsu.edu


def ISBN_transfer(isbn9):
    if len(isbn9) != 9: 
        print('Incorrect input. It must have exact 9 digits')
        exit()
    checksum = 0
    for i in range(9):
        checksum += int(isbn9[i]) * (i + 1)

    d10 = ''
    if checksum % 11 == 10:
        d10 = 'X'
    else:
        d10 = str(checksum % 11)

    ISBN10 = isbn9 + d10
    return ISBN10


isbn9 = input('Enter the first 9 digits of an ISBN: ')
isbn10 = ISBN_transfer(isbn9)
print('The ISBN-10 number is', isbn10)