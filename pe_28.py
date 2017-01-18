#Project Euler 28
diagonal = []

for x in range(3,1003,2):
    tr = x**2
    diff = x-1
    a = tr - diff
    b = tr - 2*diff
    c = tr-3*diff
    diagonal.append(tr)
    diagonal.append(a)
    diagonal.append(b)
    diagonal.append(c)


print sum(diagonal)+1
