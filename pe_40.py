#Project Euler problem #40
list_num = range(1,10**6+1)

num =(''.join(map(str,list_num)))

#print int(num)
print num[12]
print num[0], num[9], num[99], num[999], num[9999], num[99999]
champ = int(num[0]) * int(num[9]) * int(num[99]) * int(num[999]) * int(num[9999]) * int(num[99999]) * int(num[999999])

print champ
