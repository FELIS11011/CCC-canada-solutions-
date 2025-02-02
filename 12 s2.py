aromatic = "2I3I2X9V1X"

digits = []
sum = 0


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

print (digits)
first = digits [0::2]
second = digits [1::2]



for i in range (len(first)) :
    product = 
   
print (sum)
