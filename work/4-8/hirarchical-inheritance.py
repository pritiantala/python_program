class user:
    def __init__(self):
            print("user class")
            
            
    def input(self):
        self.email=input("enter email:")
        self.password=input("enter password:")
            
class doctor(user):
    def doc_input(self):
        self.specification=input("enter specification:")

    def displayd(self):
        print("doctor email=",self.email)
        print("doctor password=",self.password)
        print("doctor specification=",self.specification)
                
class patient(user):
    def p_input(self):
        self.bloodgroup=input("enter bloodgroup:")

    def displayp(self):
        print("patient email=",self.email)
        print("patient password=",self.password)
        print("patient bloodgroup=",self.bloodgroup)

choice=int(input("enter your choice press 1 for doctor and 2 for patient: "))
if choice==1:
    doctor=doctor()
    doctor.input()
    doctor.doc_input()
    doctor.displayd() 
elif choice==2:
    patient=patient()
    patient.input()
    patient.p_input()
    patient.displayp()    
    