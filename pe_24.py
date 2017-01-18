#Project Euler #24
import itertools

print list(itertools.permutations('0123',2))
print list(itertools.permutations('0123',2))[2]
print list(itertools.permutations('0123456789',10))[10**6-1]
