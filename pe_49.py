import math
import itertools
#generate primes to 10000
#have prime number between 1000,3339
#add 3330 and 6660
#check if they are prime
#permute original 


p = [True] * 10 ** 4			#edit number here i suppose
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

for i in primes:
	if i > 1000 and i < 10000:
		t_i = i + 3330
		s_i = i + 6660
		if t_i in primes and s_i in primes:
			a = list(map("".join, itertools.permutations(str(i))))
			if str(t_i) in a and str(s_i) in a:
				print i, t_i, s_i
			