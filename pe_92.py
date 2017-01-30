#Project Euler 92

counter = 0
def test(x):
    if x == 89:
        #    counter += 1
        return x
    elif x ==1:
        return x
    else:
         return test(sum(int(digits)**2 for digits in str(x)))

#print test(78)
#print test(44)
#print test(99)

for a in range(1,10**7):
    if test(a) == 89:
        counter += 1


print counter
