num = list(map(int,input().strip().split()))
odd = []
even = []
for i in range(len(num)-1):
    if(num[i] % 2 == 0):
        even.append(num[i])
    else:
        odd.append(num[i])
print("The even numbers of array: ",even)
print("The odd numbers of array: ",odd)
