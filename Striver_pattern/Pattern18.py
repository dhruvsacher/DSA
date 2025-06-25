# n = 6
# for i in range(1,n):
#     ch = chr(ord('E'))
    
#     for j in range(1,i+1):
#         print(ch, end='')
#         ch = chr(ord('E') - j)
#     print()


"""
E
DE
CDE
BCDE
ABCDE

"""
n = 5
for i in range(0,n):
    
    # for ch in range(chr(ord('E')-1), chr(ord('E')+1)):
    for ch in range(ord('E') - i, ord('E') + 1):
        print(chr(ch), end='')
    print()
    