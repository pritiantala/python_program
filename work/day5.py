# while loop
#example 1
i=1
while i<=5:
    print("play game")
    i += 1

#take input from user and check true or false
status=True
while status:
    subject=input("enter your subject:")
    choice =input("do you want to enter more subject? press 'y' for yes and 'n' for no:")
    if choice=='n' or choice=='no' or choice=='N':
        status=False

#enter marks of student ,if student is pass then print pass and if student is fail then print fail and program is terminate
status=True
while status:
    marks=int(input("enter your marks:"))
    if marks<=35:
        print("fail")
        status=False
    else:
        print("pass")

#number guessing game
import random
computer_guess= random.randint(1,100)

status= True
while status:
        user_guess=int(input("enter number:"))
        if user_guess>computer_guess:
            print("HINT:guess lower number")
        elif user_guess<computer_guess:
            print("HINT:guess higher number")
        else:
            print("YOU GOT IT!!!")
            status=False
#number guessing games for 5 times
import random
computer_guess= random.randint(1,100)

trail=5
while trail > 0:
        user_guess=int(input("enter number:"))
        if user_guess>computer_guess:
            print("HINT:guess lower number")
        elif user_guess<computer_guess:
            print("HINT:guess higher number")
        else:
            print("YOU GOT IT!!!")
            trail=0
        trail -= 1    

#nested for loop
#example 1
from doctest import Example


for raw in range(1,6):
    for col in range(1,6):
        print("*",end=" ")
    print()

#example 2
for row in range(1,6):
    for col in range(1,6):
        if row==3 and col==3:
            print("$",end=" ")
        else:
            print("*",end=" ")
    print()

#example3
for i in range(1,6):
    for a in range(1,i+1):
        print("*",end=" ")
    print()

#example4
for i in range(1,6):
    for a in range(1,i+1):
        print(i,end=" ")
    print()

#Example5
for i in range(1,6):
    for a in range(1,i+1):
        print(a,end=" ")
    print()

#example6
for i in range(1,6):
    for a in range(1,i+1):
        if i%2==0:
            print("0",end=" ")
        else:   
            print("1",end=" ")
    print()

#example7
for i in range(1,6):
    for a in range(1,i+1):
        if a%2==0:
            print("0",end=" ")
        else:   
            print("1",end=" ")
    print()

#jumping statement : break
for i in range(1,6):
    marks=int(input("enter marks:"))
    if marks>35:
        print("pass")
    else:
        break

#continue
for i in range(1,6):
    if i==3:
        continue
    else:
        print(i)

#pass
for i in range(1,6):
    if i==3:
        pass
    else:
        print(i)
