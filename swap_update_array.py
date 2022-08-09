array = [12,23,5,49,20,12]
n = list(map(int,input().strip().split()))

for i in range(len(n)):
    for j in range(len(array)):     #updating index element as 0
        if(n[i] == j):
            array[j] = 0
print(array)        

for i in range(len(array)):
    for j in range(i+1,len(array)): #swapping 0 elements to last element
        if(array[i] == 0):
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
print(array)

