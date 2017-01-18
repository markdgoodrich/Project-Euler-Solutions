#Project Euler 55
import math

lychrel = []

for b in range(10**2, 10**4+1):
    iterations = 0
    a = b
    while a != int(str(a)[::-1]) and iterations <50:
        a += int(str(a)[::-1])
        iterations += 1
        if iterations == 49:
            lychrel.append(b)
            #a == int(str(a)[::-1])

print len(set(lychrel)) + 3         #There are 3 palindromic Lychrel numbers between 1 and 10000
#print lychrel

#Missing the palindrome lychrel numbers (4994)


