#Create a class with PROTECTED fields and methods.
#Access these fields and methods from any other class in the same package.
#Also, Access the PROTECTED fields and methods from child class located in a different package
#Access the PROTECTED fields and methods from any class in different package


class defaults():
     def __init__(self,student1,student2):
                self.protected_member=student1
                self.student2=student2

class other(defaults):
    def name(self,student1,student2):
        print("student1=",student1)
        print("student2=",student2)

s=other("st1","st2")
print(s.protected_member)
s.name("mohesh","moulesh")
print(s.protected_member)
