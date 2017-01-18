import math
def is_prime(n):
	if any( n % i == 0 for i in range(2,int(math.sqrt(n)+1))):
		return False
	else:
		return True

counter = 1 				#including '2' already
i=3

while counter < 10001:
	if is_prime(i) is True:
		#print i		#testing purposes	
		counter += 1
		i += 2			#only testing odd numbers
		
	else:
		i += 2			#only testing odd numbers

print i-2, counter