#Project Euler 36
import math

q = range(1,1000000)
pals = []

for x in q:
    b="{0:b}".format(x)
    #print x , b
    if str(x) == str(x)[::-1] and str(b) == str(b)[::-1]:
        pals.append(x)

print sum(pals)
