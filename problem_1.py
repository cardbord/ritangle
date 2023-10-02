def main():
     counter = 0
     for a in range(1,9):
          for b in range(1,9):
               for c in range(1,9):
                    for d in range(1,9):
                         for e in range(1,9):
                              for f in range(1,9):
                                   for g in range(1,9):
                                        for h in range(1,9):
                                             if not (a in [b,c,d,e,f,g,h] or b in [a,c,d,e,f,g,h] or c in [a,b,d,e,f,g,h] or d in [a,b,c,e,f,g,h] or e in [a,b,c,d,f,g,h] or f in [a,b,c,d,e,g,h] or g in [a,b,c,d,e,f,h] or h in [a,b,c,d,e,f,g]):

                                             
                                                  if a*b*c*d*e < f*g*h:
                                                       counter+=1
                                                       
                                                       print(f"number of times: {counter}")
                                                       print(a,b,c,d,e,f,g,h)
                                                       print(a*b*c*d*e)
                                                       print(f*g*h)
                                                       print('')
                                             
     print(counter)

#after running, counter hits 3600.
def test():
     for i in range(10):
          for x in range(10):
               if i in [x]:
                    print(f"these are the same: {i,x}")
          
main()