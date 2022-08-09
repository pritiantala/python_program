import imp
from random import random
import tkinter
from turtle import Screen
import random

screen=tkinter.Tk()
screen.title("ROCK PAPER SCISSOR")
screen.geometry("500x500")

numu=0
numc=0

var_user_choice=tkinter.StringVar()
var_com_choice=tkinter.StringVar()
var_result_choice=tkinter.StringVar()
game_list=["ROCK","PAPER","SCISSOR"]

def myfun(msg):
    var_user_choice.set(msg)
    com=random.choice(game_list)
    var_com_choice.set(com)

    if msg==com:
        var_result_choice.set("TIE")
    else:
        global numc
        global numu
            
        if (msg=="ROCK" and com=="SCISSOR") or (msg=="PAPER" and com=="ROCK") or (msg=="SCISSOR" and com=="PAPER"):
            var_result_choice.set("user won")
            numu+=1
            lbl_name1.config(text=numu)
        else:
            var_result_choice.set("computer won")
            numc+=1
            lbl_name2.config(text=numc)

btn=tkinter.Button(screen,text="ROCK",font=("arial",20,"bold"),bg="blue",fg="white",activebackground="black",activeforeground="white",command=lambda:myfun("ROCK"))
btn.place(x=10,y=10)

btn=tkinter.Button(screen,text="PAPER",font=("arial",20,"bold"),bg="blue",fg="white",activebackground="black",activeforeground="white",command=lambda:myfun("PAPER"))
btn.place(x=150,y=10)

btn=tkinter.Button(screen,text="SCISSOR",font=("arial",20,"bold"),bg="blue",fg="white",activebackground="black",activeforeground="white",command=lambda:myfun("SCISSOR"))
btn.place(x=300,y=10)

user=tkinter.Label(screen,text="USER",font=("arial",14,"bold"))
user.place(x=10,y=150)
lbl_name1=tkinter.Label(screen,text=numu,font=("arial",10,"bold"),bg="grey")
lbl_name1.place(x=300,y=150)

computer=tkinter.Label(screen,text="COMPUTER",font=("arial",14,"bold"))
computer.place(x=10,y=200)
lbl_name2=tkinter.Label(screen,text=numc,font=("arial",10,"bold"),bg="grey")
lbl_name2.place(x=300,y=200)

user=tkinter.Label(screen,textvariable=var_user_choice,font=("arial",14,"bold"),fg="blue")
user.place(x=150,y=150)

computer=tkinter.Label(screen,textvariable=var_com_choice,font=("arial",14,"bold"),fg="green")
computer.place(x=150,y=200)

btn=tkinter.Button(screen,textvariable=var_result_choice,font=("arial",20,"bold"),bg="blue",fg="white",width=25,activebackground="black",activeforeground="white")
btn.place(x=10,y=400)
screen.mainloop()