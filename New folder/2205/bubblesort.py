n=int(input("Enter a number"))
arr=[]

for i in range(n):
    a=int(input(""))
    arr.append(a)

print("Your entered array is",arr)

state=0

for i in range(n):
    for j in range(n-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            state=1

    if state==0:
        break
    else:
        pass 

print("The sorted array is",arr)

