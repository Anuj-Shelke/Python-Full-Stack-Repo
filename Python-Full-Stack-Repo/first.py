class Student:
    def __init__(self,name,branch,marks):
        self.name = name
        self.branch = branch
        self.marks = marks 

    def display(self):
        print(self.name,self.branch,self.marks)

s1 = Student("Anuj","AIDS",45)
S2 = Student("Rahul","Computer",78)

S2.display()
s1.display()




