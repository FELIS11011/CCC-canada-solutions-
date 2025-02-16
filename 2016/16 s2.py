q = int (input ())
n = int (input ())

city1 = []
city2 = []

city1 = input().split ()
city2 = input ().split ()

cities = city1 + city2

cities = [int (x) for x in cities]

cities.sort ()

midpoint = len(cities)//2



if q == 1:
    print (sum (cities [: midpoint ]))
if q == 2:
    print (sum (cities [1::2]))
