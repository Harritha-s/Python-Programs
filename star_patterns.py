n = 5
for i in range(n):
    for j in range (i,n):       #decreasing order
        print("*",end = ' ')
    print()
print()

for i in range(n):
    for j in range (i+1):       #incerasing order
        print("*",end = ' ')
    print()
print()

for i in range(n):
    for j in range(i,n-1):      #left triangle
        print(" ",end = ' ')
    for k in range(i+1):
        print("*",end = ' ')
    print()
print()

for i in range(n):
    for j in range(i+1):
        print(" ",end =' ')
    for k in range(i,n-1):
        print("*",end = ' ')
    for l in range(i,n):
        print("*",end = ' ')
    print()
print()


for i in range(n-1):
    for j in range(i,n):
        print(" ",end = ' ')
    for k in range(i):
        print("*",end = ' ')
    for l in range(i+1):
        print("*",end = ' ')
    print()
for m in range(n):
    for j in range(m+1):
        print(" ",end = ' ')
    for k in range(m,n-1):
        print("*",end = ' ')
    for l in range(m,n):
        print("*",end = ' ')
    print()
        