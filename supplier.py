import sqlite3
from tkinter import *
from tkinter import ttk, messagebox

class SupplierManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Supplier & Product Management")
        self.root.geometry("800x500")
        self.root.config(bg="white")

        # Variables
        self.var_pid = StringVar()
        self.var_supplier = StringVar()
        self.var_category = StringVar()
        self.var_name = StringVar()
        self.var_price = StringVar()
        self.var_qty = StringVar()
        self.var_status = StringVar()

        # Title
        title = Label(self.root, text="Supplier & Product Management", font=("goudy old style", 20, "bold"), bg="#262626", fg="white").pack(side=TOP, fill=X)

        # Form Frame
        form_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        form_frame.place(x=10, y=50, width=380, height=400)

        # Labels & Entries
        Label(form_frame, text="Supplier", font=("times new roman", 15), bg="white").place(x=10, y=20)
        Entry(form_frame, textvariable=self.var_supplier, font=("times new roman", 13), bg="lightyellow").place(x=120, y=20, width=200)

        Label(form_frame, text="Category", font=("times new roman", 15), bg="white").place(x=10, y=60)
        Entry(form_frame, textvariable=self.var_category, font=("times new roman", 13), bg="lightyellow").place(x=120, y=60, width=200)

        Label(form_frame, text="Product Name", font=("times new roman", 15), bg="white").place(x=10, y=100)
        Entry(form_frame, textvariable=self.var_name, font=("times new roman", 13), bg="lightyellow").place(x=120, y=100, width=200)

        Label(form_frame, text="Price", font=("times new roman", 15), bg="white").place(x=10, y=140)
        Entry(form_frame, textvariable=self.var_price, font=("times new roman", 13), bg="lightyellow").place(x=120, y=140, width=200)

        Label(form_frame, text="Quantity", font=("times new roman", 15), bg="white").place(x=10, y=180)
        Entry(form_frame, textvariable=self.var_qty, font=("times new roman", 13), bg="lightyellow").place(x=120, y=180, width=200)

        Label(form_frame, text="Status", font=("times new roman", 15), bg="white").place(x=10, y=220)
        combo_status = ttk.Combobox(form_frame, textvariable=self.var_status, values=("Active", "Inactive"), state="readonly", font=("times new roman", 13))
        combo_status.place(x=120, y=220, width=200)
        combo_status.current(0)

        # Buttons
        btn_frame = Frame(form_frame, bg="white")
        btn_frame.place(x=10, y=260, width=350, height=100)

        Button(btn_frame, text="Add Product", command=self.add_product, bg="green", fg="white", font=("times new roman", 13)).grid(row=0, column=0, padx=5, pady=10)
        Button(btn_frame, text="Update Product", command=self.update_product, bg="blue", fg="white", font=("times new roman", 13)).grid(row=0, column=1, padx=5, pady=10)
        Button(btn_frame, text="Delete Product", command=self.delete_product, bg="red", fg="white", font=("times new roman", 13)).grid(row=1, column=0, padx=5, pady=10)
        Button(btn_frame, text="Clear Fields", command=self.clear_fields, bg="gray", fg="white", font=("times new roman", 13)).grid(row=1, column=1, padx=5, pady=10)

        # Product List Frame
        list_frame = Frame(self.root, bd=2, relief=RIDGE)
        list_frame.place(x=400, y=50, width=380, height=400)

        scroll_y = Scrollbar(list_frame, orient=VERTICAL)
        scroll_x = Scrollbar(list_frame, orient=HORIZONTAL)

        self.product_table = ttk.Treeview(list_frame, columns=("pid", "Supplier", "Category", "Name", "Price", "Qty", "Status"), yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.config(command=self.product_table.yview)
        scroll_x.config(command=self.product_table.xview)

        for col in ("pid", "Supplier", "Category", "Name", "Price", "Qty", "Status"):
            self.product_table.heading(col, text=col)
        self.product_table["show"] = "headings"
        self.product_table.pack(fill=BOTH, expand=1)
        self.product_table.bind("<ButtonRelease-1>", self.get_data)

        self.show_products()

    # ==================== Functions ======================
    def add_product(self):
        if self.var_supplier.get() == "" or self.var_name.get() == "":
            messagebox.showerror("Error", "Supplier and Product Name are required")
            return
        con = sqlite3.connect("ims.db")
        cur = con.cursor()
        try:
            cur.execute("INSERT INTO product (Supplier, Category, Name, Price, Qty, Status) VALUES (?,?,?,?,?,?)",
                        (self.var_supplier.get(), self.var_category.get(), self.var_name.get(),
                         self.var_price.get(), self.var_qty.get(), self.var_status.get()))
            con.commit()
            messagebox.showinfo("Success", "Product added successfully")
            self.show_products()
            self.clear_fields()
        except Exception as e:
            messagebox.showerror("Error", f"Error due to {str(e)}")
        finally:
            con.close()

    def show_products(self):
        con = sqlite3.connect("ims.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT P_Id, Supplier, Category, Name, Price, Qty, Status FROM product")
            rows = cur.fetchall()
            self.product_table.delete(*self.product_table.get_children())
            for row in rows:
                self.product_table.insert("", END, values=row)
        except Exception as e:
            messagebox.showerror("Error", f"Error due to {str(e)}")
        finally:
            con.close()

    def get_data(self, ev):
        f = self.product_table.focus()
        content = self.product_table.item(f)
        row = content["values"]
        if row:
            self.var_pid.set(row[0])
            self.var_supplier.set(row[1])
            self.var_category.set(row[2])
            self.var_name.set(row[3])
            self.var_price.set(row[4])
            self.var_qty.set(row[5])
            self.var_status.set(row[6])

    def update_product(self):
        if self.var_pid.get() == "":
            messagebox.showerror("Error", "Please select a product to update")
            return
        con = sqlite3.connect("ims.db")
        cur = con.cursor()
        try:
            cur.execute("UPDATE product SET Supplier=?, Category=?, Name=?, Price=?, Qty=?, Status=? WHERE P_Id=?",
                        (self.var_supplier.get(), self.var_category.get(), self.var_name.get(),
                         self.var_price.get(), self.var_qty.get(), self.var_status.get(), self.var_pid.get()))
            con.commit()
            messagebox.showinfo("Success", "Product updated successfully")
            self.show_products()
            self.clear_fields()
        except Exception as e:
            messagebox.showerror("Error", f"Error due to {str(e)}")
        finally:
            con.close()

    def delete_product(self):
        if self.var_pid.get() == "":
            messagebox.showerror("Error", "Please select a product to delete")
            return
        op = messagebox.askyesno("Confirm", "Are you sure you want to delete this product?")
        if op:
            con = sqlite3.connect("ims.db")
            cur = con.cursor()
            try:
                cur.execute("DELETE FROM product WHERE P_Id=?", (self.var_pid.get(),))
                con.commit()
                messagebox.showinfo("Deleted", "Product deleted successfully")
                self.show_products()
                self.clear_fields()
            except Exception as e:
                messagebox.showerror("Error", f"Error due to {str(e)}")
            finally:
                con.close()

    def clear_fields(self):
        self.var_pid.set("")
        self.var_supplier.set("")
        self.var_category.set("")
        self.var_name.set("")
        self.var_price.set("")
        self.var_qty.set("")
        self.var_status.set("Active")

# Run the application
if __name__ == "__main__":
    root = Tk()
    obj = SupplierManagement(root)
    root.mainloop()
