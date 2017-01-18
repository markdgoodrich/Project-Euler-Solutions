#Project Euler 52
import itertools

permuts = [''.join(p) for p in itertools.permutations('123')]
print permuts
print str(132) in permuts


c = 60
print str(2*c)

for x in range(10**6):
    perms = [''.join(p) for p in itertools.permutations(str(x))]
    if (str(2*x)) in perms and str(3*x) in perms and str(4*x) in perms and str(5*x) in perms and str(x*6) in perms:
        print x, 2*x, 3*x, 4*x, 5*x, 6*x
    else:
        perms = []

