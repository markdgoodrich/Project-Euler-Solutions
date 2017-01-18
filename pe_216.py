import math

def is_prime(n):
	if any( n % i == 0 for i in range(2,int(math.sqrt(n)+1))):
		return False
	else:
		return True
counter = 0
for n in range(2,50000000):
	n = float(2*n**2 -1)
	if is_prime(n):
		counter += 1

print counter