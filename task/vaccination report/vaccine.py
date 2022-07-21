from datetime import datetime
from secrets import choice
from telnetlib import STATUS
import os
import time
vaccine_date=datetime.now()
vaccine_date=str(vaccine_date.date())
t=time.localtime()
vaccine_time=time.strftime("%H:%M:%S",t)
path=r'C:\Users\PRITI\Documents\GitHub\python_program\task\vaccination report\report'
file=open(os.path.join(path,vaccine_date),'a')

STATUS = True
while STATUS:
        f_name=input("enter your first name:")
        l_name=input("enter your last name:")
        age=int(input("enter your age:"))
        b_date=input("enter birth date in formate dd/mm/yyyy:")
        gender=input("enter your gender:")
        vaccine=input("enter a type of vaccine you take:")
        vaccine_dose=int(input("enter dose no 1\2:"))



        file.write("---------INFO---------------------")
        file.write(f"\n VACCINATION DATE:{vaccine_date}")
        file.write(f"\n VACCINATION TIME:{vaccine_time}")
        file.write(f" \n FIRST NAME:{f_name}")
        file.write(f"\n LAST NAME:{l_name}")
        file.write(f"\n AGE:{age}")
        file.write(f"\n BIRTH DATE:{b_date}")
        file.write(f"\n GENDER:{gender}")
        file.write(f"\n VACCINE TYPE:{vaccine}")
        file.write(f"\n VACCINE DOSE NO:{vaccine_dose}")
        
        file.write("\n ------------------------------------")

        choice=input("do you want to enter any other person ??press 'y' for yes and 'n' for no:")
        if choice=='n' or choice=='no':
            STATUS=False
