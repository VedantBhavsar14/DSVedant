arr = list(map(int, input("Enter employee IDs: ").split()))

print("Your entered array is =", arr)

print("Select sorting method:\n")
print("1. Bubble Sort")
print("2. Selection Sort")

x = int(input("Choose sorting type: "))

n = len(arr)

if x == 1:
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print(arr)


elif x == 2:
    for i in range(n - 1):
        SI = i

        for j in range(i + 1, n):
            if arr[j] < arr[SI]:
                SI = j

        arr[i], arr[SI] = arr[SI], arr[i]

else:
    print("Invalid choice!")

print("The sorted array is =", arr)