#15/15 dmoj
q = int (input ())
n = int (input ())

city1 = []
city2 = []
mini = 0 

city1 = input ().split ()
city2 = input ().split ()

cities = city1 + city2

cities = [int (x) for x in cities]

cities.sort ()

city1 = [int (x) for x in city1]
city2 = [int (x) for x in city2]
city1.sort ()
city2.sort ()

midpoint = len(cities)//2





if q == 2:
    print (sum (cities [ midpoint : ]))
if q == 1:
    for i in range (len(city1)):
        mini += max (city1 [i] , city2 [i])
    print (mini)
