j = int (input ())
a = int (input ())

sizes = []
statisfy = 0
used = [False] * j


for i in range (j) :
    sizes.append (input ())

for i in range (a) :
    size = ""
    number = 0 
    size , number = input ().split ()
    number = int (number) - 1
    if used [number] == False and number < j  :
        if size == "L" and sizes [number] == "L":
            statisfy += 1 
            used [number] = True 
        elif size == "M" and (sizes [number] == "L" or sizes [number] == "M"):
            statisfy += 1 
            used [number] = True
        elif size == "S" and (sizes [number] == "M" or sizes [number] == "L" or sizes [number] == "S"):
            statisfy += 1 
            used [number] = True

print (statisfy)
