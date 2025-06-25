"""
1
01
101
0101
10101
"""

n =5 
start = 1
for i in range(0,n):
    if i%2==0:
        start =1
    else:
        start =0

    for j in range(0,i+1):
        print(start, end='')
        start = 1 - start
    print()













    # for j in range(i+1):
    #     if j % 2 ==0:
    #         print('1', end='')
    #     else:
    #         print('0', end='')
    # print()