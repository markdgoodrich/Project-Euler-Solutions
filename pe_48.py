#Project Euler 48
import math

x=range(1,1001)

sum = 0
for y in x:
    y=y**y
    sum = y + sum
    #print sum % 10000000000
print sum % 10000000000
