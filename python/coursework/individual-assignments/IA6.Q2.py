kilo = 0
miles = 0



print ('Kilometers      |       Miles')

for kilo in range(0,101,10):
    miles = round((kilo * .621371), 4)
    print(str(kilo) + '               |               ' + str(miles))