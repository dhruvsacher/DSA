"""
ABCDE
ABCD
ABC
AB
A
"""
n = 5
for i in range(0,n):
    for j in range(0, n-i):
        print(chr(ord('A') + j), end='')
    print()