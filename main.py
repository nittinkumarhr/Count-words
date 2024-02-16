from tkinter import *
from tkinter import ttk
from tkinter import Tk, Label,messagebox
from PIL import Image, ImageTk
import random


class RMS :
    def __init__(self,root):
        self.root = root
        self.root.geometry("300x300")
        self.root.title("Words Counter")
        self.root.configure(highlightbackground="black")
        self.root.configure(highlightcolor="black")
        self.root.geometry("900x550+0+0")
        self.root.resizable(False,False)
        self.root.focus_force()
        
        
        #---------------------------image content=================================================
        #image background ++++++++++++++++++++++++++++++++++++++
        self.bg_image1 = ImageTk.PhotoImage(file="/home/nitin/Word Counter/back_re.jpg")
        self.bg_lb1 = Label(self.root, image=self.bg_image1,bg='black')
        self.bg_lb1.place(x=0,y=0,width=900,relheight=1)
        
        #===============title==========================================
        l={"Red","Violet","MediumSlateBlue","Lime","Blue","Fuchsia","LimeGreen","DarkGoldenrod","DarkSlateGray"}
        for i in l:
            self.title=Label(self.root,text="Count the words",font=("times new roman",25,"bold"),fg=i,bg='black')
            self.title.place(x=350,y=10)
        #NOTE - +++++++++++++++++++++++++Level++++++++++++++++++++++++++++++++++++++++++++    
        lb_String=Label(self.root,text="Enter String",font=("goudy old style",15,"bold"),bg="black",fg="white")
        lb_String.place(x=270,y=185)
        
        total_lb=Label(self.root,text="Total Words :)",font=("goudy old style",15,"bold"),bg="black",fg="white")
        total_lb.place(x=240,y=300)
        
        total2_lb=Label(self.root,text="Total Repeat Words :)",font=("goudy old style",15,"bold"),bg="black",fg="white")
        total2_lb.place(x=420,y=300)
        
        #====variables==================================================================================
        self.var_string=StringVar()
        
        #==================Entry=========================================================
        self.entry_string=Entry(self.root,textvariable=self.var_string,font=("goudy old style",15,"bold"),bg="black")
        self.entry_string.bind("<FocusIn>",lambda e: self.entry_string.configure(background="white",fg="black"))
        self.entry_string.bind("<FocusOut>",lambda e: self.entry_string.configure(background="black",fg="white"))
        self.entry_string.place(x=420,y=185,width=225)
        
        #================Button================================================
        
        self.bt_change=Button(self.root,text="Count World",bg="black",fg='RoyalBlue',font=("times new roman",15),bd=0,cursor="hand2",justify=CENTER,activebackground="RoyalBlue",activeforeground="black",command=self.check_string)
        #self.bt_change.bind("<Leave>",lambda e: self.bt_change.place(x=540,y=348))
        self.bt_change.place(x=460,y=235)
    
    def check_string(self):
        if self.var_string.get()=="" :
            messagebox.showerror("Error","Column is Empty  Please Enter the Something",parent=self.root)
        else:
            data=self.var_string.get()
            l=data.replace(","or '@' or '$'," ").split()
            
            total_words=len(l)
            
            list2 = len(list(set(l)))
            
            #====================================Data in the showing the GUI---------------------------------------- 
            
            total_lb=Label(self.root,text=total_words,font=("goudy old style",15,"bold"),bg="black",fg="white")
            total_lb.place(x=390,y=300)
            
            total2_lb=Label(self.root,text=list2,font=("goudy old style",15,"bold"),bg="black",fg="white")
            total2_lb.place(x=650,y=300)
            
            self.entry_string.delete(0,END)
            
            



if __name__ == "__main__":
    ob = Tk()
    obj = RMS(ob)
    ob.mainloop()
