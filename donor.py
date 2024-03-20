from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class donorClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Blood Bank Management System")
        self.root.config(bg="white")
        self.root.focus_force()
        #==================
        #All Variables=====
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.var_donor_id=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()
        self.var_dob=StringVar()
        self.var_dod=StringVar()
        self.var_email=StringVar()
        self.var_location=StringVar()
        self.var_bldgrp=StringVar()


        #===Search====
        SearchFrame=LabelFrame(self.root,text="Search Donor",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=250,y=20,width=600,height=70)

        #====options===
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Location","Blood Grp","Contact"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=410,y=9,width=150,height=30)

        #====title=====
        title=Label(self.root,text="Donor Details",font=("goudy old style",15),bg="#0f4d7d",fg="white").place(x=50,y=100,width=1000)

        #=====content=====
        #===row1===
        lbl_donid=Label(self.root,text="Don ID",font=("goudy old style",15),bg="white").place(x=50,y=150)
        lbl_gender=Label(self.root,text="Gender",font=("goudy old style",15),bg="white").place(x=350,y=150)
        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15),bg="white").place(x=750,y=150)

        txt_donid=Entry(self.root,textvariable=self.var_donor_id,font=("goudy old style",15),bg="lightyellow").place(x=150,y=150,width=180)
        cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female","Other"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_gender.place(x=500,y=150,width=180)
        cmb_gender.current(0)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="lightyellow").place(x=850,y=150,width=180)

        #===row2===
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15),bg="white").place(x=50,y=190)
        lbl_dob=Label(self.root,text="D.O.B",font=("goudy old style",15),bg="white").place(x=350,y=190)
        lbl_dod=Label(self.root,text="D.O.D",font=("goudy old style",15),bg="white").place(x=750,y=190)

        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=150,y=190,width=180)
        txt_dob=Entry(self.root,textvariable=self.var_dob,font=("goudy old style",15),bg="lightyellow").place(x=500,y=190,width=180)
        txt_dod=Entry(self.root,textvariable=self.var_dod,font=("goudy old style",15),bg="lightyellow").place(x=850,y=190,width=180)

        #===row3===
        lbl_email=Label(self.root,text="Email",font=("goudy old style",15),bg="white").place(x=50,y=230)
        lbl_bldgrp=Label(self.root,text="Blood Grp",font=("goudy old style",15),bg="white").place(x=750,y=230)
        lbl_location=Label(self.root,text="Location",font=("goudy old style",15),bg="white").place(x=350,y=230)
        
        txt_email=Entry(self.root,textvariable=self.var_email,font=("goudy old style",15),bg="lightyellow").place(x=150,y=230,width=180)
        cmb_bldgrp=ttk.Combobox(self.root,textvariable=self.var_bldgrp,values=("Select","A+","A-","B+","B-","AB+","AB-","O+","O-"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_bldgrp.place(x=850,y=230,width=180)
        cmb_bldgrp.current(0)
        txt_location=Entry(self.root,textvariable=self.var_location,font=("goudy old style",15),bg="lightyellow").place(x=500,y=230,width=180)

         #===row4===
        lbl_address=Label(self.root,text="Address",font=("goudy old style",15),bg="white").place(x=50,y=270)
        
        self.txt_address=Text(self.root,font=("goudy old style",15),bg="lightyellow")
        self.txt_address.place(x=150,y=270,width=530,height=65)

        #===button===
        btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=750,y=270,width=130,height=30)
        btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=900,y=270,width=130,height=30)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=750,y=305,width=130,height=30)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=900,y=305,width=130,height=30)

        #===Donor Details====

        don_frame=Frame(self.root,bd=3,relief=RIDGE)
        don_frame.place(x=0,y=350,relwidth=1,height=150)

        scrollx=Scrollbar(don_frame,orient=HORIZONTAL)
        scrolly=Scrollbar(don_frame,orient=VERTICAL)
        

        self.DonorTable=ttk.Treeview(don_frame,columns=("Do_id","name","email","gender","contact","dob","dod","Bld_grp","address","location"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)####database mai jayga
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.DonorTable.xview)
        scrolly.config(command=self.DonorTable.yview)

        self.DonorTable.heading("Do_id",text="Don_Id")
        self.DonorTable.heading("name",text="Name")
        self.DonorTable.heading("email",text="Email")
        self.DonorTable.heading("gender",text="Gender")
        self.DonorTable.heading("contact",text="Contact")
        self.DonorTable.heading("dob",text="DOB")
        self.DonorTable.heading("dod",text="DOD")
        self.DonorTable.heading("Bld_grp",text="Bld_grp")
        self.DonorTable.heading("address",text="Address")
        self.DonorTable.heading("location",text="Location")

        self.DonorTable["show"]="headings"

        self.DonorTable.column("Do_id",width=90)
        self.DonorTable.column("name",width=100)
        self.DonorTable.column("email",width=100)
        self.DonorTable.column("gender",width=100)
        self.DonorTable.column("contact",width=100)
        self.DonorTable.column("dob",width=100)
        self.DonorTable.column("dod",width=100)
        self.DonorTable.column("Bld_grp",width=100)
        self.DonorTable.column("address",width=100)
        self.DonorTable.column("location",width=100)

        self.DonorTable.pack(fill=BOTH,expand=1)
        self.DonorTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()

