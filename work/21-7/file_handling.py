"""
    r= read mode
    w= write mode
    a= append mode
    x= blank file
"""
import os

f=open("C:\\Users\\PRITI\\Documents\\GitHub\\python_program\\21-7\\example.txt","r")
#read file--------------------
#print(f.read())

#2nd example to read line-----------------------------------
#f=open(r"C:\Users\PRITI\Documents\GitHub\python_program\21-7\example.txt","r")
#print(f.read())

#read first line of file--------------------
#print(f.readline())

#store in the list and print specific lines and file length--------
#readlines() auto converting file into list
l1=f.readlines()
print("---->",l1)

print("no of lines in file:",len(l1))
print("3rd line in file:",l1[2])
print("last line in file:",l1[-1])
