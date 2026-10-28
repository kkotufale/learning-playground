# Name: Kike Otufale
# Email Address: aotufale1@student.gsu.edu


import math

distance = float(input('Enter the distance from the observer to the base of the mountain (in meters): '))
angle = math.radians(float(input('Enter the angle of elevation to the mountain peak (degrees): ')))

height = round(distance * (math.tan(angle)), 2)
slant = round(distance / (math.cos(angle)), 2)
angleofdepression = round(math.degrees(math.atan((height/distance))),2)

print ('Mountain height (h): ', height, 'meters')
print ('Slant distance to the peak (s): ', slant, 'meters')
print ('Angle of depression from peak (θ_2): ', angleofdepression)