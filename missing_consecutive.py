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
    elif(array[i]+2 in array):
            consecutive.append(array[i]+2)
            if(array[i] not in consecutive):
                consecutive.append(array[i])
                count += 1
consecutive.sort()
print(consecutive)
for i in range(len(consecutive)):
    if(consecutive[i]+1 not in consecutive):
        print(consecutive[i]+1)
        break
        
    """ Output:
        1 3 5 4 6 9         i/p
        [1, 3, 4, 5, 6]     consecutive numbers
        2                   o/p

        1 2 3 4 5 9
        2                   o/p
    """
