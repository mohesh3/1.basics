class person:
    def __init__(self, name, age):
        self.personName = name
        self.personAge = age
    def displayAge(self):			
        print("Age: ", self.personAge)

obj = person("mohesh", 20)
print("Name: ", obj.personName)
obj.displayAge()
