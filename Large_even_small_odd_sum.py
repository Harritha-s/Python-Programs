num = list(map(int,input().split()))
even = []
odd = []
for i in range(len(num)):
    if(num[i] % 2 == 0):
        even.append(num[i])
    else:
        odd.append(num[i])
even.sort()
even.reverse()
odd.sort()
even_count = 0
odd_count = 0
sum_even = 0
sum_odd = 0
while(even_count < 3):
    sum_even += even[even_count]
    even_count += 1
        
while(odd_count < 3):
    sum_odd += odd[odd_count]
    odd_count += 1  
print(sum_even)
print(sum_odd)


