#Project Euler 43
import itertools


pandigital_permuts = [''.join(p) for p in itertools.permutations('1234567890')]

#print "The amount on permutations of the pandigital number is: %s" %len(list(pandigital_permuts))


#x = 1406357289
#
#a = str(x)
#
#print int(a[1:4]), int(a[2:5]), int(a[3:6]), int(a[4:7]), int(a[5:8]), int(a[6:9]), int(a[7:10])
#

sum = 0

for x in pandigital_permuts:
    if int(x[1:4]) % 2 ==0 and int(x[2:5]) % 3 == 0 and int(x[3:6]) % 5 == 0 and int(x[4:7]) % 7 == 0 and int(x[5:8]) % 11 == 0 and int(x[6:9]) % 13 == 0 and int(x[7:10]) % 17 == 0:
            print x
            sum += int(x)

print sum
