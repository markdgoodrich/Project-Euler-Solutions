#38 notes

#Find pandigital numbers
#perhaps in some combination fashion
	#split into three parts
	#NOPE!!! Can be many different parts	
#check divisibility of each part
# ^ Terrible ideas


import math
import itertools

a = list(map("".join,itertools.permutations('987654321')))

# Must be larger than 918273645, which is 9 (1,2,3,4,5)
# == str(9*1)+str(9*2)+str(9*3)+str(9*4)+str(9*5)

#start with a number 1,2,3,4,5,...193...,n
#have max = 0, for maximum number
#have incrementor t = 1 --> ACTUALLY t = 2


max = 0

for n in range(1,10000):
	t = 2
	m = str(n)
	while len(m) < 9:
		m += str(n*t)
		t += 1		
	
	if len(m) == 9:
		if m in a and int(m) > max:		#a being the list of permutations
			max = int(m)
			#print n			# n = 9327 for final answer
print max



#Regards Python:
#Learned an important lesson here. Ranges are much faster than while loops and additions.
#Also switching from n**2 to n*n gives about 30% better result (9.7 to 6 seconds) - NUTS.