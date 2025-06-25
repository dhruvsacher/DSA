"""
A
AB
ABC
ABCD
ABCDE

"""

n = 6
for i in range(1,n):
    for j in range(1,i+1):
        print(chr(ord('A') + j-1), end='')
    print()