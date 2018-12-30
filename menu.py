import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.one_player=tk.Button(self,text="1 Player", command=self.one_p)
        self.one_player.pack(side="top")
        self.two_player=tk.Button(self,text="2 Player",command=self.two_p)
        self.two_player.pack()
        self.quit=tk.Button(self,text="QUIT",fg="red",command=self.master.destroy)
        self.quit.pack(side="bottom")

    def one_p(self):
        print("Play a 1 player game.")

    def two_p(self):
        print("Play a 2 player game.")

root=tk.Tk()
app=Application(master=root)
app.mainloop()
