# not full marks 

line1 = input ()
line2 = input ()
line1a = list (line1)
line2a = list (line2)
count = 0

if "*" in line2a :
    for i in range (len(line2a)) :
        if line2a [i] in line1a :
            count = count + 1
            line1a.remove (str(line2a[i]))
        
        
        
    if count == len (line2a) - line2a.count("*") and len (line2a) == len (line1a) :
        print ("A")
    else:
        print ("N")
else : 
    print ("N")
