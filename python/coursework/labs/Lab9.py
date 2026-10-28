num = int(input('Enter the number of students: '))
highest_score = 0
highest_name = ''

for i in range(num):
    name = input('Enter a student name:')
    score = float(input('Enter a student score:'))
    if score > highest_score:
        highest_score = score
        highest_name = name
    
    
print('Top student', highest_name, 'score is', highest_score)

