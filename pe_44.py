#Project Euler problem #44 
import math
#generate pentagonal numbers
#order them somehow
#subtract pentagonal numbers from each other
#check to see if subtractions are pentagonal
#add pentagonal numbers to each other
#check to see if additions are pentagonal
# if additions and subtractions are pentagonal, then add D =|P_k - P_j| to a list
#find the minimum D

p = []
distance = []
for n in range(1,5000):
    pentagonal = (n*(3*n-1))/2
    p.append(pentagonal)
#print pentagonal

for a in p:
    for b in p[:-1]:
        subtract = a -b
        add = a + b
        if add in p and subtract in p:
            d= abs(a - b)
            distance.append(d)

print distance, a, b
