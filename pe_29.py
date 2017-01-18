#Project Euler Problem #29 potentinal
import math

#r=range(2,6)
#list = []
#list=[2,3,4,2]
#for i in range (0,4):
#    for j in range (0,4):
#        if list[i] == list[j]:
#            list.remove(j)
#print list
#
#for a in r:
#    for b in r:
#        #print "%s^%s = %s" %(a,b,a**b)
#        list.append(a**b)
#        if list[i]==list[j]:
#            list.remove(i)
#
#print list

#Euler Problem #29 potential  THIS ONE WORKS

#generate numbers of powers
#put them into a list
#check to see if there are any duplicates in the list
#remove those duplicates
#find the number of elements in the list
#
nums = []
r = range(2, 101)							#change to (2,101) after testing
for a in r:
    for b in r:
        pow=a**b
        nums.append(pow)
print len(set(nums))  #'set' prints only unique elemtns in the set!
