import math

print('Degree            Sin            Cosine')
    
    
    
for degree in range(0,361,10):    
    sin = round(math.sin(math.radians(degree)),4)
    cos = round(math.cos(math.radians(degree)),4)
    print(degree,"          ",sin,"          ",cos)