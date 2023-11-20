#m, n
#factors(n) =6, factors(m) = 6
#d = factors(m*n) 

#highest(dlist)

from functools import reduce
def factors(n):    
    return set(reduce(list.__add__, 
                    ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

print(len(factors(2023)))

dlist = []
def main():
    for n in range(1,10000):
        for m in range(1,10000):
            
            if len(factors(n)) == 6 and len(factors(m))==6:
                if not len(factors(n*m)) in dlist:
                    dlist.append(len(factors(n*m)))

    

        if n %300==0:
            total=0
#arr = [15, 16, 20, 20, 16, 20, 24, 24, 20, 24, 20, 27, 20, 20, 24, 24, 20, 24, 20, 27, 20, 24, 20, 24, 20, 36, 20, 24, 20, 20, 24, 21, 20, 36, 24, 20, 36, 24, 20, 20, 20, 36, 20, 24, 24, 20, 27, 24, 24, 20, 20, 20, 24, 36, 20, 20, 20, 36, 24, 27, 20, 20, 24, 36, 20, 24, 20, 36, 24, 20, 24, 20, 36, 20, 36, 24, 20, 24, 20, 20, 24, 20, 24, 20, 36, 24, 20, 20, 36, 20, 20, 24, 36, 20, 36, 36, 27, 24, 20, 20, 24, 20, 36, 24, 36, 20, 20, 24, 20, 24, 20, 24, 36, 20, 20, 24, 36, 20, 27, 20, 20, 20, 36, 20, 24, 20, 36, 24, 36, 20, 24, 20, 24, 20, 20, 20, 36, 24, 20, 24, 20, 20, 20, 24, 36, 20, 36, 24, 20, 36, 20, 24, 20, 36, 36, 20, 20, 24, 36, 27, 20, 20, 24, 24, 20, 36, 20, 24, 20, 24, 20, 20, 24, 20, 20, 24, 36, 24, 20, 36, 36, 36, 20, 20, 20, 36, 20, 24, 20, 24, 20, 20, 36, 20, 24, 36, 20, 36, 20, 24, 36, 24, 36, 20, 20, 24, 36, 24, 20, 24, 20, 36, 20, 20, 24, 20, 20, 36, 36, 20, 24, 20, 24, 20, 20, 20, 24, 36, 20, 24, 20, 20, 20, 24, 27, 20, 36, 36, 24, 24, 20, 20, 36, 20, 36, 20, 20, 24, 20, 36, 36, 20, 20, 36, 20, 24, 24, 20, 36, 24, 20, 24, 36, 20, 24, 36, 20, 27, 36, 20, 20, 20, 20, 24, 36, 16, 15, 24, 24, 21, 24, 20, 27, 24, 20, 24, 24, 24, 24, 27, 20, 24, 20, 24, 24, 24, 20, 24, 20, 24, 36, 24, 20, 24, 24, 27, 16, 24, 36, 20, 24, 36, 20, 24, 24, 24, 36, 24, 20, 27, 24, 24, 20, 20, 24, 24, 24, 20, 36, 24, 24, 24, 36, 20, 24, 24, 24, 20, 36, 24, 20, 24, 36, 27, 24, 20, 24, 36, 24, 36, 20, 24, 20, 24, 24, 20, 24, 27, 24, 36, 20, 24, 24, 36, 24, 24, 20, 36, 24, 36, 36, 24, 20, 24, 24, 20, 24, 36, 20, 36, 24, 24, 20, 24, 20, 24, 20, 36, 24, 24, 27, 36, 24, 24, 24, 24, 24, 36, 24, 20, 24, 36, 20, 36, 24, 20, 24, 20, 24, 24, 24, 36, 20, 24, 20, 24, 24, 24, 20, 36, 24, 36, 20, 24, 36, 24, 20, 24, 36, 36, 24, 24, 20, 36, 24, 24, 24, 20, 20, 24, 36, 24, 27, 24, 20, 24, 24, 20, 24, 24, 20, 36, 20, 24, 36, 36, 36, 24, 24, 24, 36, 24, 20, 24, 27, 24, 24, 36, 24, 20, 36, 24, 36, 24, 20, 36, 20, 36, 24, 24, 20, 36, 20, 24, 20, 24, 36, 24, 24, 20, 24, 24, 36, 36, 24, 20, 24, 20, 24, 24, 24, 20, 36, 24, 20, 24, 24, 24, 20, 24, 24, 36, 36, 20, 20, 24, 24, 36, 24, 36, 24, 24, 20, 24, 36, 36, 24, 24, 36, 24, 27, 20, 24, 36, 20, 24, 20, 36, 24, 20, 36, 24, 24, 36, 24, 24, 24, 24, 20, 36, 20, 24, 15, 20, 16, 20, 27, 16, 20, 36, 20, 24, 20, 20, 24, 36, 20, 36, 20, 36, 20, 36, 20, 36, 20, 24, 20, 36, 20, 20, 24, 36, 20, 27, 36, 20, 24, 36, 20, 20, 20, 24, 20, 36, 24, 20, 36, 36, 36, 20, 20, 20, 36, 24, 20, 20, 20, 24, 36, 36, 20, 20, 36, 36, 20, 36, 20, 24, 24, 20, 36, 20, 27, 20, 36, 36, 20, 36, 20, 20, 36, 20, 24, 20, 24, 36, 20, 20, 24, 20, 20, 36, 36, 20, 27, 36, 36, 36, 20, 20, 36, 20, 24, 36, 36, 20, 20, 36, 20, 36, 20, 36, 24, 20, 20, 24, 24, 20, 36, 20, 20, 20, 36, 20, 36, 20, 24, 36, 36, 20, 36, 20, 36, 20, 20, 20, 24, 36, 20, 36, 20, 20, 20, 36, 36, 20, 27, 36, 20, 24, 20, 36, 20, 36, 24, 20, 20, 36, 36, 36, 20, 20, 36, 36, 20, 24, 20, 24, 20, 36, 20, 20, 36, 20, 20, 36, 24, 36, 20, 27, 36, 24, 20, 20, 20, 36, 20, 36, 20, 24, 20, 20, 24, 20, 36, 36, 20, 36, 20, 36, 36, 36, 24, 20, 20, 36, 36, 36, 20, 36, 20, 24, 20, 20, 36, 20, 20, 36, 36, 20, 36, 20, 36, 20, 20, 20, 36, 24, 20, 36, 20, 20, 20, 36, 36, 20, 24, 36, 36, 36, 20, 20, 24, 20, 36, 20, 20, 36, 20, 27, 24, 20, 20, 24, 20, 24, 36, 20, 36, 36, 20, 36, 24, 20, 36, 36, 20, 36, 36, 20, 20, 20, 20, 36, 36, 20, 24, 20, 15, 16, 20, 36, 24, 20, 27, 20, 36, 20, 20, 16, 36, 20, 36, 20, 24, 20, 36, 20, 36, 20, 27, 20, 36, 20, 20, 24, 36, 20, 24, 36, 20, 36, 36, 20, 20, 20, 36, 20, 36, 24, 20, 36, 36, 36, 20, 20, 20, 36, 36, 20, 20, 20, 36, 36, 36, 20, 20, 36, 24, 20, 36, 20, 36, 24, 20, 36, 20, 36, 20, 24, 36, 20, 36, 20, 20, 36, 20, 24, 20, 36, 36, 20, 20, 36, 20, 20, 36, 24, 20, 36, 27, 36, 36, 20, 20, 36, 20, 36, 36, 24, 20, 20, 36, 20, 36, 20, 36, 36, 20, 20, 24, 36, 20, 36, 20, 20, 20, 24, 20, 36, 20, 36, 36, 27, 20, 36, 20, 36, 20, 20, 20, 36, 36, 20, 36, 20, 20, 20, 36, 24, 20, 36, 36, 20, 36, 20, 36, 20, 24, 36, 20, 20, 36, 36, 36, 20, 20, 36, 36, 20, 36, 20, 24, 20, 36, 20, 20, 36, 20, 20, 36, 36, 36, 20, 36, 24, 36, 20, 20, 20, 36, 20, 36, 20, 24, 20, 20, 36, 20, 36, 24, 20, 27, 20, 36, 36, 36, 36, 20, 20, 36, 24, 36, 20, 36, 20, 36, 20, 20, 36, 20, 20, 36, 24, 20, 36, 20, 36, 20, 20, 20, 36, 36, 20, 36, 20, 20, 20, 36, 36, 20, 36, 27, 36, 36, 20, 20, 36, 20, 24, 20, 20, 36, 20, 36, 36, 20, 20, 36, 20, 24, 36, 20, 36, 36, 20, 36, 36, 20, 36, 36, 20, 36, 24, 20, 20, 20, 20, 36, 24, 16, 21, 16, 16, 11, 16, 36, 21, 16, 36, 16, 36, 16, 16, 21, 36, 16, 36, 16, 36, 16, 36, 16, 36, 16, 36, 16, 36, 16, 16, 21, 36, 16, 36, 36, 16, 36, 36, 16, 16, 16, 36, 16, 36, 21, 16, 36, 36, 36, 16, 16, 16, 36, 36, 16, 16, 16, 36, 36, 36, 16, 16, 36, 36, 16, 36, 16, 36, 21, 16, 36, 16, 36, 16, 36, 36, 16, 36, 16, 16, 36, 16, 21, 16, 36, 36, 16, 16, 36, 16, 16, 36, 36, 16, 36, 36, 36, 36, 16, 16, 36, 16, 36, 36, 36, 16, 16, 36, 16, 36, 16, 36, 36, 16, 16, 21, 36, 16, 36, 16, 16, 16, 36, 16, 36, 16, 36, 36, 36, 16, 36, 16, 36, 16, 16, 16, 36, 36, 16, 36, 16, 16, 16, 36, 36, 16, 36, 36, 16, 36, 16, 36, 16, 36, 36, 16, 16, 36, 36, 36, 16, 16, 36, 36, 16, 36, 16, 21, 16, 36, 16, 16, 36, 16, 16, 36, 36, 36, 16, 36, 36, 36, 16, 16, 16, 36, 16, 36, 16, 21, 16, 16, 36, 16, 36, 36, 16, 36, 16, 36, 36, 36, 36, 16, 16, 36, 36, 36, 16, 36, 16, 36, 16, 16, 36, 16, 16, 36, 36, 16, 36, 16, 36, 16, 16, 16, 36, 36, 16, 36, 16, 16, 16, 36, 36, 16, 36, 36, 36, 36, 16, 16, 36, 16, 36, 16, 16, 36, 16, 36, 36, 16, 16, 36, 16, 21, 36, 16, 36, 36, 16, 36, 36, 16, 36, 36, 16, 36, 36, 16, 16, 16, 16, 36, 36, 20, 24, 20, 20, 16, 15, 36, 24, 20, 36, 20, 36, 20, 20, 24, 27, 20, 36, 20, 36, 20, 36, 20, 36, 20, 36, 20, 36, 20, 20, 16, 36, 20, 36, 36, 20, 27, 36, 20, 20, 20, 36, 20, 36, 24, 20, 24, 36, 36, 20, 20, 20, 36, 36, 20, 20, 20, 36, 36, 36, 20, 20, 36, 27, 20, 36, 20, 36, 24, 20, 36, 20, 24, 20, 36, 36, 20, 36, 20, 20, 36, 20, 24, 20, 36, 36, 20, 20, 36, 20, 20, 36, 36, 20, 36, 24, 36, 36, 20, 20, 36, 20, 36, 36, 36, 20, 20, 36, 20, 36, 20, 36, 36, 20, 20, 24, 36, 20, 36, 20, 20, 20, 36, 20, 36, 20, 36, 36, 36, 20, 36, 20, 36, 20, 20, 20, 36, 36, 20, 36, 20, 20, 20, 36, 36, 20, 36, 36, 20, 36, 20, 36, 20, 36, 36, 20, 20, 36, 24, 36, 20, 20, 36, 36, 20, 36, 20, 24, 20, 36, 20, 20, 36, 20, 20, 36, 36, 36, 20, 36, 36, 36, 20, 20, 20, 27, 20, 36, 20, 24, 20, 20, 36, 20, 36, 36, 20, 36, 20, 36, 24, 36, 36, 20, 20, 36, 36, 36, 20, 36, 20, 36, 20, 20, 36, 20, 20, 24, 36, 20, 36, 20, 36, 20, 20, 20, 36, 36, 20, 36, 20, 20, 20, 36, 36, 20, 36, 36, 36, 36, 20, 20, 36, 20, 36, 20, 20, 36, 20, 36, 36, 20, 20, 36, 20, 24, 36, 20, 24, 36, 20, 36, 36, 20, 36, 36, 20, 36, 36, 20, 20, 20, 20, 36, 36, 24, 20, 27, 36, 36, 36, 15, 24, 36, 20, 36, 16, 36, 36, 36, 20, 36, 20, 36, 24, 36, 20, 36, 20, 36, 24, 36, 20, 36, 36, 36, 16, 36, 27, 20, 36, 24, 20, 36, 36, 36, 24, 36, 20, 36, 36, 24, 20, 20, 36, 36, 36, 20, 24, 36, 36, 36, 24, 20, 24, 36, 36, 20, 36, 36, 20, 36, 24, 36, 36, 20, 36, 27, 36, 36, 20, 36, 20, 36, 36, 20, 36, 36, 36, 24, 20, 36, 36, 24, 36, 36, 20, 36, 36, 27, 36, 24, 20, 36, 36, 20, 36, 24, 20, 36, 36, 36, 20, 36, 20, 36, 20, 24, 36, 36, 36, 24, 36, 24, 36, 36, 36, 36, 36, 20, 36, 24, 20, 36, 36, 20, 36, 20, 36, 36, 36, 24, 20, 36, 20, 36, 36, 36, 20, 36, 36, 27, 20, 36, 24, 36, 20, 36, 36, 24, 36, 36, 20, 36, 24, 36, 36, 20, 20, 36, 24, 36, 36, 36, 20, 36, 36, 20, 36, 36, 20, 24, 20, 36, 27, 36, 24, 36, 36, 36, 36, 36, 20, 36, 36, 36, 36, 24, 36, 20, 36, 36, 36, 36, 20, 36, 20, 24, 36, 36, 20, 36, 20, 36, 20, 36, 24, 36, 36, 20, 36, 36, 36, 36, 36, 20, 36, 20, 36, 36, 36, 20, 24, 36, 20, 36, 36, 36, 20, 24, 36, 24, 36, 20, 20, 36, 36, 24, 36, 36, 36, 36, 20, 36, 27, 24, 36, 36, 24, 36, 36, 20, 36, 36, 20, 36, 20, 24, 36, 20, 36, 36, 24, 36, 36, 36, 36, 36, 20, 36, 24, 27, 16, 24, 21, 24, 24, 15, 24, 36, 24, 20, 24, 24, 27, 36, 24, 36, 24, 36, 24, 36, 24, 36, 24, 20, 24, 36, 24, 24, 27, 36, 24, 24, 36, 24, 20, 36, 24, 24, 24, 20, 24, 36, 27, 24, 36, 36, 36, 24, 24, 24, 36, 20, 24, 24, 24, 20, 36, 36, 24, 24, 36, 36, 24, 36, 24, 20, 27, 24, 36, 24, 24, 24, 36, 36, 24, 36, 24, 24, 36, 24, 27, 24, 20, 36, 24, 24, 20, 24, 24, 36, 36, 24, 24, 36, 36, 36, 24, 24, 36, 24, 20, 36, 36, 24, 24, 36, 24, 36, 24, 36, 20, 24, 24, 27, 20, 24, 36, 24, 24, 24, 36, 24, 36, 24, 20, 36, 36, 24, 36, 24, 36, 24, 24, 24, 20, 36, 24, 36, 24, 24, 24, 36, 36, 24, 24, 36, 24, 20, 24, 36, 24, 36, 20, 24, 24, 36, 36, 36, 24, 24, 36, 36, 24, 20, 24, 27, 24, 36, 24, 24, 36, 24, 24, 36, 20, 36, 24, 24, 36, 20, 24, 24, 24, 36, 24, 36, 24, 27, 24, 24, 20, 24, 36, 36, 24, 36, 24, 36, 36, 36, 20, 24, 24, 36, 36, 36, 24, 36, 24, 20, 24, 24, 36, 24, 24, 36, 36, 24, 36, 24, 36, 24, 24, 24, 36, 20, 24, 36, 24, 24, 24, 36, 36, 24, 20, 36, 36, 36, 24, 24, 20, 24, 36, 24, 24, 36, 24, 24, 20, 24, 24, 20, 24, 27, 36, 24, 36, 36, 24, 36, 20, 24, 36, 36, 24, 36, 36, 24, 24, 24, 24, 36, 36, 20, 24, 20, 20, 16, 20, 36, 24, 15, 36, 20, 36, 20, 20, 24, 36, 20, 27, 20, 36, 20, 36, 20, 36, 20, 36, 20, 36, 20, 20, 24, 36, 20, 36, 36, 20, 36, 36, 20, 20, 20, 27, 20, 36, 16, 20, 36, 36, 36, 20, 20, 20, 36, 36, 20, 20, 20, 36, 36, 24, 20, 20, 36, 36, 20, 36, 20, 36, 24, 20, 36, 20, 36, 20, 27, 36, 20, 36, 20, 20, 36, 20, 24, 20, 36, 36, 20, 20, 36, 20, 20, 36, 36, 20, 24, 36, 36, 36, 20, 20, 36, 20, 36, 36, 36, 20, 20, 36, 20, 36, 20, 36, 36, 20, 20, 24, 36, 20, 36, 20, 20, 20, 36, 20, 36, 20, 36, 36, 24, 20, 36, 20, 36, 20, 20, 20, 36, 36, 20, 36, 20, 20, 20, 36, 36, 20, 36, 36, 20, 36, 20, 36, 20, 36, 36, 20, 20, 36, 27, 36, 20, 20, 36,]
            
            for num in dlist:
                total+=num
            print(total)


main()