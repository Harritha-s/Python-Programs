intersection = []
union = []
array1 = list(map(int,input().strip().split()))
array2 = list(map(int,input().strip().split()))
for i in range(len(array1)):
    if(array1[i] in array2):
        intersection.append(array1[i])
print("Intersection of array: ",intersection)
for i in range(len(array1)):
    if(array1[i] in array2 or array1[i] not in array2):
        union.append(array1[i])
for j in range(len(array2)):
    if(array2[j] not in array1):
        union.append(array2[j])
print("Union of array: ",union)
