#Project Euler problem #30 potential

#generate numbers
#break numbers into digits
#check to see if the sum of the fifth power of their digits is equal to the number
#store that number
#add all numbers that fit that description

#x = 1634
num =0
this_list = []
for x in range(2,10**6):
    num = sum(int(digit)**5 for digit in str(x))
    if num == x:
        #print num
        this_list.append(num)
    else:
        num ==0

print sum(this_list)
