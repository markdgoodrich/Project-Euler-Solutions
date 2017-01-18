#Project Euler 56
import math

r = range(1,100)
dsums = []
for a in r:
    for b in r:
        n=a**b
        m=sum(int(digit) for digit in str(n))
        dsums.append(m)
print max(dsums)
