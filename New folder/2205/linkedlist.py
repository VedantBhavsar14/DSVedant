class Node:
    def __init__(self,marks,rollno,name):
        self.rollno=rollno
        self.name=name
        self.marks=marks
        self.next=None

class StudentRecordSystem:
    def __init__(self):
        self.head=None

    def add_student(self):
        rollno=int(input("Enter your roll no"))
        marks=int(input("Enter your marks"))
        name=input("Enter your name")

        new_Node=Node(rollno,marks,name)

        if self.head is None:
            self.head=new_Node

        else:
            temp=self.head

            while temp.next is not None:
                temp=temp.next
            temp.next=new_Node

        print("New Student data is created successfully")
