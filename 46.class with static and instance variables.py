class Student:
	department = 'ece'				
	def __init__(self,name,roll):
		self.name = name		 
		self.roll = roll		 


a = Student('mohesh', "11189c171")
b = Student('gokul', 2)

print(a.department,a.name,a.roll)
print(b.department,b.name,b.roll)

print(Student.department)

a.department = 'cse'
print(a.department)
print(b.department)

Student.department = 'mech'
print(a.department)
print(b.department)

a.department="ece"
print("roll number = ",a.roll,"\t name =",a.name,"\t department = ",a.department)
print("roll number = ",b.roll,"\t name =",b.name,"\t department = ",b.department)
