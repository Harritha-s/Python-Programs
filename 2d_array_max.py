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