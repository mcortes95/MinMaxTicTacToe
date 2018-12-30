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
        
        self.help=tk.Button(self,text="Help",fg="red")
        self.help.pack(side="top")
        
        self.quit=tk.Button(self,text="QUIT",fg="red",command=self.master.destroy)
        self.quit.pack(side="bottom")

    def one_p(self):
        print("Play a 1 player game.")

    def two_p(self):
        print("Play a 2 player game.")

root=tk.Tk()
app=Application(master=root)
app.mainloop()
