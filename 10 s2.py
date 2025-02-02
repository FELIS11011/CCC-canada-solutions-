n = int (input ())

current = ""
codes = {}
decode = ""

for i in range (n) :
    char , code = input ().split (" ")
    codes [code] = char

sequence = input ()

for bits in sequence :
    current += bits 
    if current in code :
        decode += codes [current]
        current = ""

print (decode)

