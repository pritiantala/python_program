from telnetlib import STATUS


menu="""
            MENU
        VADAPAV 30
        DABELI  30
        BHEL    70
"""
data="""
            CHOICE
        (1)PRESS 1 FOR ADD TO CART
        (2)PRESS 2 FOR CHECK ITEM
        (3)PRESS 3 FOR REMOVE ITEM
        (4)PRESS 4 FOR BILL AMOUNT 
"""
print(menu)

print("JAY BHAVANI")
item=[]     #blank list for add item
QTY=[] #add quantity of item
price=[]       #add  price
total=[]
STATUS=True
while STATUS:
    print(data)
    choice=int(input("enter your choice:"))
    if choice==1:
        item_name=input("enter item:")
        item_price=int(input("enter price:"))
        item_qty=int(input("enter quantity:"))
        item.append(item_name)
        price.append(item_price)
        QTY.append(item_qty)
    elif choice==2:
        item_name=input("enter item:")
        if item_name in item:
            print("AVAILABLE")
        else:
            print("NOT AVAILABLE")
    elif choice==3:
        item_name=input("enter item:")
        if item_name in item:
            for item_name in item:
                index1=item.index(item_name)
                price.pop(index1)
                item.pop(index1)
                QTY.pop(index1)
        else:
            print("sorry,item is not available")        
           
    elif choice==4:
        for i in item:
            print(i)
        print("total number of item in list:",len(item))
        for i in range(0, len(price)):
            total.append(price[i] * QTY[i])

        print("total price:",total)
        print("total quantaty:",QTY)
        print("total amount:",sum(total))
    else:
        print("invalid input")
    user_choice=input("do yo want to perform more operation?,press 'y' for yes and 'n' for no:")
    if user_choice=='n' or user_choice=='N' or user_choice=='no':
        STATUS=False
    else:
        STATUS=True
         