#generate pyth triples
#find perimeter for each triple
#find duplicates
import math
import itertools
array = []

for a in range(1,500):
	for b in range(1,500):
		c = math.sqrt(a**2 + b**2)
		p = a + b + math.sqrt(a**2 + b **2)
		if c % 1 == 0 and p < 1000:
			array.append(p)

def most_common(list):				#taken from Stackoverflow
	return max(set(list), key=list.count)	#taken from Staveoverflow

print most_common(array)