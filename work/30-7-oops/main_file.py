import faculty,student

f=faculty.FacultyClass()        #obj=filename.classname

s=student.StudentClass()

print(f.name)
print(s.name)

f.cresteFaculty("aaaa","p@gamil.com","ahmedabad","9445465","python")
print(f.name)
print(f.subject)


s.cresteFaculty("ppppp","p@gamil.com","ahmedabad","9445465","python",50000,50)
print(s.name)
print(s.subject)
print(s.fees)
print(s.marks)
