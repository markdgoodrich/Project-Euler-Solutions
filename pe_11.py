import math

for x in range(0,10):
	for y in range(1,10):
		for z in range(0,10):
			if (x + y + z) % 10 == z:
				print x,y,z
