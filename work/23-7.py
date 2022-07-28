
# exception handling using try and except
"""try:
    print(a)
except:
    print("invalid input")
"""
#ex 2 try-except

try:
    num1=int(input("enter a number:"))
    num2=int(input("enter a number:"))

    ans=num1/num2
    print(ans)
except ZeroDivisionError:
    print("make sure entered number is grater than 0")
except:
    print("invalid input")


#ex 3 try-except-else-finally

try:
    num1=int(input("enter a number:"))
    num2=int(input("enter a number:"))

    ans=num1/num2
   
except ZeroDivisionError:
    print("make sure entered number is grater than 0")
except:
    print("invalid input")
else:
    print(ans)
finally:
    print("THANK YOU FOR USING THIS APLLICATION")

