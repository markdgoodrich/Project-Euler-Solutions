import random
import time

start = time.time()
rounds = 0
counter = 0
while rounds < 10**8:

	p_1 = random.randint(1,4)
	p_2 = random.randint(1,4)
	p_3 = random.randint(1,4)
	p_4 = random.randint(1,4)
	p_5 = random.randint(1,4)
	p_6 = random.randint(1,4)
	p_7 = random.randint(1,4)
	p_8 = random.randint(1,4)
	p_9 = random.randint(1,4)

	p_score = p_1 + p_2 + p_3 + p_4 + p_5 + p_6 + p_7 + p_8 + p_9


	c_1 = random.randint(1,6)
	c_2 = random.randint(1,6)
	c_3 = random.randint(1,6)
	c_4 = random.randint(1,6)
	c_5 = random.randint(1,6)
	c_6 = random.randint(1,6)

	c_score = c_1 + c_2 + c_3 +c_4 + c_5 + c_6
	
	rounds += 1
	#print p_score, c_score
	
	if p_score > c_score:
		counter += 1


end = time.time()
print (float(counter)/float(rounds)), (end-start)

#this gives an estimate at best.
#takes 3 minutes to run 10**7 rounds
#let's do some combinatorics

#for 10**8:
#0.57314466 in 1817.782 seconds
