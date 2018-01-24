a = []
x = input("Enter the total numbers in the list")

for j in range (x) :
    a.append(input("Enter the elements "))
max = a[0]
min = a[0]

for j in range (x) :
    if(a[j]>max) :
        max = a[j]
        j = j+1

    elif(a[j] < min) :
        min = a[j]
        j=j+1

    else :
        j = j+1

print("The maximum elements is {}".format(max))
print ("The minimum elemets is {}".format(min))
