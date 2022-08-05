class productClass:
    """"
    __init__ work as a constructor
    it automatically call when object of class create
    
    def __init__(self):
        print("welcome to product panel")
        self.mobile=5000
        self.__laptop=45000     #diclare private

    def display(self):
        print("mobile=",self.mobile)
        print("laptop=",self.__laptop)

    def updatePrice(self,newLaptopPrice):
        self.__laptop = newLaptopPrice  #update laptop price
"""

    def __init__(self):
        self.mobile=1000
        self.laptop=15000

    def setMobile(self,price):
        self.mobile=price

    def setLaptop(self,price):
        self.laptop=price
    