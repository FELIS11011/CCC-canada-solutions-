n = int (input ())

a = [1 , 2 , 3 , 6 , 7 , 11]

b = n // 20 

c = n // 4 

d = 5 * (c - b)

if n in a :
    print (0)
elif n <= d :
    print (b + 1)
else: 
    print (b)



