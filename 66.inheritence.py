#first two functions are normal functions
#third function in all classes is overriding function

class A:
    def first(self):
        print("first alphabet is A")
    def after1(self):
        print("after A is B")
    def classname(self):
        print("this is class A")
class B(A):
    def second(self):
        print("second alphabet is A")
    def after2(self):
        print("after B is c")
    def classname(self):
        print("this is class B")
class C(B):
    def third(self):
        print("third alphabet is A")
    def after3(self):
        print("after C is D")
    def classname(self):
        print("this is class C ")
# all functions calling in main function with objects
def main():
    a=A()
    b=B()
    c=C()

    a.first()
    b.second()
    c.third()
    a.after1()
    b.after2()
    c.after3()
    a.classname()
    b.classname()
    c.classname()
#calling the main function
main()