a = [ ]
x = input("Enter he total number of elements to be sorted")

for j in range (x) :
    a.append(input("enter the element"))

for j in range (1,len(a)) :
    i=j-1
    k=a[j]
    while i>=0 and a[i]>k :
        a[i+1] = a[i]
        i=i-1
    a[i+1]=k

print a


