import tkinter as tk

def one():
    if b:
        sqone=tk.Button(frameone,height=10,width=20,bg="green").grid(row=1,column=1)
    else:
        sqone=tk.Button(frameone,height=10,width=20,bg="red").grid(row=1,column=1)
    print("00")
def two():
    if b:
        sqtwo=tk.Button(frameone,height=10,width=20,bg="green").grid(row=1,column=1)
    else:
        sqtwo=tk.Button(frameone,height=10,width=20,bg="red").grid(row=1,column=1)
    print("10")
def three():
    if b:
        sqthree=tk.Button(frameone,height=10,width=20,bg="green").grid(row=1,column=1)
    else:
        sqthree=tk.Button(frameone,height=10,width=20,bg="red").grid(row=1,column=1)
    print("10")
def four():
    if b:
        sqfour=tk.Button(frameone,height=10,width=20,bg="green").grid(row=1,column=1)
    else:
        sqfour=tk.Button(frameone,height=10,width=20,bg="red").grid(row=1,column=1)
    print("01")
def five():
    if b:
        sqfive=tk.Button(frameone,height=10,width=20,bg="green").grid(row=1,column=1)
    else:
        sqfive=tk.Button(frameone,height=10,width=20,bg="red").grid(row=1,column=1)
    print("11")
def six():
    if b:
        sqsix=tk.Button(frameone,height=10,width=20,bg="green").grid(row=1,column=1)
    else:
        sqsix=tk.Button(frameone,height=10,width=20,bg="red").grid(row=1,column=1)
    print("21")
def seven():
    if b:
        sqseven=tk.Button(frameone,height=10,width=20,bg="green").grid(row=1,column=1)
    else:
        sqseven=tk.Button(frameone,height=10,width=20,bg="red").grid(row=1,column=1)
    print("02")
def eight():
    if b:
        sqeight=tk.Button(frameone,height=10,width=20,bg="green").grid(row=1,column=1)
    else:
        sqeight=tk.Button(frameone,height=10,width=20,bg="red").grid(row=1,column=1)
    print("12")
def nine():
    if b:
        sqnine=tk.Button(frameone,height=10,width=20,bg="green").grid(row=1,column=1)
    else:
        sqnine=tk.Button(frameone,height=10,width=20,bg="red").grid(row=1,column=1)
    print("22")

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
