"""
*
**
***
****
*****
****
***
**
*
"""

#Method-1

# n =5
# for i in range(0,5):
#     for j in range(i+1):
#         print('*', end='')
#     print()

# for k in range(0,n-1):
#     for m in range(n-k-1):
#         print('*', end='')
#     print()


#Method-2 - optimum soln 

# n=5
# #upper Triangle
# for i in range(0,n):
#     print('*' * i)

# #Lower triangle
# for i in range(n-1,0, -1):
#     print('*' * i)
    

#Method-3
n = 5
rows = 2 * n - 1  # total rows: 9 for n=5

for i in range(1, rows + 1):
    if i <= n:
        # upper part
        print('*' * i)
    else:
        # lower part
        print('*' * (2 * n - i))