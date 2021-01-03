import tkinter as tk
from tkinter import messagebox
def HaCk():
    vs=tk.Tk()
    img1=tk.PhotoImage(file='bug1.png')
    vs.iconphoto(False, img1)
    def show():
            run=True
            while run:
                messagebox.showerror('Virus Found!!!!!','Your computer has been hacked! "')
    vs.title('Hello From Darkweb!')
    vs.minsize(500,500)
    vs.maxsize(500,500)
    vs.configure(bg='black')
    img=tk.PhotoImage(file='virus1.png')
    label=tk.Label(vs, image=img,border=0).pack()  
    show()
    vs.mainloop()
HaCk()