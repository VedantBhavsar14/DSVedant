arr=[10,20,30,40,50,60,70,80,90,100]
low=0
high=len(arr)-1

mid=int((low+high)/2)

key=int(input("Enter the number to search"))
for i in range(len(arr)):
    if mid == key :
        print(f"Element found at index {mid}")
        break
    
    elif mid<key:
        low=mid+1
        mid=int((low+high)/2)
        if arr[mid]==key:
            print(f"Element found at index {mid}")
            break
        
    elif mid>key:
        high=mid-1
        mid=int((low+high)/2)    
        if arr[mid]==key:
            print(f"Element found at index {mid}")
            break
        
else:
    print("Element not found")