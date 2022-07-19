"""
#Write a Python program to check if a number is positive, negative or zero.
num=int(input("enter a number:"))

if num > 0:
    print("number is positive")
elif num < 0:
    print("number is negative")
else:
    print("number is 0")    


# Write a Python program to get the Factorial number of given number.


from math import factorial
num=int(input("enter a number:"))
if num < 0:
    print(0)
elif num == 0 or num == 1:
    print(1)
elif num > 1:
    print("factorial number is:",num * factorial(num-1))
else:
    print("not found")

# Write a Python program to get the Fibonacci series of given range.
n=int(input("enter number:"))
a=0
b=1
print(a)
print(b)

if n<0:
    print("invalid number")
elif n==0:
    print(0)
elif n==1 and n==2:
    print(b)
else:
    for n in range (1,n):
        c=a+b
        a=b
        b=c
        print(c)



#Write python program that swap two number with temp variable and without temp variable.
n1=int(input("enter one number:"))
n2=int(input("enter second number:"))
print("value of n1:",n1,"value of n2:",n2)
n1,n2=n2,n1
print("after swapping value of n1:",n1,"value of n2:",n2)

#swap using temp variable
n1=int(input("enter one number:"))
n2=int(input("enter second number:"))
print("value of n1:",n1,"value of n2:",n2)
a=n1
n1=n2
n2=a
print("after swapping value of n1:",n1,"value of n2:",n2)


#Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user.
num=int(input("enter number:"))
if num%2 == 0:
    print("given number is even number")
else:
    print("given number is odd number")


# Write a Python program to test whether a passed letter is a vowel or not.
letter=input("enter alphabet letter:")
if letter == "a" or letter == "e" or letter == "i" or letter =="o" or letter =="u":
    print("alphabet is vowel")
else:
    print("not vowel") 

#Write a Python program to sum of three given integers.However, if two values are equal sum will be zero.
n1=int(input("enter number:"))
n2=int(input("enter number:"))
n3=int(input("enter number:"))

if n1 == n2 or n2==n3 or n1==n3:
    print("sum is 0")
else:
    print("sum of three number is",n1+n2+n3)

#Write a Python program that will return true if the two given integervalues are equal or their sum or difference is 5.
n1=int(input("enter number:"))
n2=int(input("enter number:"))
sum= n1+n2
dif= n1-n2
if n1 == n2 or sum == 5 or dif == 5:
    print("true")
else:
    print("false")


# Write a python program to sum of the first n positive integers.
n = int(input("enter a number:"))
sum=(n*(n+1))/2
print("sum of n integer is",sum)


#Write a Python program to calculate the length of a string.

from posixpath import split


checklength=input("input string:")
print(len(checklength))

# Write a Python program to count the number of characters (character frequency) in a string.
name=input("enter your Fullname:")
for i in name:
    frequency = name.count(i)
    print(str(i) + ": " + str(frequency), end=", ")

# What are negative indexes and why are they used?
#Write a Python program to count occurrences of a substring in a string.
string=input("enter a string:")
i=string.split(",")

for word in i:
     frequency = i.count(word)
     print(str(word) + ": " + str(frequency), end=", ")
      """  
# Write a Python program to count the occurrences of each word in a given sentence.
string=input("enter a string:")
i=string.split()

for word in i:
     frequency = i.count(word)
     print(str(word) + ": " + str(frequency), end=", ")
        
#Write a Python program to get a single string from two given strings,separated by a space and swap the first two characters of each string.
str1=input("enter one string:")
str2=input("enter second string:")
new_str1 = str2[:2] + str1[2:]
new_str2 = str1[:2] + str2[2:]
print(new_str1 + ' ' + new_str2)

'''Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly'
insteadif the string length of the given string is less than 3, leave it
unchanged.'''
str1=input("enter a string:")
length=len(str1)
if length > 2:
    if str1[-3:] == 'ing':
      str1 += 'ly'
      print("adding ly at the end of string:",str1)  
    else:
      str1 += 'ing'
      print("adding ing at the and of string:",str1)
else:
    print("without anything:",str1)
  

'''Write a Python program to find the first appearance of the substring 'not'
and 'poor' from a given string, if 'not' follows the 'poor', replace the whole
'not'...'poor'substring with 'good'. Return the resulting string.'''
str1=input("enter a string:")
#var.find(“search word”)-->to find anything from given string.
snot = str1.find('not')
spoor = str1.find('poor')
  
if spoor > snot and snot>0 and spoor>0:
    #var.replace(,)--> using for replacing string words
    str1 = str1.replace(str1[snot:(spoor+4)], 'good')
    print("after replace with good:",str1)
else:
   print("without replacement:",str1)


#Write a Python function that takes a list of words and returns the length of the longest one.


# Write a Python function to reverses a string if its length is a multiple of 4.

str1=input("enter a string:")

if len(str1) % 4 == 0:
    
    print("after reverseing the string: ",str1[::-1])
else:
    print("without reversing:",str1)    

''' Write a Python program to get a string made of the first 2 and the last 2
chars from a given a string. Ifthe string length islessthan 2,return instead
of the empty string.
o Sample String:w3resource'
o Expected Result: 'w3ce'
o Sample String: 'w3'
o Expected Result: 'w3w3'
o Sample String: ' w'
o Expected Result: Empty String'''

str=input("enter a string:")
if len(str) < 2:
    print("without changes:",str)
else:
    new=str[0:2] + str[-2:]
    print("after:",new)


#Write a Python function to insert a string in the middle of a string.
str1=input("enter one string:")
str2=input("enter second string:")
mid=len(str1)//2
new_str=str1[:mid]+ str2 +str1[mid:]
print("add str2 in the middle of str1:",new_str,'\t')