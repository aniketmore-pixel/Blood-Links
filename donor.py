from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
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
        btn_search=Button(SearchFrame,text="Search",font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=410,y=9,width=150,height=30)

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
        txt_dob=Entry(self.root,textvariable=self.var_donor_id,font=("goudy old style",15),bg="lightyellow").place(x=500,y=190,width=180)
        txt_dod=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="lightyellow").place(x=850,y=190,width=180)

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
        btn_add=Button(self.root,text="Save",font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=750,y=270,width=130,height=30)
        btn_update=Button(self.root,text="Update",font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=900,y=270,width=130,height=30)
        btn_delete=Button(self.root,text="Delete",font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=750,y=305,width=130,height=30)
        btn_clear=Button(self.root,text="Clear",font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=900,y=305,width=130,height=30)

        #===Donor Details====

        don_frame=Frame(self.root,bd=3,relief=RIDGE)
        don_frame.place(x=0,y=350,relwidth=1,height=150)

        scrolly=Scrollbar(don_frame,orient=VERTICAL)
        scrollx=Scrollbar(don_frame,orient=HORIZONTAL)

        self.DonorTable=ttk.Treeview(don_frame,columns=("Do_id","name","email","gender","contact","dob","dod","Bld_grp","address","location"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)####database mai jayga
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=BOTTOM,fill=Y)
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


        



if __name__=="__main__":
    root=Tk()
    obj=donorClass(root)
    root.mainloop() 