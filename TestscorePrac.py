'''

Ask the user for a test score (0–100).
Print the grade based on:
"A" if score ≥ 90
"B" if score ≥ 80
"C" if score ≥ 70
"D" if score ≥ 60
"F" otherwise

'''

score = int(input('Enter your test score: '))

if score < 0 or score > 100:
    print('Error, please enter a value 0 - 100')
elif score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print( 'C')        
elif score >= 60:
    print ('D')


else: 
    print( 'F' )


    
    