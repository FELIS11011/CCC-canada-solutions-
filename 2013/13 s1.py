year = int (input ())
distinct = False
while distinct == False :
    year = year +1 
    l = list(str(year))
    s = set(l)
    if len(l) == len(s) :
        distinct = True
        print (year)
