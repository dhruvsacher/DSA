n = 5
for i in range(0,n):
    #star
    for j in  range(n-i):
        print('*', end='')
    
    #space
    for space in range(i*2):
        print(' ', end='')
    
    #star
    for k in  range(n-i):
        print('*', end='')
    print()

for i in range(1,n+1):
    #star
    for j in  range(i):
        print('*', end='')
    
    #space
    for space in range(2*n-2*i):
        print(' ', end='')
    
    #star
    for k in  range(i):
        print('*', end='')
    print()
