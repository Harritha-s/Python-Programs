intersection = []
array1 = list(map(int,input().strip().split()))
array2 = list(map(int,input().strip().split()))
for i in range(len(array1)):
    if(array1[i] in array2):
        intersection.append(array1[i])
print(intersection)
