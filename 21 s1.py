n = int (input ())

area = float (0)

heights = list (map (int , input ().split (" ")))
widths = list (map (int , input ().split (" ")))

for i in range (n) :
    area += ((heights [i] + heights [i+1]) * widths [i]) / 2


print (area)