class user:
    def __init__(self):
        print("user class")
        
    def input(self):
        self.email=input("enter email:")
        self.password=input("enter password:")

class doctor(user):
    def doc_input(self):
        self.specification=input("enter specification:")

    def display(self):
        print("doctor email=",self.email)
        print("doctor password=",self.password)
        print("doctor specification=",self.specification)



doctor=doctor()
doctor.input()
doctor.doc_input()
doctor.display()    
    