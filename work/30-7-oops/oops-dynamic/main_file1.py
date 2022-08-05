from telnetlib import STATUS
import faculty1,student1

f=faculty1.FacultyClass()        #obj=filename.classname

s=student1.StudentClass()


choice=int(input("choice 1 for faculty and choice 2 for student:"))
if choice==1:

    STATUS=True

    while STATUS:
        fname=input("enter faculty name:")
        subject=input("enter your subject:")
        email=input("enter email:")
        contact=input("enter contact:")
        city=input("enter your city:")

        f.cresteFaculty(fname,email,city,contact,subject)
        

        choice=input("do you want to make details press 'y' for yes and 'n' for no:")
        if choice=='n':
            STATUS=False

elif choice==2:
    STATUS=True

    while STATUS:
            fname=input("enter student name:")
            subject=input("enter your subject:")
            email=input("enter email:")
            contact=input("enter contact:")
            city=input("enter your city:")
            fees=input("enter fees:")
            marks=input("enter marks")
            s.cresteFaculty(fname,email,city,contact,subject,fees,marks)
            

            choice=input("do you want to make details press 'y' for yes and 'n' for no:")
            if choice=='n':
                STATUS=False