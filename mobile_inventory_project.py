mobile_store={}
cart={}
menu="""
                MENU
        PRESS 1 FOR MANAGER
        PRESS 2 FOR CUSTOMER"""
status=True
while status:
    specificaton={}
    specificatonc={}
    print (menu)
    role=int(input("enter your choice for role(1/2):"))
    if role == 1:
        print("PRODUCT MANAGER")
        product_name=input("enter product name:")
        model_num=input("enter model number:")
        colour=input("enter colour name:")
        qty=int(input("enter qty:"))
        price=int(input("enter price:"))
        #store details in nested dic
        specificaton["model"]=model_num
        specificaton["colour"]=colour
        specificaton["qty"]=qty
        specificaton["price"]=price
        #nested dic store in main dic
        mobile_store[product_name]=specificaton
        print(mobile_store) #print main dic with nested

    elif role==2:
        print("CUSTOMER")
        for k in mobile_store.keys():
            print("--------------------------------")
            print(f"PRODUCT:{k}")
            print("MODEL:"+mobile_store[k]["model"])
            print("COLOUR:"+mobile_store[k]["colour"])
            #print("QTY:"+mobile_store[k]["qty"])
            print("PRICE:"+str(mobile_store[k]["price"]))
        product_namec=input("enter product name:")
        model_numc=input("enter model name:")
        qtyc=int(input("enter number of quantity u want to buy:"))
        specificatonc["model"]=model_numc
        cart[product_namec]=specificatonc
        if qtyc<=qty:
            print("PRODUCT IS AVAILABLE")
            specificatonc["qty"]=qtyc
            for k in mobile_store.keys():
                for i in cart.keys():
                    print("COLOUR:"+mobile_store[k]["colour"])
                    pricec=+int(mobile_store[k]["price"])*+int(cart[i]["qty"])
                    print("PRICE FOR ONE:"+str(mobile_store[k]["price"]))
                    print("TOTAL PRICE :",pricec)
                    specificatonc["price"]=pricec
        else:
            print("OUT OF STOCK")
            
        #nested dic2 store in cart dic2
        print(cart)
        mobile_store[product_name]['qty']-=qtyc
    else:
        print("invalid input")

    choice=input("do yo want to continue? press 'y' for yes and 'n' for no:")
    if choice=='n' or choice=='no':
        status=False

for k in mobile_store.keys():
    print("--------------------------------")
    print(f"PRODUCT:{k}")
    print("MODEL:"+mobile_store[k]["model"])
    print("COLOUR:"+mobile_store[k]["colour"])
    print("QTY:"+str(mobile_store[k]["qty"]))
    print("PRICE:"+str(mobile_store[k]["price"]))