#Kike Otufale
#aotufale1@student.gsu.edu

import IA7Q3Convert


while True:
    print('1. Convert Celsius to Fahrenheit\n2. Convert Fahrenheit to Celsius: ')
    choice = input("Enter your choice (1 or 2): ")    
    if choice == '1':
        celsius = float(input('Enter a temperature in celsius: '))
        print('Fahrenheit is', (round(IA7Q3Convert.celsiusToFahrenheit(celsius),2)))
    elif choice == '2':
        fahrenheit = float(input('Enter a temperature in fahrenheit: '))
        print('Celsius is', (round(IA7Q3Convert.fahrenheitToCelsius(fahrenheit), 2)))
    else: 
        break
