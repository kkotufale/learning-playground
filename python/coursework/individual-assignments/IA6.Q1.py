


excellent_count = 0
poor_count = 0
total_ratings_count = 0
total_sum = 0

while True:
    ratings = input('Enter a rating (or type "done" to finish): ')
    if ratings == 'done':
        break
    elif ratings == 'done' and total_ratings_count == 0:
        print('No ratings entered')
    else: 
        ratings = float(ratings)
        total_sum += ratings
        total_ratings_count += 1

        if ratings >= 4.5:
            excellent_count += 1
        elif ratings <= 2.0:
            poor_count += 1
            
print('Total ratings entered: ' + str(total_ratings_count))
print('Number of excellent ratings (>= 4.5): ' + str(excellent_count))
print('Number of poor ratings (<= 2.0) ' + str(poor_count))
print('Average rating: ' + str(total_sum/total_ratings_count))
print('Ratio of excellent ratings: ' + str((excellent_count/total_ratings_count)* 100))


    
    
