from itertools import permutations
from math import gcd

def genTriples(k):
    n,m = 1,2
    while m*m+1<k:                  
        if n>=m: n,m = m%2,m+1      
        z = m*m+n*n                 
        if z >= k: n=m;continue     
        if gcd(n,m) == 1:           
            yield m*m-n*n,2*m*n,z   
        n += 2

pythagtrips = [[x,y,z] for x,y,z in genTriples(1000)]

temp = [[25,69,77], [49, 57, 65], [49, 87, 95], [69, 77, 85], [77, 81, 95]]
tr = []

while temp != []:
    a = temp.pop()
    newa = [i for i in permutations(a)]
    tr.append(newa)
    
nrrs = []

while pythagtrips != []:
    a = pythagtrips.pop()
    newa = [i for i in permutations(a)]
    nrrs.append(newa)


for a in tr:
    ac1 = a[0]
    ac2 = a[1]
    ac4 = a[2]
    
    