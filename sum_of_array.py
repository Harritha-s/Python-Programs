# Got input(sum) from the user then add array's in a continuous order to get the sum value

array = []
n = int(input())
sum = int(input())
for i in range(n):
    a = int(input())
    array.append(a)
for i in range(len(array)-1):
    for j in range(i+1,n-1):
        if(array[i] + array[j] == sum):
            print(i,j)
        else:
            total = array[i]+array[j]
            for j in range(i+1,n-1):
                total += array[j+1]
                if(total == sum):
                    print(i,j+1)
""" Output:
5 - n
17 -sum
1   - array's
2
3
7
5
1 4 - Optput
"""
            
       