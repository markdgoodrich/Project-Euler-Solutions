import math

#Creates arrays of prime numbers

p = [True] * (10 ** 6)			#edit number here i suppose
p[0] = False
p[1] = False

for i in range(2, len(p)):
	if p[i]:
		j = i**2
		while j < len(p):
			p[j] = False
			j += i


primes = []
for n in range(len(p)):
	if p[n]:
		primes.append(n)
#now we have array of primes


len = 0
sum = 0
for p in primes:
	sum += p
	len += 1
	if sum in primes:
		print "%d is prime with length %d" %(sum,len)
