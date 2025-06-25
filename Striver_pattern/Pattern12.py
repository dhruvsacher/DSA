"""
1      1
12    21
123  321
12344321
"""
n = 5

for i in range(1,n):
    for j in range(1,i+1):
        print(j, end='')
    
    for space in range(1, 2*(n-i-1)+1):
        print(' ', end='')

    for k in range(i,0,-1):
        print(k, end='')
    print()