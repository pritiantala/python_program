from views import *

name=input("enter your name:")

menu="""
            MENU
        1- LAPTOP
        2-MOBILE

"""
print(menu)

choice=int(input("enter you choice:"))

if choice==1:
    viewlaptop()
    laptop_name=input("enter laptop name which you want to purchase:")
    qty=int(input("enter no. of qty do you want to purchase:"))
    total_price=purchaseLaptop(laptop_name,qty)
    choice=input("do you want to purchase??press 'y' for yes:")
    if choice=='y' or choice=='yes':
        addTocart(name,"laptop",laptop_name,qty,total_price)

elif choice==2:
    viewMobile()
    
else:
    print("invalid input")