'''
Ask the user for:
• Loan amount
• Annual interest rate (as % e.g. 5 for 5%)
• Number of years
Then calculate the monthly payment using the formula:

'''

LoanAmount = int(input('Enter the Loan amount: '))
AR = int(input('Enter the Annual Interest Rate: ')) / 100
Year = int(input('Enter number of years: '))

Monthlyrate = (AR / 12)
months = Year * 12


payment = (LoanAmount * Monthlyrate / (1 - (1 + Monthlyrate) ** (-months)))

print (payment)