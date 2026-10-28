#Kike Otufale
#aotufale1@student.gsu.edu

isbn9 = input(' Enter the first 9 digits of an ISBN as a string: ')

if len(isbn9) != 9: 
    print('Incorrect input. It must have exact 9 digits')
    exit()

checksum = (int(isbn9[0])*1 + int(isbn9[1])*2 + int(isbn9[2])*3 + int(isbn9[3])*4 + int(isbn9[4])*5 + int(isbn9[5])*6 + int(isbn9[6])*7 + int(isbn9[7])*8 + int(isbn9[8])* 9) % 11
d10 = ''

if checksum == 10:
    d10 = 'X'
else:
    d10 = str(checksum)

ISBN10 = str(isbn9 + d10)

print ('The ISBN-10 number is', ISBN10)