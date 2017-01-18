#27

#b must be prime
#try 2nd formula when n= 80 to see if a type of divisibility pattern emerges
#80^2 - 79*80 + 1601 = 1681 
#1681 = 41^2
#hm....


#1681^2 = 2825761
import math

def is_prime(n):
	if any( n % i == 0 for i in range(2,int(math.sqrt(n)+1))):
		return False
	else:
		return True
counter = 0

def quad(n):
	return (n-31)**2 + (n-31) + 41

for n in range(31):
	if is_prime(quad(n)):
		counter += 1 
	print "%d is prime. n = %d" %(quad(n),n)

print counter

#if p(x) is prime generating for 0 < x <n then so is p(n-x)
#p(n-9)=p(31) = n^2 - 61 - 971
#971*61