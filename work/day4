#project kalyan jewellers
customer_name=input("enter customer name:")
customer_monum=int(input("enter mobile number:"))
customer_age=int(input("enter your age:"))
customer_gender=input("enter customer gender:")
product_name=input("enter product name:")
product_qty=float(input("enter product qty in gram:"))
current_price= 4829
making_charge= 589
price_qty=(current_price * product_qty)

#purchase amount
if product_qty >=10:
        making_charg2 = (589*product_qty)/100
        purchase_amount=price_qty + making_charg2 + making_charge
        print("total amount:",purchase_amount)
        if customer_age >= 60:
         if customer_gender == 'm' and purchase_amount > 200000 and purchase_amount < 500000:
            total=(purchase_amount*10)/100
            purchase_amount1 = purchase_amount- total
            print("total price:",purchase_amount1)
        elif customer_gender == 'm' and purchase_amount > 500000 and purchase_amount < 1000000:
            total2=(purchase_amount*15)/100
            purchase_amount1 =purchase_amount- total2
            print("total price:",purchase_amount1)
        elif customer_gender == 'm' and purchase_amount > 1000000:
            total3=(purchase_amount*20)/100
            purchase_amount1 =purchase_amount- total3
            print("total price:",purchase_amount1)
        elif customer_gender == 'f' and purchase_amount > 200000 and purchase_amount < 500000:
            total4=(purchase_amount*15)/100
            purchase_amount1 =purchase_amount- total4
            print("total price:",purchase_amount1)
        elif customer_gender == 'f' and purchase_amount > 500000 and purchase_amount < 1000000:
            total5=(purchase_amount*20)/100
            purchase_amount1 =purchase_amount- total5
            print("total price:",purchase_amount1)
        elif customer_gender == 'f' and purchase_amount > 1000000:
            total6=(purchase_amount*25)/100
            purchase_amount1 =purchase_amount- total6
            print("total price:",purchase_amount1)
        else:
            if customer_gender == 'm' and purchase_amount > 200000 and purchase_amount < 500000:
                total7=(purchase_amount*5)/100
                purchase_amount1 =purchase_amount- total7
                print("total price:",purchase_amount1)
            elif customer_gender == 'm' and purchase_amount > 500000 and purchase_amount < 1000000:
                total8=(purchase_amount*10)/100
                purchase_amount1 =purchase_amount - total8
                print("total price:",purchase_amount1)
            elif customer_gender == 'm' and purchase_amount > 1000000:
                total11=(purchase_amount*15)/100
                purchase_amount1 =purchase_amount- total11
                print("total price:",purchase_amount1)
            elif customer_gender == 'f' and purchase_amount > 200000 and purchase_amount < 500000:
                total9=(purchase_amount*10)/100
                purchase_amount1 =purchase_amount- total9
                print("total price:",purchase_amount1)
            elif customer_gender == 'f' and purchase_amount > 500000 and purchase_amount < 1000000:
                total10=(purchase_amount*15)/100
                purchase_amount1 =purchase_amount- total10
                print("total price:",purchase_amount1)
            elif customer_gender == 'f' and purchase_amount > 1000000:
                total12=(purchase_amount*20)/100
                purchase_amount1 =purchase_amount- total12
                print("total price:",purchase_amount1)
    #invoice
        print("INVOICE")
        print()
        print("NAME:",customer_name)
        print("MOBILE NUMBER:",customer_monum)
        print("AGE:",customer_age)
        print("GENDER:",customer_gender)
        print("PRODUCT NAME:",product_name)
        print("QUANTATY:",product_qty)
        print("CURRENT PRICE OF 1 GRAM GOLD:",current_price)
        print("MAKING CHARGES OF BELLOW 10 GRAM GOLD:",making_charge)
        print("TOTAL AMOUNT WITHOUT DISCOUNT:",purchase_amount)
        print()
        #discount
        if customer_age >= 60:
                if customer_gender =='m' and purchase_amount>200000 and purchase_amount<500000:
                    discount=10
                    print("AVAILABLE DISCOUNT IS:",discount,"%")
                elif customer_gender =='m' and purchase_amount>500000 and purchase_amount<1000000:
                    discount=15
                    print("AVAILABLE DISCOUNT IS:",discount,"%")
                elif customer_gender =='m' and purchase_amount>1000000 :
                    discount=20
                    print("AVAILABLE DISCOUNT IS:",discount,"%")
                elif customer_gender =='f' and purchase_amount>200000 and purchase_amount<500000:
                    discount=15
                    print("AVAILABLE DISCOUNT IS:",discount,"%")
                elif customer_gender =='f' and purchase_amount>500000 and purchase_amount<1000000:
                    discount=20
                    print("AVAILABLE DISCOUNT IS:",discount,"%")
                elif customer_gender =='f' and purchase_amount>1000000:
                    discount=25
                    print("AVAILABLE DISCOUNT IS:",discount,"%")
        else:
                    if customer_gender =='m' and purchase_amount>200000 and purchase_amount<500000:
                        discount=5
                        print("AVAILABLE DISCOUNT IS:",discount,"%")
                    elif customer_gender =='m' and purchase_amount>500000 and purchase_amount<1000000:
                        discount=10
                        print("AVAILABLE DISCOUNT IS:",discount,"%")
                    elif customer_gender =='m' and purchase_amount>1000000 :
                        discount=15
                        print("AVAILABLE DISCOUNT IS:",discount,"%")
                    elif customer_gender =='f' and purchase_amount>200000 and purchase_amount<500000:
                        discount=10
                        print("AVAILABLE DISCOUNT IS:",discount,"%")
                    elif customer_gender =='f' and purchase_amount>500000 and purchase_amount<1000000:
                        discount=15
                        print("AVAILABLE DISCOUNT IS:",discount,"%")
                    elif customer_gender =='f' and purchase_amount>1000000:
                        discount=20
                        print("AVAILABLE DISCOUNT IS:",discount,"%")
                    print("DISCOUNT AMOUNT IS:",purchase_amount1)

        print("GST:",3,"%")
        print()
        gst=(purchase_amount1*3)/100
        net_amount=purchase_amount1+gst
        print("PAYABLE NET AMOUNT:",net_amount)
else:
    total=price_qty+making_charge
    print("total amount:",total)
    print("INVOICE")
    print()
    print("NAME:",customer_name)
    print("MOBILE NUMBER:",customer_monum)
    print("AGE:",customer_age)
    print("GENDER:",customer_gender)
    print("PRODUCT NAME:",product_name)
    print("QUANTATY:",product_qty)
    print("CURRENT PRICE OF 1 GRAM GOLD:",current_price)
    print("MAKING CHARGES OF BELLOW 10 GRAM GOLD:",making_charge)
    print("TOTAL AMOUNT WITHOUT DISCOUNT:",total)
    print()

    print("GST:",3,"%")
    print()
    gst=(total*3)/100
    net_amount1=total+gst
    print("PAYABLE NET AMOUNT:",net_amount1)






