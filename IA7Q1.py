#Kike Otufale
#aotufale1@student.gsu.edu


rate = float(input('Please enter the exchange rate: '))

def RMB_to_USD(amount):
    new_rate = amount / rate
    print('Equivalent amount in USD is:', round(new_rate,2))


def USD_to_RMB(amount):
    new_rate = rate * amount
    print('Equivalent amount in RMB is:', round(new_rate,2))

while True:
    option = input('Please enter "1" for RMB to USD,\n"2" for USD to RMB\nor "exit" to exit the program: ')
    if option == '1':
        amount = float(input('Please enter the amount you would like to convert: '))
        RMB_to_USD(amount)
    elif option == '2':
        amount = float(input('Please enter the amount you would like to convert: '))
        USD_to_RMB(amount)
    elif option == 'exit':
        print('Goodbye')
        break
    else: 
        continue


