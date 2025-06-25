"""
A
BB
CCC
DDDD
EEEEE

"""

n = 5

for i in range(0,n):
    ch = chr(ord('A')+ i)
    for j in range(0,i+1):
        print(chr(ord(ch)), end='')
        
    print()