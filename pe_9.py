import math
#Project Euler Problem #9

x = range(1,1000)
    
for a in x:
    for b in x:
        c = (a**2+b**2)**(0.5)
        if a+b+c == 1000:
            #print a , b , c
            prod = a*b*c
            print prod
