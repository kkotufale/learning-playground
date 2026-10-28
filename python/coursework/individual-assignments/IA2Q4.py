#Kike Otufale
#aotufale1@student.gsu.edu

PrincipalAmount = int(input('Enter the initial investment amount ($): '))
AnnualRate = int(input('Enter the annual interest rate (in %): ')) / 100
Years = int(input('Enter the number of years the investment will grow: '))
Compoundings_Per_Year = int(input('Enter the number of times the interest is compounded per year: '))

TotalAmount = (PrincipalAmount * ((1 + (AnnualRate/Compoundings_Per_Year))) ** (Compoundings_Per_Year * Years))


print(('Total amount is $ '), float(TotalAmount))

