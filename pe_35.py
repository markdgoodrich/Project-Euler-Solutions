#Project Euler 35

import math
import time

start = time.time()

def prime_sieve(n):
    primes = [True] * (n + 1)
    
    primes[0] = False
    primes[1] = False
    
    for i in range(2, int(math.floor(math.sqrt(n)+1))):
        if primes[i]:
            j = i * i
            while j < n + 1:
                primes[j] = False
                j += i
    
    result = []
    for i in range(len(primes)):
        if primes[i]:
            result.append(i)

    return result

primes = prime_sieve(10**6)

#def circular(n):                   #string
#    y = len(str(n))
#    while y > 1:
#        n = int(str(n)[1:] + str(n)[0])
#        if n in primes:
#            y -= 1
#        else:
#            return False
#    return True

def circular(n):            #mathematical
    y = len(str(n))
    holder = len(str(n))    #holds the initial values of the number of digits
    while y > 0:
        n = n % 10**(len(str(n))-1)*10 + n/10**(len(str(n))-1)         #Mathematical method
        if holder > len(str(n)):        #this removes any potential primes that have 0's
            return False
        elif n in primes:
            y -= 1
        else:
            return False
    return True

counter = 0
for n in primes:
    if circular(n) is True:
        counter += 1
        #print n
print counter

end = time.time()

print(end-start)
