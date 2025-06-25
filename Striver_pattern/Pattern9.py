""" Diamond Pattern
   *
  ***
 *****
*******
*******
 *****
  ***
   *

"""

n = 4
for i in range(0,n):
    #spaces
    for j in  range(n -i -1):
        print(' ', end='')
    #stars
    for k in range(2*i +1):
        print('*', end='')
    print()


for l in range(0,n):
    #spaces
    for m in range(l):
        print(' ', end='')
    for star in range(2*n -(2*l+1)):
        print('*', end='')
    print()