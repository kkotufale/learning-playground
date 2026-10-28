#Kike Otufale
#aotufale1@student.gsu.edu

price = (int(input('Enter the price ($): ')))
number = (int(input('Enter the number of items purchased: ')))
rate = (int(input('Enter the tax rate(%): ') ) / 100)


taxAmount = price * number * rate
totalPrice = price * number + taxAmount

print('The tax amount is $:', (taxAmount), 'and the total price is $:', (totalPrice))


