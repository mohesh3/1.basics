class Student():
    def __init__(self, name):
        self.name = name
		
    def display(self):
        return self.name

st1 = Student("mohesh")
st2 = Student("gokul")

print(st1.display())
print(st2.display())