import itertools
import math

#a = itertools.permutations(range(10))

a = list(map("".join, itertools.permutations('7654321')))

def is_prime(n):
	if any( n % i == 0 for i in range(2,int(math.sqrt(n)+1))):
		return False
	else:
		return True



for i in a:
	i = int(i)
	if is_prime(i) and i > 7652413:
		print i

#there are 362880 permutations of 123456789 (if i did it right)
#Current candidate: 7652413
