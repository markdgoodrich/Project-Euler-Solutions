#Project Euler 63
counter = 0
for x in range(1,10**4):
    for n in range(1,100):
        num = x **n
        if len(str(num)) == n:
            counter +=1
            #print num, x, n

print counter
