class FacultyClass:
    name=""
    subject=""
    city=""
    email=""
    contact=""

    dict={}

    def cresteFaculty(self,name,email,city,contact,subject):
        innerDict={}
        self.name=name
        self.email=email
        self.city=city
        self.contact=contact
        self.subject=subject

        innerDict['email']=self.email
        innerDict['city']=self.city
        innerDict['contact']=self.contact
        innerDict['subject']=self.subject

        self.dict[name]=innerDict

        print(self.dict)