array1 = []
array2 = []
union = []
n1 = int(input())
n2 = int(input())

for i in range(n1):           #creating arrays
    a = int(input())
    array1.append(a)
print(array1)
for i in range(n2):
    b = int(input())
    array2.append(b)
print(array2)
for i in range(n1):           #logic
    if(array1[i] in array2 or array1[i] not in array2):
        union.append(array1[i])
for j in range(n2):
    if(array2[j] not in array1):
        union.append(array2[j])
print(union)
print(len(union))
