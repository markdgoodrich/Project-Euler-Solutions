#Euler Problem #45
import math
#Generate Triangle numbers
#Generate Pentagonal numbers
#Generate hexagonal numbers
#must compare all three.
#when T=P=H, print

r = range(1,5000000)
t=[]
p=[]
h=[]
for n in r:
    triangle = n*(n+1)/2
    t.append(triangle)
        
    pentagonal = n*(3*n-1)/2
    p.append(pentagonal)
    
    hexagonal = n*(2*n-1)
    h.append(hexagonal)
intersection = set(t) & set(p) & set(h)
print intersection
