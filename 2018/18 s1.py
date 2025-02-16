n = int (input ())

v1 = []
s1 = []


for i in range (n) :
    v = float (input ())
    v1.append (v)

v2 = sorted (v1)

for j in range (n - 2) :
    s = (v2 [j + 2]) / 2 - (v2 [j]) / 2 
    s1.append (s)

s2 = sorted (s1)

print (s2 [0])
    



