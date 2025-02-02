n = int (input())

time = []
distance = []
speed = []


for i in range (n) :
    line = input ()
    line1 = list(map(int, line.split (" ")))
    time.append (line1 [0])
    distance.append (line1 [1])

times , distances = zip(*sorted (zip (time , distance)))

for x in range (n - 1) :
    speed.append (abs(distances [x + 1] - distances [x]) / abs(times [x+1] - times [x]))

speed.sort ()

print (speed [-1])
        






