max = 4
stack = [None]

top = -1

def push():
    global top 
    
    if top == max - 1:
        print("Stack Overflow")
    else:
        item = int(input("Enter the stack value: "))
        top += 1       
        stack[top] = item 
        print(f"Your stack array is {stack}")

def pop():
    global top
    
    if top == -1:
        print("Stack Underflow")
    else:
        item = stack[top] 
        stack[top] = None  
        top -= 1          
        print("Pop element is", item)

def peek():
    if top == -1:
        print("Stack is empty")
    else:
        print("Top is", stack[top])

def display():
    if top == -1:
        print("Stack is empty")
    else:
        for i in range(top, -1, -1):
            print("Display Element at index", i, "is", stack[i])

def isEmpty():
    if top == -1:
        print("Stack is Empty")
    else:
        print("Stack is Not Empty")

def isFull():
    if top == max - 1:
        print("Stack is Full")
    else:
        print("Stack is Not Full")
flag = True
def main():
    while True:
        print("\n1.push\n2.pop\n3.peek\n4.Display\n5.is empty\n6.is full\n7.Exit\n")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            push()
        elif choice == choice == 2:
            pop()
        elif choice == 3:
            peek()
        elif choice == 4:
            display()
        elif choice == 5:
            isEmpty()
        elif choice == 6:
            isFull()
        elif choice == 7:
            print("Exiting program.")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
