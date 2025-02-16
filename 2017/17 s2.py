n = int (input ())
tides = input ().split ()

final = []
tides = [int(x) for x in tides]
tides.sort ()
odd = False

if len(tides) % 2 == 1 :
    first = tides [0]
    tides.pop (0)
    odd = True 


lows = tides [ : len(tides)//2 ]
highs = tides [len(tides)//2 : ]

lows.sort (reverse = True)

for i in range (len(lows)) :
    final.append (lows [i])
    final.append (highs [i])

if odd == True :
    final.append (first)

string = " ".join (map(str , final))

print (string)