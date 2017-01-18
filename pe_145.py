#Project Euler 145

def rev_check(n):
    if n % 10 == 0:
        return False
    n = n + int(str(n)[::-1])
    if all(int(digit) % 2 == 1 for digit in str(n)):
        return True

counter = 0
for n in range(10**9):
    if rev_check(n):
        counter += 1


print counter



#608720
