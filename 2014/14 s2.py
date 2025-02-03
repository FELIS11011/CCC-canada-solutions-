n = int (input ())
line1 = input ()
line2 = input ()

good = True

name1 = line1.split(" ")
name2 = line2.split(" ")

for i in range (n) :
    if name1 [i] != name2 [name1.index(name2[i])] or name1 [i] == name2 [i] :
        good = False

if good == False :
    print ("bad")
else:
    print ("good")

