#multi-level inheritance
class A:
    def displayA(self):
        print("A class display")
class B(A):
    def displayB(self):
        print("B class display")
class C(B):
    def displayC(self):
        self.displayA()
        self.displayB()
        print("C class display")

obj=C()

obj.displayC()