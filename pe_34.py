#Project Euler 34
import math

digit_factorials=[]

for n in range(1,10**6):
    the_sum = 0
    for x in str(n):
        the_sum = the_sum + math.factorial(int(x))
    if the_sum == n:
            digit_factorials.append(n)
#print n, the_sum

print sum(digit_factorials)-3
