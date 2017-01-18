import math


def div(n):
	counter = 1			 
	for i in range(2,int(math.sqrt(n))):
		if n % i == 0:
			counter += 1
	return 2*counter

i = 0
j = 1
while div(i) < 500:
	i += j
	j += 1


print i