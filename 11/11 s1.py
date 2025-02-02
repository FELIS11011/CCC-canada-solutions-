n = int (input())
text = ''

for i in range (n) :
    line = input ()
    text = text + line 

t = text.count("t") + text. count("T")
s = text.count("s") + text. count("S")


if t > s:
    print ("English")
else: 
    print ("French")

