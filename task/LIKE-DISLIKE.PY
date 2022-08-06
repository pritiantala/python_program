from cgitb import text
from distutils.command.config import config
from logging import root
import tkinter
from turtle import color

screen= tkinter.Tk()

numl=0
numd=0

# w x h
screen.geometry("500x500")
screen.configure(bg="grey")

#tkinter variable
var_ename_id=tkinter.StringVar()   #IT WILL TAKE VALUE UN STRING

def like():
    print("WELCOME")
    print("VALUE FROM LIKE ENTRY:",var_ename_id.get())
    global numl
    numl+=1
    lbl_name1.config(text=numl)
def Dlike():
    print("WELCOME")
    print("VALUE FROM DIS-LIKE ENTRY:",var_ename_id.get())
    global numd
    numd+=1
    lbl_name2.config(text=numd)

#label
lbl=tkinter.Label(screen,text="WELCOME TO TKINTER",font=("arial",26,"bold","underline"),bg="grey",fg="red")
lbl.place(x=50,y=10)

# entry\
e1=tkinter.Entry(screen,textvariable=var_ename_id)
e1.place(x=130,y=80)

# button
btn=tkinter.Button(screen,text="like",font=("arial",10,"bold"),command=like)
btn.place(x=130,y=120)

btn=tkinter.Button(screen,text="Dis-like",font=("arial",10,"bold"),command=Dlike)
btn.place(x=200,y=120)

#label for name
lbl_name1=tkinter.Label(screen,text=numl,font=("arial",10,"bold"),bg="grey")
lbl_name1.place(x=130,y=180)
lbl_name2=tkinter.Label(screen,text=numd,font=("arial",10,"bold"),bg="grey")
lbl_name2.place(x=200,y=180)

screen.mainloop()

