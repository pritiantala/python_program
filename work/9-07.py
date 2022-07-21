from secrets import choice


fruits={}
menu="""
            press 1 for add fruits
            press 2 for view fruits
            press 3 for purchase fruits
            press 4 for exit
"""
status=True
while status:
    print (menu)
    specification={}
    choice=int(input("enter your choice:"))
    if choice==1:
        fruit_name=input("enter fruit name:")
        qty=int(input("enter qty of fruits:"))
        price=int(input("enter price of fruits:"))

        specification['qty']=qty
        specification['price']=price

        fruits[fruit_name]=specification

    elif choice==2:
        for k in fruits.keys():
            print("---------------------")
            print(f"FRUIT NAME:{k}")
            print(f"fruit qty:",fruits[k]["qty"])
            print(f"fruit price:(for 1 piece)",fruits[k]["price"])

    elif choice==3:
        for k in fruits.keys():
            print("---------------------")
            print(f"FRUIT NAME:{k}")
            print(f"fruit price:(for 1 piece)",fruits[k]["price"])
        fruit_name=input("enter fruit which you want to buy:")
        if fruit_name in fruits.keys():
            qty=int(input("enter no qty you want:"))

            price=qty*fruits[fruit_name]['price']
            print("price=",price)
    
    elif choice==4:
        status=False
        break

    user_choice=input("do yo want to continue?? press 'y' for yes and 'n'for no:")
    if user_choice=='n':
        status=False
    else:
        status=True