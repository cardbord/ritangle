from itertools import permutations
from math import gcd, sqrt


def check(arr,nums):
    for num in nums:
        if num in arr:
            return False
    return True


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
    tr.extend(newa)

nrrs = []

while pythagtrips != []:
    a = pythagtrips.pop()
    newa = [i for i in permutations(a)]
    nrrs.extend(newa)


ans = []
for a in tr:
    ans = []
    ac1 = a[0]
    ac2 = a[1]
    ac4 = a[2]
    ans.extend(a)
    for b in nrrs:
        bans = ans.copy()
        if (b[0]) in range(10,100) and (b[1]) in range(10,100) and (b[2]) in range(10,100) and check(ans,b):
            ac11 = b[0]
            dn10 = b[1]
            dn12 = b[2]
            bans.extend(b)
            
            for c in nrrs:
                cans = bans.copy()
                if (c[0]) > 99 and (c[1]) > 99 and (c[2]) in range(10,100) and str(c[1])[2] == str(c[0])[1] and str(c[2])[0] == str(ac1)[0] and str(c[0])[0] == str(dn10)[1] and check(bans,c):
                    ac13 = c[0]
                    dn7 = c[1]
                    dn1 = c[2]
                    cans.extend(c)
                    for d in nrrs:
                        dans = cans.copy()
                        if (d[0]) > 99 and (d[1]) > 99 and (d[2]) in range(10,100) and str(d[2])[0] == str(ac4)[1] and str(d[0])[2] == str(dn12)[1] and str(d[1])[2] == str(d[0])[1] and check(cans, d):
                            ac14 = d[0]
                            dn9 = d[1]
                            dn5 = d[2]
                            dans.extend(d)
                            
                            for i in range(10):
                                
                                for j in range(1,10):
                                    
                                    
                                    dn2 = int(str(ac2)[0] + str(i)+ str(ac11)[0])
                                    dn3 = int(str(ac2)[1] + str(j)+ str(ac11)[1])
                                    if sqrt(dn2+dn3).is_integer() and check(dans,[dn2,dn3]):
                                        
                                        ac6 = int(str(dn1)[1] + str(dn7)[0] + str(i))
                                        ac8 = int(str(j) + str(dn9)[0] + str(dn5)[1])
                                        if check(dans,[ac6,ac8]):

                                            allnums = [ac11, dn10, dn12, ac13, dn7, dn1, dn9, dn5, ac14, ac6, ac8, dn2, dn3]
                                            for num in allnums:
                                                for anothernum in allnums:
                                                    if num==anothernum:
                                                        pass
                                                    else:
                                                        if num - anothernum == ac1 + ac2 + ac4:
                                                            print('FITS CRITERIA ',[(i[2:]+i[:2],globals()[i]) for i in globals() if ('ac' in i or 'dn' in i) and i != '__package__' and i != '__cached__'])
                else:
                    pass
        else:
            pass


