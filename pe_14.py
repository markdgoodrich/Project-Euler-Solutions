 import math
print "------------Project Euler Problem #14-----------------"

def collatz(num, count):
    if num == 1:
        return count

    elif num % 2 == 0:
        num = num / 2
        count += 1
        return collatz(num, count)
        
    else:
        num = (3 * num) + 1
        count += 1
        return collatz(num, count)

def allnums():
    x = range(1,999999)
    counts = []
    
    for n in x:
        ct = collatz(n, 0)
        counts.append(ct)

    print counts.index(max(counts)) + 1
