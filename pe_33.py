#a/b
#b > a
#len(str(a)) and len(str(b)) == 2
#range(10,100)
#first digit both, first digit num sec denom, second num fist denom, both second

#c = flaot(a)/float(b)
#if float(string(a)[0])/float(string(b)[0] == c:
#	print a,b
#elif float(string(a)[0])/float(string(b)[1] == c:
#	print a,b
#elif float(string(a)[1])/float(string(b)[0] == c:
#	print a,b 
#elif float(string(a)[1])/float(string(b)[1] == c:
#	print a,b





import math

ma = 1
mb = 1

for a in range(10,100):
	for b in range(10,100):
		if b > a and (str(b)[1] != '0' and str(a)[1] != '0'):

			c = float(a)/float(b)

			if float(str(a)[0])/float(str(b)[0]) == c and float(str(a)[1])==float(str(b)[1]):
				print a,b
				ma *= a
				mb *= b
			elif float(str(a)[0])/float(str(b)[1]) == c and float(str(a)[1])==float(str(b)[0]):
				print a,b
				ma *= a
				mb *= b
			elif float(str(a)[1])/float(str(b)[0]) == c and float(str(a)[0])==float(str(b)[1]):
				print a,b 
				ma *= a
				mb *= b
			elif float(str(a)[1])/float(str(b)[1]) == c and float(str(a)[0])==float(str(b)[0]):
				print a,b
				ma *= a
				mb *= b
			else:
				continue

#16/64, 19/95, 26/65, 49/98
print ma, mb
print float(ma)/float(mb)