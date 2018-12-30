import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        label1 = tk.Label(self,text="Tik Tac Toe",fg="blue")
        label1.pack()
        
        self.one_player=tk.Button(self,text="1 Player",fg="green", command=self.one_p)
        self.one_player.pack(side="top")
        
        self.two_player=tk.Button(self,text="2 Player",fg="green", command=self.two_p)
        self.two_player.pack(side="top")
        
        self.help=tk.Button(self,text="Help",fg="red",command=self.help_btn)
        self.help.pack(side="top")
        
        self.quit=tk.Button(self,text="QUIT",fg="red",command=self.master.destroy)
        self.quit.pack(side="bottom")

    def one_p(self):
        print("Play a 1 player game.")
        

    def two_p(self):
        print("Play a 2 player game.")
    def help_btn(self):
        self.h_button=tk.Button(self,text="HELP")
        self.h_button.pack()

class Page(tk.Frame):
    def __init__(self,*args,**kwargs):
        tk.Frame.__init__(self,*args,**kwargs)
    def show(self):
        self.lift

class Page1(Page):
    def __init__(self,*args,**kwargs):
        Page.__init__(self,*args,**kwargs)
        label=tk.Label(self,text="kk")
        label.pack(side="top",fill="both",expand=True)
        self.create_widgets()
    def add_w(self,n):
        self.new_btn=n
        self.new_btn.pack()
    def create_widgets(self):
        label1 = tk.Label(self,text="Tik Tac Toe",fg="blue")
        label1.pack()
        
        self.one_player=tk.Button(self,text="1 Player",fg="green", command=self.one_p)
        self.one_player.pack(side="top")
        
        self.two_player=tk.Button(self,text="2 Player",fg="green", command=self.show)
        self.two_player.pack(side="top")
        
        self.help=tk.Button(self,text="Help",fg="red",command=self.help_btn)
        self.help.pack(side="top")
        
        self.quit=tk.Button(self,text="QUIT",fg="red",command=self.master.destroy)
        self.quit.pack(side="bottom")

    def one_p(self):
        print("Play a 1 player game.")
        

    def two_p(self):
        print("Play a 2 player game.")
    def help_btn(self):
        self.h_button=tk.Button(self,text="HELP")
        self.h_button.pack()

                
class Page2(Page):
    def __init__(self,*args,**kwargs):
        Page.__init__(self,*args,**kwargs)
        label=tk.Label(self,text="Page 2")
        label.pack(side="top",fill="both",expand=True)

class View(tk.Frame):
    def __init__(self,*args,**kwargs):
        tk.Frame.__init__(self,*args,**kwargs)
        p1=Page1(self)
        p2=Page2(self)
        
        n_b=tk.Button(text="P1",command=p2.lift)
        
        p1.add_w(n_b)
        bf=tk.Frame(self)
        cont=tk.Frame(self)
        bf.pack(side="top",fill="x",expand=False)
        cont.pack(side="top",fill="both",expand=True)

        p1.place(in_=cont,x=0,y=0,relwidth=1,relheight=1)
        p2.place(in_=cont,x=0,y=0,relwidth=1,relheight=1)

        b1=tk.Button(bf,text="P1",command=p1.lift)
        b2=tk.Button(bf,text="P2",command=p2.lift)

        b1.pack(side="left")
        b2.pack(side="right")
        p1.show()

root=tk.Tk()
root.title("Tic Tac Toe")
root.geometry("1000x1000")
app=View(root)
app.pack(side="top",fill="both",expand=True)
#app=Application(master=root)
app.mainloop()
