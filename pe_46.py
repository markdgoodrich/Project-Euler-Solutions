import math

def prime_sieve(n):
    
    primes = [True] * (n + 1)
    
    primes[0] = False
    primes[1] = False
    
    for i in range(2, n):
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

primes = prime_sieve(100000)





odds = [2*n+1 for n in range(2,5000)]



for n in odds:      # n is an odd number
    if n not in primes:     #n is an odd composite number
        if not any(n-2*i**2 in primes for i in range(1, int(math.floor(math.sqrt((n-2)/2)))+1)):
            print n

