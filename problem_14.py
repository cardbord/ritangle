#C (a,b)
#A (b,c)
#B (c,a)
from math import sqrt


for c in range(1,1000000):
    c1 = c/1000
        
    dist1 = c1
    dist2 = c1
    dist3 = c1*sqrt(2)

    if round(dist1 + dist2 + dist3,3) == 1:    
        print(c/1000)
        
    
