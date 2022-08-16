def getMinMax( a, n):
    product = []
    a1 = max(a)
    b1 = min(a)
    return (b1,a1)

def main():
    T = int(input())
    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        product = getMinMax(a,n)
        print(product[0],end=" ")
        print(product[1])
        T -= 1
if __name__ == "__main__":
    main()