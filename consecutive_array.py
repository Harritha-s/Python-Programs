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

""" Output:
    18 1 4 3 2
    [1, 2, 3, 4]
    4
    
    22 15 19 20 16 18 17
    [15, 16, 17, 18, 19, 20]
    6
"""    
