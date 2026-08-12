arr=[20,10,40,30,60,50,80,70,90]
print("Unsorted array is",arr)

n=len(arr)

for i in range(n):
    min_index=i
    for j in range(i+1,n):
        if arr[j]<arr[min_index]:
            min_index=j
    arr[i],arr[min_index]=arr[min_index],arr[i]

print("Sorted array is",arr)
