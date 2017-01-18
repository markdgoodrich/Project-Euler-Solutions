  #Euler Problem #25
import math
#Generate Fibonacci numbers
#count the index
#look at the length of each Fibonacci number
#print when len(fib)=1000

f_one = 1
f_two = 1
index = 2
fib = 0

while fib <= 10**1000: 			#change to 10**999 after testing
    fib = f_one + f_two
    f_two = f_one
    f_one = fib
    
    index += 1
    digits = len(str(fib))
    #print fib, index, digits
        
    if digits >= 1000: 		#change to 1000 after testing
            print index
