# use of elif statement
num=int(input("enter a number:"))
if num == 10:
    print('num=10')
elif num == 20:
    print("num=20") 
elif num == 30:
    print("num=30")
else:
    print("invalid number")   

#check the number using elif statement
num=int(input("enter a number:"))
if num>=10 and num<=50:
    print("number is between 10-50")
elif num>=51 and num<=100:
    print("number is between 51-100") 
else:
    print("number is below 10 or above 100")

#accept marks from user and give them grade
marks=int(input("enter student marks"))
if marks>=70:
    print("A grade")
elif marks >= 60 and marks < 70:
    print("B grade")
elif marks >= 50 and marks < 60:
    print("C grade")
elif marks >= 40 and marks < 50:
    print("D grade")
else:
    print("fail")

#check email and password is valid or not using nested if conditin
email=p@gmail.com
password=123456

s_email=input("enter email:")
s_password=input("enter password:")

if s_email == email:
    if s_password == password:
        print("welcome to tops")
    else:
        print("invalid password")
else:
    print("invalid email")

 #accept marks from user and give them grade, if marks is below 0 or above 100 then print invalid marks using nested condition
marks=int(input("enter student marks"))
if marks >= 0 and marks <= 100:

    if marks>=70:
        print("A grade")
    elif marks >= 60 and marks < 70:
        print("B grade")
    elif marks >= 50 and marks < 60:
        print("C grade")
    elif marks >= 40 and marks < 50:
        print("D grade")
    else:
        print("fail")
else:
    print("invalid marks")   

#for loop statement

for i in range(1,6):
    print(i)

for i in range(5):
    print(i)

for i in range(5,0,-1):
    print(i)

for i in range(1,11,2):
    print(i)

for i in range(1,4):
    print(i,"hello")
    