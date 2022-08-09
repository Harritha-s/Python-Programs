a = list(map(int,input().strip().split()))
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if(a[i]>a[j]):
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
print(a)            