n = int (input ())
n1 = input ()
n2  = input ()

sum1 = 0 
sum2 = 0
days = []

swift = n1.split (" ")
sema = n2.split (" ")

for i in range (n): 
    sum1 = sum1 + int(swift [i])
    sum2 = sum2 + int(sema [i])
    if sum1 == sum2 :
        days.append (i+1)


if len (days) == 0:
    print (0)
else:
    print (days[-1])




