even = 0
odd = 0

for i in range(0,100):
    value = int(input('Please enter a value: '))
    if value == 0:
        break
    elif value < 0:
        continue
    elif value % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print('There are', str(even), 'even numbers and', str(odd),'odd numbers.')