#==============================================================
        
    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_donor_id.get()=="":
                messagebox.showerror("Error","Donor ID must be required",parent=self.root)
            else:
                cur.execute("Select * from donor where Do_id=?",(self.var_donor_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Donor ID already assigned, try different",parent=self.root)
                else:
                    cur.execute("Insert into donor (Do_id,name,email,gender,contact,dob,dod,Bld_grp,address,location) values(?,?,?,?,?,?,?,?,?,?)",(
                                      self.var_donor_id.get(),
                                      self.var_name.get(),
                                      self.var_email.get(),
                                      self.var_gender.get(),
                                      self.var_contact.get(),
                                      self.var_dob.get(),
                                      self.var_dod.get(),
                                      self.var_bldgrp.get(),
                                      self.txt_address.get('1.0',END),
                                      self.var_location.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Donor Added Successfully",parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from donor")
            rows=cur.fetchall()
            self.DonorTable.delete(*self.DonorTable.get_children())
            for row in rows:
                self.DonorTable.insert('',END,values=row)


            self.DonorTable.delete(*self.DonorTable.get_children())
            for row in rows:
                self.DonorTable.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
            
   


        
    def get_data(self,ev):
        f=self.DonorTable.focus()
        content=(self.DonorTable.item(f))
        row=content['values']
        #print(row)
        self.var_donor_id.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_contact.set(row[4])
        self.var_dob.set(row[5])
        self.var_dod.set(row[6])
        self.var_bldgrp.set(row[7])
        self.txt_address.delete('1.0',END)
        self.txt_address.insert(END,row[8])
        self.var_location.set(row[9])

    
    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_donor_id.get()=="":
                messagebox.showerror("Error","Donor ID must be required",parent=self.root)
            else:
                cur.execute("Select * from donor where Do_id=?",(self.var_donor_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Donor Id",parent=self.root)
                else:
                    cur.execute("Update donor set name=?,email=?,gender=?,contact=?,dob=?,dod=?,Bld_grp=?,address=?,location=? where Do_id=?",(
                                      
                                      self.var_name.get(),
                                      self.var_email.get(),
                                      self.var_gender.get(),
                                      self.var_contact.get(),
                                      self.var_dob.get(),
                                      self.var_dod.get(),
                                      self.var_bldgrp.get(),
                                      self.txt_address.get('1.0',END),
                                      self.var_location.get(),
                                      self.var_donor_id.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Donor Updated Successfully",parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_donor_id.get() == "":
                messagebox.showerror("Error", "Donor ID must be required", parent=self.root)
            else:
                op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                if op:
                    cur.execute("DELETE FROM donor WHERE Do_id=?", (self.var_donor_id.get(),))
                    con.commit()
                    messagebox.showinfo("Delete", "Donor deleted successfully", parent=self.root)
                    self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)


    def clear(self):
        self.var_donor_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_contact.set("")
        self.var_dob.set("")
        self.var_dod.set("")
        self.var_bldgrp.set("Select")
        self.txt_address.delete("1.0",END)
        self.var_location.set("")
        self.var_searchtxt.set("")
        self.var_searchby.set("")
        self.show()

        
    # def search(self):
    #     con=sqlite3.connect(database=r'ims.db')
    #     cur=con.cursor()
    #     try:
    #         if self.var_searchby.get()=="Select":
    #           messagebox.showerror("Error","Select Search by option",parent=self.root)
    #         elif self.var_searchtxt.get()=="":
    #           messagebox.showerror("Error","Search input should be required",parent=self.root)
    #         else:
    #           cur.execute("Select * from donor where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
    #           rows=cur.fetchall()
    #           if len(rows)!=0:
    #              self.DonorTable.delete(*self.DonorTable.get_children())
    #              for row in rows:
    #                self.DonorTable.insert('', END, values=row)
    #           else:
    #               messagebox.showerror("Error","No record found!",parent=self.root)


    #         self.DonorTable.delete(*self.DonorTable.get_children())
    #         for row in rows:
    #             self.DonorTable.insert('',END,values=row)

    #     except Exception as ex:
    #         messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
        
    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            search_by = self.var_searchby.get()
            search_txt = self.var_searchtxt.get()

            if search_by == "Select":
                messagebox.showerror("Error", "Select Search by option", parent=self.root)
            elif search_txt == "":
                messagebox.showerror("Error", "Search input should be required", parent=self.root)
            else:
                if search_by == "Location":
                    cur.execute("SELECT * FROM donor WHERE location LIKE '%" + search_txt + "%'")
                elif search_by == "Blood Grp":
                    cur.execute("SELECT * FROM donor WHERE Bld_grp LIKE '%" + search_txt + "%'")
                elif search_by == "Contact":
                    cur.execute("SELECT * FROM donor WHERE contact LIKE '%" + search_txt + "%'")

            rows = cur.fetchall()
            if len(rows) != 0:
                self.DonorTable.delete(*self.DonorTable.get_children())
                for row in rows:
                    self.DonorTable.insert('', END, values=row)
            else:
                messagebox.showerror("Error", "No record found!", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)


if __name__=="__main__":
    root=Tk()
    obj=donorClass(root)
    root.mainloop() 