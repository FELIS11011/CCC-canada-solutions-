ori = list (input ())

h = int()
v = int ()

for i in range (len(ori)) :
    if ori[i] == "H" :
        h = h + 1
    elif ori [i] == "V" :
        v = v + 1
    
h1 = h % 2
v1 = v % 2

if v1 == 1 and h1 == 1 :
    print (4 , 3)
    print (2 , 1)
elif v1 == 1 and h1 == 0 :
    print (2 , 1)
    print (4 , 3)
elif v1 == 0 and h1 == 1 :
    print (3 , 4)
    print (1 , 2)
elif v1 == 0 and h1 == 0 :
    print (1 , 2)
    print (3 , 4)

    

