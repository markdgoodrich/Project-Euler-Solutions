#Project Euler 21
amicable = []

for x in range(1, 10000):
    potential_num = x
    divisors=[]
    for l in range(1,potential_num/2+1):
        if potential_num % l == 0:
            divisors.append(l)

#print sum(divisors)
#print divisors

    potential_num2 = sum(divisors)
    divisors=[]
    for k in range(1, potential_num2/2+1):
        if potential_num2 % k == 0:
            divisors.append(k)

    if sum(divisors) == potential_num:
        print potential_num, potential_num2
        amicable.append(potential_num)
        amicable.append(potential_num2)

print sum(amicable)/2-(6+28+496+8128)       #have to remove the perfect numbers
