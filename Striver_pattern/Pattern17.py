# n = 4
# for i in range(0,n):
#     ch = chr(ord('A')+j)
#     #spaces
#     for j in range(n-i-1):
#         print(' ', end='') 
#     #letters
#     for k in range(2 * i + 1):
#         print(ch, end='')
#     print()


"""
   A
  ABA
 ABCBA
ABCDCBA

"""
n = 4
for i in range(0,n):
    #spaces
    for j in range(n-i-1):
        print(' ', end='') 

    #letters
    ch = chr(ord('A'))
    breakpoint = (2*i+1)//2

    for k in range(2 * i + 1):
        print(ch, end='')
        if k < breakpoint:
            ch = chr(ord(ch) + 1)  # move forward in alphabet
        else:
            ch = chr(ord(ch) - 1) 
    print()