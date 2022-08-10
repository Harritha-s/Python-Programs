#Find the random of 3 elements in a array and sort them according to first array

import random

result = []
index = []
random_array = []
array = list(map(int,input().strip().split()))
for i in range(3):
    r_value = random.choice(array) #finding random elements in array
    random_array.append(r_value)
print(random_array)
for j in range(len(array)):
    for k in range(len(random_array)):
        if(array[j] == random_array[k]):
            index.append(j)
         
index.sort()
#print(index)

for l in range(len(index)):
    a = index[l]
    result.append(array[a])
    
print(result)
