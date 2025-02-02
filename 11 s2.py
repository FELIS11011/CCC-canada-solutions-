n = int (input ())

student = []
correct = []
c = 0 

for i in range (n) :
    student.append (input ())

for j in range (n) :
    correct. append (input ())

for k in range (n) :
    if student [k] == correct [k] :
        c += 1

print (c)