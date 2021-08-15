"""Create a class with DEFAULT fields and methods.
 Access these fields and methods from any other class in the same package"""
class defaults():
     def __init__(self,student1,student2):
                self.student1=student1
                self.student2=student2

class other(defaults):
    def name(self,student1,student2):
        print("student1=",student1)
        print("student2=",student2)

s=other("st1","st2")

s.name("mohesh","moulesh")
