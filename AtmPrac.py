'''

Ask the user for a bank balance.
Ask the user to withdraw an amount.
If the withdrawal is more than the balance, print "Insufficient funds".
Otherwise, subtract the amount and print the new balance.

'''

a = int(input('Enter your bank balance: '))
b = int(input('How much do you want to withdraw? '))

if b > a: 
    print ('Insufficient funds')
else:
    a = a - b
    print('Your new balance is', a)