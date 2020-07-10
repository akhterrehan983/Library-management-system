import sys
from tkinter import *
from tkinter import messagebox
import pickle
class Adm_login:
    rt=None
    def check(self):
        with open('admin_pass.pkl','rb') as f:
            obj=pickle.load(f)
            if(self.entry2.get()==obj['password']):
                messagebox.showinfo("MATCHED",icon="info")
                Adm_login.rt=self.root
                #self.root.destroy()
                return 1
            else:
                messagebox.showinfo("WRONG",icon="warning")
                self.root.destroy()
                return 0
    def login(self):
        root=Tk()
        root.title("GUI PRACTICE")
        root.geometry("500x300")
        lb=Label(root,text="Admin Login",font=('Arial',12,'bold'),fg="steel blue",bd=20,anchor='w')
        lb.grid(row=0,column=2)
        # fr=Frame(root,width=100,heigh=100,text="ADMIN LOGIN")
        name=Label(root,text="Name",font=('arial',10,'bold'))
        password=Label(root,text="password",font=('arial',10,'bold'))
        self.entry1=Entry(root)
        self.entry2=Entry(root)

        name.grid(row=1,column=0,stick=E)
        password.grid(row=2,column=0,stick=E)

        self.entry1.grid(row=1,column=1)
        self.entry2.grid(row=2,column=1)
        submit=Button(root,text="SUBMIT",fg="blue",bg="powder blue",command=self.check)
        submit.grid(row=3,column=1)
        self.root=root
        root.mainloop()
