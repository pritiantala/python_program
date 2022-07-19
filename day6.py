#task 23-6-22
#validation in email and password

import email


firstName = "Priti"
Email="pritiantala@gmail.com"
Password="12345678"

userEmail=input("enter your email:")
userPasword=input("enter your Password:")

if userEmail==Email and userPasword==Password:
    print("hello!!:",firstName)
elif userEmail!=Email and userPasword==Password:
    print("invalid email")
elif userEmail==Email and len(userPasword)!=8:
    print("WARNNING:password length must be 8 character!!!!")
elif userEmail==Email and userPasword!=Password:
    print("invalid password")
else:
    print("invalid user")
