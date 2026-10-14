#class Queue:
 #   def __init__(self):
  #      self.arr=[]

arr=[]
max=5
top=0

def push():
    arr.append(int(input("Enter the call id number")))

for _ in range(max):
    push()

def pop():
    count =top
    if arr==0:
        print("Stack Underflow")

    else:
        arr.pop(count)

        if count == max:
            print("Stack Overflow")

        else:
            count+=1
            print(arr)

pop()