import tkinter as tk
import random
def one():
    sqone=tk.Button(frameone,height=10,width=20,bg="green").grid(row=1,column=1)
    x=random.randint(0,9)
def two():
    sqtwo=tk.Button(frameone,height=10,width=20,bg="green").grid(row=1,column=2)
    x=random.randint(0,9)
def three():
    sqthree=tk.Button(frameone,height=10,width=20,bg="green").grid(row=1,column=3)
    x=random.randint(0,9)
def four():
    sqfour=tk.Button(frameone,height=10,width=20,bg="green").grid(row=2,column=1)
    x=random.randint(0,9)
def five():
    sqfive=tk.Button(frameone,height=10,width=20,bg="green").grid(row=2,column=2)
    x=random.randint(0,9)
def six():
    sqsix=tk.Button(frameone,height=10,width=20,bg="green").grid(row=2,column=3)
    x=random.randint(0,9)
def seven():
    sqseven=tk.Button(frameone,height=10,width=20,bg="green").grid(row=3,column=1)
    x=random.randint(0,9)
def eight():
    sqeight=tk.Button(frameone,height=10,width=20,bg="green").grid(row=3,column=2)
    x=random.randint(0,9)
def nine():
    sqnine=tk.Button(frameone,height=10,width=20,bg="green").grid(row=3,column=3)
    x=random.randint(0,9)
root=tk.Tk()
frameone=tk.Frame(root,bg="gray")
frameone.pack(fill="both",expand="true")
labone=tk.Label(frameone,text="TIC TAC TOE",font="LARGE_FONT",fg="white",bg="gray")
labone.grid(row=0,column=2)
sqone=tk.Button(frameone,height=10,width=20,command=one).grid(row=1,column=1)
sqtwo=tk.Button(frameone,height=10,width=20,command=two).grid(row=1,column=2)
sqthree=tk.Button(frameone,height=10,width=20,command=three).grid(row=1,column=3)
sqfour=tk.Button(frameone,height=10,width=20,command=four).grid(row=2,column=1)
sqfive=tk.Button(frameone,height=10,width=20,command=five).grid(row=2,column=2)
sqsix=tk.Button(frameone,height=10,width=20,command=six).grid(row=2,column=3)
sqseven=tk.Button(frameone,height=10,width=20,command=seven).grid(row=3,column=1)
sqeight=tk.Button(frameone,height=10,width=20,command=eight).grid(row=3,column=2)
sqnine=tk.Button(frameone,height=10,width=20,command=nine).grid(row=3,column=3)
root.mainloop()
