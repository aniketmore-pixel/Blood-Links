import tkinter as tk
from tkinter import ttk, Scrollbar, messagebox
import sqlite3
from datetime import datetime, timedelta

class productClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Eligible Donors")
        self.root.geometry("1100x500+220+130")

        scrollx = ttk.Scrollbar(root, orient="horizontal")
        scrolly = ttk.Scrollbar(root, orient="vertical")

        # Create Treeview to display eligible donors
        self.tree = ttk.Treeview(
            self.root,
            columns=( "Name", "Email", "Gender", "Contact", "DOB", "DOD", "Bld_grp", "Address", "Location"),
            yscrollcommand=scrolly.set,
            xscrollcommand=scrollx.set
        )
        scrollx.pack(side="bottom", fill="x")
        scrolly.pack(side="right", fill="y")
        scrollx.config(command=self.tree.xview)
        scrolly.config(command=self.tree.yview)

        #self.tree.heading("Patient Name", text="Patient Name")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Gender", text="Gender")
        self.tree.heading("Contact", text="Contact")
        self.tree.heading("DOB", text="DOB")
        self.tree.heading("DOD", text="DOD")
        self.tree.heading("Bld_grp", text="Blood Group")
        self.tree.heading("Address", text="Address")
        self.tree.heading("Location", text="Location")

        self.tree["show"] = "headings"

        #self.tree.column("Patient Name", width=100)
        self.tree.column("Name", width=100)
        self.tree.column("Email", width=100)
        self.tree.column("Gender", width=100)
        self.tree.column("Contact", width=100)
        self.tree.column("DOB", width=100)
        self.tree.column("DOD", width=100)
        self.tree.column("Bld_grp", width=100)
        self.tree.column("Address", width=100)
        self.tree.column("Location", width=100)
        self.tree.pack(expand=True, fill=tk.BOTH)

        # Get eligible donors data
        eligible_donors = self.get_eligible_donors()

        # Insert eligible donors data into Treeview
        for donor in eligible_donors:
            self.tree.insert("", tk.END, values=donor)

    def get_eligible_donors(self):
        eligible_donors = []

        try:
            con = sqlite3.connect(database=r'ims.db')
            cur = con.cursor()

            # Retrieve donors data from the database including the patient name
            cur.execute("SELECT  d.name, d.email, d.gender, d.contact, d.dob, d.dod, d.Bld_grp, d.address, d.location FROM donor d")
            rows = cur.fetchall()

            # Calculate the eligibility for each donor
            for row in rows:
                dod = datetime.strptime(row[5], "%d/%m/%Y")  # Date of Donation
                next_donation_date = dod + timedelta(days=120)  # Next donation date after 4 months

                if datetime.now() >= next_donation_date:
                    # Exclude ID and display Donor ID instead
                    eligible_donors.append(row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error: {str(ex)}")

        finally:
            con.close()

        return eligible_donors

if __name__ == "__main__":
    root = tk.Tk()
    app = productClass(root)
    root.mainloop()

