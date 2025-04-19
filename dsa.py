#Weird Algo
#Consider an algorithm that takes as input a positive integer n. If n is even, the algorithm divides it by two, and if n is odd, the algorithm multiplies it by three and adds one. The algorithm repeats this, until n is one. For example, the sequence for n=3 is as follows:
# 3 10 5 16 8 4  2 1


def main():
    N = 3
    while N != 1:
        print(N, end = " ")
        if N%2 !=0:
            N = 3*N +1
        else:
            N = N/2
    print(1)

if __name__ == "__main__":
    main()

