def check (num) :
    if num == 0 or num == 1 or num == 2 :
        return False 
    for i in range (2 , int (num ** 0.5 + 1)) :
        if num % i == 0 :
            return False 
    return True 

t = int (input ())

for i in range (t) :
    n = int (input ())
    a = n 
    b = n 
    while True :
        if check (a) and check (b) :
            print (a , b)
            break 
        a -= 1
        b += 1