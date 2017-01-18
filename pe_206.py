#1_2_3_4_5_6_7_8_9_0
#1_2_3_4_5_6_7_8_900 = n**2
# n ends with a 0
#that leaves 16 digits in n**2
#or only 8 digits in n
# n can be, at max, 138902663

#-----------------------------------------------------------

for x in xrange(10**8, 138902663):
	sx = str(x**2)
	if sx[0] == '1' and sx[2] == '2' and sx[4] == '3' and sx[6] == '4' and sx[8] == '5' and sx[10] == '6' and sx[12] == '7' and sx[14] == '8' and sx[16] == '9':
		print x, sx, str(x) + '0'
