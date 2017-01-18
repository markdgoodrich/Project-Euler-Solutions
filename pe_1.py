## project euler # 1

def findsum():
    x = range(1,1000)
    mults = []
    for n in x:
        if n % 3 == 0:
            mults.append(n)
        elif n % 5 == 0:
            mults.append(n)
    print sum(mults)
