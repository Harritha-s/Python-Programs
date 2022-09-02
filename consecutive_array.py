consecutive = []
count = 0
array = list(map(int,input().strip().split()))
array.sort()
for i in range(len(array)-1):
    if(array[i]+1 in array):
       consecutive.append(array[i]+1)
       count += 1
       if(array[i] not in consecutive):
            consecutive.append(array[i])
            count += 1
       
consecutive.sort()   
print(consecutive)
print(count)