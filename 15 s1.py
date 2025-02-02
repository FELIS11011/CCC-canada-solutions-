k = int (input ())
current = []
for i in range (k) :
    statement = int (input ())
    if statement != 0 :
        current.append (statement)
    else:
        del current [-1]

print (sum (current))
        
