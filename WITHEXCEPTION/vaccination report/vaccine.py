from datetime import datetime
from secrets import choice
from telnetlib import STATUS
import os
import time
vaccine_date=datetime.now()
vaccine_date=str(vaccine_date.date())
t=time.localtime()
vaccine_time=time.strftime("%H:%M:%S",t)
path=r'C:\Users\PRITI\Documents\GitHub\python_program\WITHEXCEPTION\vaccination report\report'
file=open(os.path.join(path,vaccine_date),'a')

STATUS = True
while STATUS:
    file.write("---------INFO---------------------")
    file.write(f"\n VACCINATION DATE:{vaccine_date}")
    file.write(f"\n VACCINATION TIME:{vaccine_time}")
    try: 
            f_name=input("enter your first name:")
            if f_name.isalpha():
                  file.write(f" \n FIRST NAME:{f_name}")      
            else:
                raise TypeError

    except TypeError:
            print("invalid name use only charactor value in name:")
            f_name=input("enter your first name:")
            
            file.write(f" \n FIRST NAME:{f_name}")
    

    try: 
            l_name=input("enter your last name:")
            if l_name.isalpha():
                  file.write(f"\n LAST NAME:{l_name}")      
            else:
                raise TypeError

    except TypeError:
            print("invalid name use only charactor value in name:")
            l_name=input("enter your last name:")
            
            file.write(f"\n LAST NAME:{l_name}")
    
    try:
            contact=input("Enter a Contact Number: ")
            if len(contact)==10 and contact.isdigit():
                file.write(f"\n CONTACT NUMBER:{contact}")
            else:
                raise TypeError
    except TypeError:
            print("contact number is must have 10 digit")
            contact=input("Enter a Contact Number: ")
            file.write(f"\n CONTACT NUMBER:{contact}")
        
    age=int(input("enter your age:"))
    try:
            b_date=input("enter birth date in formate dd/mm/yyyy:")
            day,month,year = b_date.split('/')
            if len(b_date)==10 and month<=12:
                datetime(int(day),int(month),int(year))
                file.write(f"\n BIRTH DATE:{b_date}")
            else:
                raise TypeError
    except TypeError:
            print("enter bdate in dd/mm/yyyy formate")
            b_date=input("enter birth date in formate dd/mm/yyyy:")
            file.write(f"\n BIRTH DATE:{b_date}")

    gender=input("enter your gender:")
    vaccine=input("enter a type of vaccine you take:")
    vaccine_dose=int(input("enter dose no 1\2:"))

    file.write(f"\n AGE:{age}")
    
    file.write(f"\n GENDER:{gender}")
    file.write(f"\n VACCINE TYPE:{vaccine}")
    file.write(f"\n VACCINE DOSE NO:{vaccine_dose}")
        
    file.write("\n ------------------------------------")

    choice=input("do you want to enter any other person ??press 'y' for yes and 'n' for no:")
    if choice=='n' or choice=='no':
            STATUS=False
