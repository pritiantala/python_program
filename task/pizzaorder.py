class pizza:
    def __init__(self,price1=10.99,price2=9.5,quantity_pizza=0,quantity_pasta=0,total="",name="",colddrink=1,bruschetta=2,chocobrowni=2):
        self.price1 = price1
        self.price2 = price2
        self.quantity_pizza=quantity_pizza
        self.quantity_pasta=quantity_pasta
        self.total=total
        self.name=name
        self.colddrink=colddrink
        self.bruschetta=bruschetta
        self.chocobrowni=chocobrowni

status = True
while status:
        def inputdetails(self):
            self.name = input("enter a customer name : ")
            print(f"Hello {self.name}, Welcome to Pizzariya")
        def food(self):
            print("""                ----------Menu--------------
                
                    1 large pizza = 10.99 AUD 

                    2 large Pizzas = 20.99 AUD 

                    3 Large Pizzas = 29.99 AUD

                    ***Buy 4 or more pizza and get 1.5lt of soft drink free***


                    1 large pasta = 9.5 AUD 

                    2 large pastas = 17.00 AUD 
                    
                    3 large pastas = 27.50 AUD

                    ***Buy 4 or more pastas and get 2 bruschetta free.***
                    ***Buy 4 or more pizzas and pastas and get 2 chocco brownies ice cream free.""")
            
            
            print("""
                        1.  Pizza
                        2. Pasta
                        0. exit""")
            choice=int(input(" Order of food : "))
            if choice==1:
                self.quantity_pizza = int(input("enter a quantity "))
                if self.quantity_pizza==1:
                    self.price1=10.99
                    print("Your pizza order amount is:",self.price1)
                    
                elif self.quantity_pizza==2:
                    self.price1=self.price1 + 10
                    print("Your pizza order amount is:",self.price1)
                    
                elif self.quantity_pizza==3:
                    self.price1=self.price1+ 19
                    print("Your pizza order amount is:",self.price1)
                    
                elif self.quantity_pizza>=4:
                    self.price1=self.price1*self.quantity_pizza
                    print("Your pizza order amount is:",self.price1)
                    total_quantity=self.quantity_pizza
                    print(f" Quantity of pizza is {self.quantity_pizza} ***CONGRATULATIONS!!!!  1.5LT COLDDRINK {self.colddrink}  free ")
                else:
                    print(" Invalid Quantity ")
            elif choice==2:
                self.quantity_pasta = int(input("enter a quantity "))
                if self.quantity_pasta==1:
                    self.price2=9.5
                    print("Your pasta order amount is:",self.price2)
                    
                elif self.quantity_pasta==2:
                    self.price2=self.quantity_pasta*9.5
                    print("Your pasta order amount is:",self.price2)
                    
                elif self.quantity_pasta==3:
                    self.price2=self.quantity_pasta*9.5
                    print("Your pasta order amount is:",self.price2)
                    
                elif self.quantity_pasta>=4:
                    self.price2=self.quantity_pasta*9.5
                    print("Your pasta order amount is:",self.price2)
                        
                    total_quantity=self.quantity_pasta
                    print(f" Quantity of pasta is {self.quantity_pasta} ***CONGRATULATIONS!!!!get {self.bruschetta} BRUSCHETTA free ")
                        
                else:
                    print(" Invalid Quantity ")
                
            elif choice==0:
                if self.quantity_pasta>=4 and self.quantity_pizza>=4:
                    print(f" Quantity of pasta is {self.quantity_pasta} and Quantity of pizza is {self.quantity_pizza} ***CONGRATULATIONS!!!!get  {self.chocobrowni} CHOCOBROWNI free")
                    total_quantity = self.quantity_pasta+self.quantity_pizza+self.colddrink+self.bruschetta+self.chocobrowni
                    print(f" Quantity of pasta is {self.quantity_pasta},\nQuantity of pizza is {self.quantity_pizza} and \nQuantity of chocobrwni is {self.chocobrowni}\nQuantity of colddrink is {self.colddrink} \nQuantity of bruschetta is {self.bruschetta}\nTotal quantity is : ", total_quantity)
                    self.price1=10.99*self.quantity_pizza
                    self.price2=self.quantity_pasta*9.5
                    print("Total amount of price is ",self.price1+self.price2)
                else:
                    total_quantity=self.quantity_pasta+self.quantity_pizza
                    print(f" Quantity of pasta is {self.quantity_pasta},\nQuantity of pizza is {self.quantity_pizza} \nTotal quantity is : ", total_quantity)
                    self.price1=10.99*self.quantity_pizza
                    self.price2=9.5*self.quantity_pasta
                    print("Total amount of price is ",self.price1+self.price2)

                
                    # total_price = self.price1+self.price2
                    # print("Total amount is : ",total_price)
                    
            else:
                    print(" Invalid Chioce ")
                
            choice=input("do you want to add more customer???press y for yes and n for no:")
            if choice=='n' or choice=='no':
                    status=False
            
obj=pizza()
obj.inputdetails()
obj.food()
                    

                    



    
        

