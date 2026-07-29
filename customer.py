n = int(input("Enter number of Account IDs: "))

a = []

for i in range(n):
    a.append(int(input(f"Enter the account ID {i+1}")))

key = int(input("Enter Account ID to search: "))

found = 0

for i in range(n):
    if a[i] == key:
        print("Account ID Found")
        print("Position =", i + 1)
        found = 1
        break

if found == 0:
    print("Account ID Not Found")