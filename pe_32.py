import math
import itertools

#Test in terminal
#a = list(map("".join, itertools.permutations('987654321')))
#x = '39'
#y = '186'
#z = int(x) * int(y)
#(x + y + str(z)) in a #returns True!

# have array of permutations a
# have empty array. pan = []


pan = []
a = list(map("".join, itertools.permutations('987654321')))

for x in range(2,50):
	for y in range(2000, 2, -1):
		xs = str(x)
		ys = str(y)
		z = str(x*y)
		if xs + ys + z in a:
			pan.append(int(z))
			print z, y, x

print sum(set(pan))

#4*1963, 4*1738, 12*483, 18*297, 27*157, 28*157, 39*186, 42*138, 48*159

