import tkinter
from turtle import color


screen= tkinter.Tk()

# w x h
screen.geometry("500x500")
screen.configure(bg="grey")

#tkinter variable
var_ename_id=tkinter.StringVar() #IT WILL TAKE VALUE UN STRING

def myfun():
    print("WELCOME")
    print("VALUE FROM ENTRY:",var_ename_id.get())

#label
lbl=tkinter.Label(screen,text="WELCOME TO TKINTER",font=("arial",26,"bold","underline"),bg="grey",fg="red")
lbl.place(x=50,y=10)

#label for name
lbl_name=tkinter.Label(screen,text="Enter name:",font=("arial",10,"bold"),bg="grey")
lbl_name.place(x=20,y=80)

# entry\
e1=tkinter.Entry(screen,textvariable=var_ename_id)
e1.place(x=130,y=80)

# button

btn=tkinter.Button(screen,text="Submit",font=("arial",10,"bold"),command=myfun)
btn.place(x=280,y=80)

screen.mainloop()

