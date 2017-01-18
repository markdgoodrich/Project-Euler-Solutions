#Project Euler 17

single_digit = {0:0,1:3, 2:3, 3:5, 4: 4, 5:4, 6:3, 7:5, 8:5, 9:4}
double_digit = {0:0, 2:6, 3:6, 4:5, 5:5, 6:5, 7:7, 8:6, 9:6}
teen = {10:3, 11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8}



def letter_count(n):
    if len(str(n)) == 3 and int(str(n)[1:]) in range(10, 20):
        return single_digit[n/100] + 7 + teen[int(str(n)[1:])] + 3          #+3 for "and"
    elif len(str(n))== 3:
        return single_digit[n/100] + 7 + double_digit[int(str(n)[1])] + single_digit[n%10] + 3          #+3 for "and"
    elif len(str(n)) == 2 and int(str(n)[0]) == 1:
        return teen[int(str(n))]
    elif len(str(n)) == 2:
        return double_digit[int(str(n)[0])] + single_digit[n%10]
    elif len(str(n)) == 1:
        return single_digit[n]


print letter_count(300), letter_count(115), letter_count(342)

total = 11          #one thousand is 11 letters

for i in range(1,1000):
    total += letter_count(i)

print total - 3*9   #3*9  to remove "_ hundred and" for those ending in "00"

