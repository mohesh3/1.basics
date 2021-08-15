"""Create a class with PRIVATE fields, private method and a main method.
Print the fields in main method. Call the private method in main method.
Create a sub class and try to access the private fields and methods from sub class."""
class _private :
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname

    def printing(self):
        print(self.firstname,self.lastname)
    
class sub(_private):
    def printing1(self):
     print(self.firstname,self.lastname)

p=_private("private","feilds")
p.printing()
s=sub("sub","class")
s.printing1()