import random

result = []
index = []
user_array = []
array = list(map(int,input().strip().split()))
n = int(input())
for i in range(n):                  #getting random elements from user and storing in a user_array list
    a = int(input())
    user_array.append(a)
print(user_array)
for j in range(len(array)):         #comparing array and user_array storing index in a index list
    for k in range(len(user_array)):
        if(array[j] == user_array[k]):
            index.append(j)
         
index.sort()
#print(index)
for l in range(len(index)):
    a = index[l]
    result.append(array[a])
    
print(result)
