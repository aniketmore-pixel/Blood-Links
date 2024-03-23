import os
import time
from tkinter import*
from tkinter import ttk, messagebox
from PIL import Image,ImageTk
from donor import donorClass
from hospital import hospitalClass
from category import BloodGroupWindow
from product import productClass
from sales import salesClass
import sqlite3
from tkinter import messagebox
import os
import time

import sqlite3
class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Blood Bank Management System")
        self.root.config(bg="white")

        #====title===
        self.icon_title=ImageTk.PhotoImage(file="images/logo1.jpg")
        title=Label(self.root,text="BLOOD LINKS",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="white",fg="#7a0a0a",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)#bloodLnks title background color

        #===btn_logout===
        btn_logout=Button(self.root,text="Logout",font=("times new roman",15,"bold"),bg="#cdb3ba",cursor="hand2",fg="#7a0a0a").place(x=1150,y=10,height=50,width=150)

        #===clock===
        self.lbl_clock=Label(self.root,text="Welcome to BLOOD LINKS\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",15),bg="#cdb3ba",fg="#7a0a0a")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        #===Left Menu===
        self.MenuLogo=Image.open("images/menu.jpeg")
        self.MenuLogo = self.MenuLogo.resize((200, 200))
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=102,width=200,height=565)

        lbl_menuLogo=Label(LeftMenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)

        self.icon_side=ImageTk.PhotoImage(file="images/side.png")

        lbl_menu=Label(LeftMenu,text="Menu",font=("times new roman",20),bg="#cdb3ba",fg="#7a0a0a").pack(side=TOP,fill=X)

        btn_employee=Button(LeftMenu,text="Donor",command=self.donor,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2",fg="#7a0a0a").pack(side=TOP,fill=X)
        btn_supplier=Button(LeftMenu,text="Hospitals",command=self.hospital,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2",fg="#7a0a0a").pack(side=TOP,fill=X)
        btn_category=Button(LeftMenu,text="Blood Grp",command=self.category,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2",fg="#7a0a0a").pack(side=TOP,fill=X)
        btn_product=Button(LeftMenu,text="Product",command=self.product,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2",fg="#7a0a0a").pack(side=TOP,fill=X)
        btn_sales=Button(LeftMenu,text="Sales",command=self.sales,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2",fg="#7a0a0a").pack(side=TOP,fill=X)
        btn_exit=Button(LeftMenu,text="Exit",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2",fg="#7a0a0a").pack(side=TOP,fill=X)

         #===content===
        self.lbl_employee=Label(self.root,text="Total Employee\n[ 0 ]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_employee.place(x=300,y=120,height=150,width=300)

        self.lbl_supplier=Label(self.root,text="Total Supplier\n[ 0 ]",bd=5,relief=RIDGE,bg="#ff5722",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_supplier.place(x=650,y=120,height=150,width=300)

        self.lbl_category=Label(self.root,text="Total Category\n[ 0 ]",bd=5,relief=RIDGE,bg="#009688",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_category.place(x=1000,y=120,height=150,width=300)

        self.lbl_product=Label(self.root,text="Total Product\n[ 0 ]",bd=5,relief=RIDGE,bg="#607d8b",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_product.place(x=500,y=300,height=150,width=300)

        self.lbl_sales=Label(self.root,text="Total Sales\n[ 0 ]",bd=5,relief=RIDGE,bg="#ffc187",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_sales.place(x=850,y=300,height=150,width=300)


        #===footer===
        lbl_footer=Label(self.root,text="Blood Bank Management System",font=("times new roman",20),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)
        self.update_content()

#=============================================================================================================================================================

        lbl_footer=Label(self.root,text="Blood Bank Management System",font=("times new roman",20),bg="#cdb3ba",fg="#7a0a0a").pack(side=BOTTOM,fill=X)
        self.update_content()
        
    def donor(self):
        self.new_win=Toplevel(self.root) 
        self.new_obj=donorClass(self.new_win) 

    def hospital(self):
        self.new_win=Toplevel(self.root) 
        self.new_obj=hospitalClass(self.new_win)  
       
    def category(self):
        self.new_win=Toplevel(self.root)
        #self.new_obj=categoryClass(self.new_win)
        self.new_obj=BloodGroupWindow(self.new_win)
        
        
    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win)

    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesClass(self.new_win)

    def update_content(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM product")
            product = cur.fetchall()
            self.lbl_product.config(text=f'Total Products\n[ {str(len(product))} ]')

            cur.execute("SELECT * FROM hospital")
            supplier = cur.fetchall()
            self.lbl_supplier.config(text=f'Total Hospitals\n[ {str(len(supplier))} ]')

            cur.execute("SELECT * FROM category")
            category = cur.fetchall()
            self.lbl_category.config(text=f'Total Categories\n[ {str(len(category))} ]')

            cur.execute("SELECT * FROM donor")
            donor = cur.fetchall()
            self.lbl_employee.config(text=f'Total Donors\n[ {str(len(donor))} ]')
            
            bill = len(os.listdir('bill'))
            self.lbl_sales.config(text=f'Total Sales [{str(bill)}]')

            time_ = time.strftime("%I:%M:%S")
            date_ = time.strftime("%d-%m-%Y")
            self.lbl_clock.config(text=f"Welcome to BLOOD LINKS\t\t Date: {str(date_)}\t\t Time: {str(time_)}")
            self.lbl_clock.after(200,self.update_content)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


root=Tk()
obj=IMS(root)
root.mainloop() 

