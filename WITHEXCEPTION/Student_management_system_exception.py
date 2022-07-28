


counsellor={}

selection_menu="""
            press 1 for Counsellor
            press 2 for Faculty
            press 3 for Student
            
"""

status=True

while status:
    print(selection_menu)
    role=int(input("Enter a role id: "))

    if role==1:
        st=True
        coun_menu="""
            1. Add student
            2. Remove student
            3. View all student
            4. View Specific Student
        """
        while status:
            print(coun_menu)
            con_data={}
            sub_dic1={}
      
            ch=int(input("Enter a choice by counsellor: "))
            if ch==1:
                srno=int(input("Enter a Serial Number: "))
                try: 
                    fname=input("Enter a First Name: ")
                    if fname.isalpha():
                        con_data["fname"]=fname
                    else:
                        raise TypeError

                except TypeError:
                    print("invalid name use only charactor value in name:")
                    fname=input("Enter a First Name: ")
                    con_data["fname"]=fname

                try: 
                    lname=input("Enter a Last Name: ")
                    if lname.isalpha():
                        con_data["lname"]=lname
                    else:
                        raise TypeError

                except TypeError:
                    print("invalid name use only charactor value in name:")
                    lname=input("Enter a Last Name: ")
                    con_data["lname"]=lname
                

                try:
                    contact=int(input("Enter a Contact Number: "))
                    if len(contact)==10 and contact.isdigit():
                        con_data["contact"]=contact
                    else:
                        raise TypeError
                except TypeError:
                    print("contact number is must have 10 digit")
                    contact=int(input("Enter a Contact Number: "))
                    con_data["contact"]=contact


                for i in range(1,3):
                    sub_dic={}
                    subject=input("Enter a Subject: ")
                    marks=int(input("Enter a Marks: "))

                    fees=int(input("enter a fees: "))

                    sub_dic["marks"]=marks
                    sub_dic["fees"]=fees
                    sub_dic1[subject]=sub_dic
                  
                    #sub_dic1[subject]=fees


                faculty=input("Enter a Faculty")
                
                con_data["subject"]=sub_dic1
               
               
                #con_data["Fees"]=sub_dic1
                #con_data["marks"]=
                con_data["faculty"]=faculty

                counsellor[srno]=con_data
                print(counsellor)
            elif ch==2:
                srno=int(input("Enter a serial no of student whoes data you want to remove: "))
                if srno in counsellor:
                    counsellor.pop(srno)
                    print("Student Data Deleted")
                else:
                    print("Wrong Serial Number")    

            elif ch==3:
                for k in counsellor.keys():
                    print(f"Serial No: ",{k})
                    print("First Name: ",counsellor[k]["fname"])
                    print("Last Name: ",counsellor[k]["lname"])
                    print("Contact : ",counsellor[k]["contact"])
                    
                    for j in counsellor[k]["subject"].keys():
                        print("Subject: ",j)
                        print("Marks: ",counsellor[k]['subject'][j]["marks"])
                        print("Fees: ",counsellor[k]['subject'][j]["fees"])
                        

                    
                    print("Faculty: ",counsellor[k]["faculty"])
            elif ch==4:
                    srno=int(input("Enter a serial no of student whoes data you want to see: "))
                #for k in counsellor.keys():
                    if srno in counsellor.keys():
                        print("Serial No: ",srno)
                        print("First Name: ",counsellor[srno]["fname"])
                        print("Last Name: ",counsellor[srno]["lname"])
                        print("Contact : ",counsellor[srno]["contact"])
                       # print("Subject: ",counsellor[srno]["subject"])

                        for j in counsellor[srno]["subject"].keys():
                            print("Subject: ",j)
                            print("Marks: ",counsellor[srno]['subject'][j]["marks"])
                            print("Fees: ",counsellor[srno]['subject'][j]["fees"])
                        

                        print("Faculty: ",counsellor[srno]["faculty"])
                    else:
                        print("student data is not available")   

            co_choice=input("Do you want to perform more operations? (y/n) ")
            if co_choice=='n':
                 status=False
            else:
                status=True
    elif role==2:
        fac_menu="""
                1.Add marks to student
                2.View all student
        
        """
        while status:
            fac_dic={}
            print(fac_menu)
            fac_choice=int(input("Enter a choice by Faculty: "))
            
            if fac_choice==1:

                if subject in counsellor.keys():
                    for i in range(1,3):
                        marks=int(input("Enter a Marks: "))

                        fac_dic[subject]=marks
                    print(fac_dic)
                else:
                    print("Subject not exist")
            elif fac_choice==2:
                for k in counsellor.keys():
                    print(f"Serial No: ",{k})
                    print("First Name: ",counsellor[k]["fname"])
                    print("Last Name: ",counsellor[k]["lname"])
                    print("Contact : ",counsellor[k]["contact"])
                    
                    for j in counsellor[k]["subject"].keys():
                        print("Subject: ",j)
                        print("Marks: ",counsellor[k]['subject'][j]["marks"])
                        print("Fees: ",counsellor[k]['subject'][j]["fees"])
                        

                    print("Faculty: ",counsellor[k]["faculty"])
            fac_choice=input("Faculty wants to perfom any other operations? (y/n) ")
            
            if fac_choice=='n':
                status=False
            else:
                status=True
    elif role==3:
        student_menu="""
                1.View Student
                2.Pay Fees
        """  

        while status: 
            print(student_menu)
            student_choice=int(input("Enter a Student Choice: "))
            if student_choice==1:
                srno=int(input("Enter a serial no of student whoes data you want to see: "))
                if srno in counsellor.keys():
                        print("Serial No: ",srno)
                        print("First Name: ",counsellor[srno]["fname"])
                        print("Last Name: ",counsellor[srno]["lname"])
                        print("Contact : ",counsellor[srno]["contact"])
                       # print("Subject: ",counsellor[srno]["subject"])

                        for j in counsellor[srno]["subject"].keys():
                            print("Subject: ",j)
                            print("Marks: ",counsellor[srno]['subject'][j]["marks"])
                            print("Fees: ",counsellor[srno]['subject'][j]["fees"])
                        

                        print("Faculty: ",counsellor[srno]["faculty"])
                else:
                        print("Please check your serial number")   
                

            elif student_choice==2:
                sum=0
                srno=int(input("Enter a serial no of student whoes data you want to see: "))
                if srno in counsellor.keys():
                    for j in counsellor[srno]["subject"].keys():
            
                            sum=sum+counsellor[srno]['subject'][j]["fees"]
                    print("Fees Needs To Pay: ",sum)
                         

                else:
                    print("Please check your serial number") 


            stu_choice=input("Do you want to do any further operations:: ")
            if stu_choice=='n':
                 status=False
            else:
                status=True



    role_choice=input("Do you want to continue: ")
    if role_choice=='n':
        status=False
    else:
        status=True




