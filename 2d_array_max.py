array = []
count = []
n = int(input())
for row in range(n):
    column = list(map(int,input().strip().split()))
    array.append(column)

for i in range(n):
    count1 = 0
    for j in range(n):
        if(array[i][j] == 1):
            count1 += 1
    count.append(count1)
print(count)
a = max(count)
print(count.index(a)+1)


""" output:
    4
    1 0 0 0
    1 1 0 1
    1 0 1 0
    0 1 0 0
    [1, 3, 2, 1]        #count
    2
    
    5
    1 0 1 1 1
    0 1 0 1 0
    0 1 1 1 1
    0 1 0 0 1
    1 1 1 1 1
    [4, 2, 4, 2, 5]     #count
    5
"""    
