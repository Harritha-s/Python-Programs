import random

array = [1,2,3,4,5,6,7,8,9,10]
random_array =  []

for i in range(0,3):
    a = random.randint(array)
    random_array.append(a)

print(random_array)



