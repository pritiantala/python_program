#hierarchical inheritance
class A:
    def displayA(self):
        print("A class display")
class B(A):
    def displayB(self):
        
        print("B class display")
class C(A):
    def displayC(self):
        self.displayA()
        print("C class display")
class D(B):
    def displayd(self):
        self.displayA()
        self.displayB()
        print("hybrid inheritance")

obj=D()
obj.displayd()
obj=C()
obj.displayC()
