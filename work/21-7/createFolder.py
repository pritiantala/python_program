#create new folder in given path

import os

if os.path.exists(r"C:\Users\PRITI\Documents\GitHub\python_program\work\21-7\MYFOLDER"):
    print("folder already exist")
else:
    os.mkdir(r"C:\Users\PRITI\Documents\GitHub\python_program\work\21-7\MYFOLDER")
    print("created folder")