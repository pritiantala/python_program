class StudentClass:
    name=""
    subject=""
    address=""
    fees=""
    email=""
    contact=""
    marks=""

    dict={}

    def cresteFaculty(self,name,email,address,contact,subject,fees,marks):
        innerDict={}
        self.name=name
        self.email=email
        self.address=address
        self.contact=contact
        self.subject=subject
        self.fees=fees
        self.marks=marks

        innerDict['email']=self.email
        innerDict['city']=self.address
        innerDict['contact']=self.contact
        innerDict['subject']=self.subject
        innerDict['fees']=self.fees
        innerDict['marks']=self.marks

        self.dict[name]=innerDict

        print(self.dict)