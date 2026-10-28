import IA7Q3Convert



print('1. Convert Celsius to Fahrenheit\n2. Convert Fahrenheit to Celsius: ')

choice = input("Enter your choice (1 or 2): ")    
while True:
    if choice == '1':
        celsius = float(input('Enter a temperature in celsius: '))
        IA7Q3Convert.celsiusToFahrenheit(celsius)
    elif choice == '2':
        fahrenheit = float(input('Enter a temperature in fahrenheit: '))
        IA7Q3Convert.fahrenheitToCelsius(fahrenheit)
    else: 
        continue
