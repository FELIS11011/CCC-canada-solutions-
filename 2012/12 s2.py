aromatic = input ()

digits = []
sums = []

for digit in aromatic : 
    if type (digit) == str :
        if digit == "I" :
            digits.append (1)
        elif digit == "V" :
            digits.append (5)
        elif digit == "X" :
            digits.append (10)
        elif digit == "L" :
            digits.append (50)
        elif digit == "C" :
            digits.append (100)
        elif digit == "D" :
            digits.append (500)
        elif digit == "M" :
            digits.append (1000)
        else :
            digits.append (int(digit))


first = digits [0::2]
second = digits [1::2]

n = len (first)

for i in range (n - 1) :
    if second [i + 1] > second [i] :
        sums. append (-first [i] * second [i])
    else :
        sums. append (first [i] * second [i])

sums.append (first [-1] * second [-1])

print (sum (sums))



