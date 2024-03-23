# from tkinter import *
# from tkinter import ttk, messagebox
# import sqlite3

# class BloodGroupWindow:
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("1100x500+220+130")
#         self.root.title("Blood Group Information")
        
#         self.total_blood = {
#             "A+": 0,
#             "A-": 0,
#             "B+": 0,
#             "B-": 0,
#             "AB+": 0,
#             "AB-": 0,
#             "O+": 0,
#             "O-": 0
#         }
        
#         self.frame = Frame(self.root, bd=2, relief=RIDGE)
#         self.frame.pack(fill=BOTH, expand=True)

#         self.lbl_title = Label(self.frame, text="Blood Group Information", font=("times new roman", 15, "bold"), bg="white")
#         self.lbl_title.pack(side=TOP, fill=X)
        
#         self.treeview = ttk.Treeview(self.frame, columns=("blood_group", "available_ml"), show="headings", height=8)
#         self.treeview.pack(fill=BOTH, expand=True)
#         self.treeview.heading("blood_group", text="Blood Group")
#         self.treeview.heading("available_ml", text="Available (ml)")

#         self.calculate_blood()
#         self.display_blood_info()

#     def calculate_blood(self):
#         con = sqlite3.connect(database=r'ims.db')
#         cur = con.cursor()

#         try:
#             cur.execute("SELECT gender, Bld_grp FROM donor")
#             rows = cur.fetchall()

#             for row in rows:
#                 gender, blood_group = row
#                 if gender.lower() == "male":
#                     donation_amount = 400
#                 elif gender.lower() == "female":
#                     donation_amount = 350
#                 else:
#                     # handle other genders if needed
#                     continue

#                 self.total_blood[blood_group] += donation_amount

#         except Exception as ex:
#             messagebox.showerror("Error", f"Error calculating blood: {str(ex)}", parent=self.root)

#     def display_blood_info(self):
#         for blood_group, total_ml in self.total_blood.items():
#             self.treeview.insert("", END, values=(blood_group, total_ml))


# if __name__ == "__main__":
#     root = Tk()
#     app = BloodGroupWindow(root)
#     root.mainloop()

# from tkinter import *

# class BloodGroupWindow:
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("1100x500+220+130")
#         self.root.title("Blood Group Information")

#         self.total_blood = {
#             "A+": 0,
#             "A-": 0,
#             "B+": 0,
#             "B-": 0,
#             "AB+": 0,
#             "AB-": 0,
#             "O+": 0,
#             "O-": 0
#         }

#         self.frame = Frame(self.root, bd=2, relief=RIDGE)
#         self.frame.pack(fill=BOTH, expand=True, padx=20, pady=20)  # Added padding to center the frame

#         self.lbl_title = Label(self.frame, text="Blood Group Data", font=("Arial", 24, "bold"), bg="white")
#         self.lbl_title.grid(row=0, column=0, columnspan=4, pady=(0, 20))  # Span title label across all columns

#         # Create labels for each blood group
#         self.create_blood_group_labels()

#         # Center the frame in the window
#         self.center_window()

#     def create_blood_group_labels(self):
#         # Labels for each blood group
#         self.lbl_Apos = Label(self.frame, text="Total A+ (ml)\n[ 0 ]", bd=5, relief=RIDGE, bg="#FF5733", fg="white",
#                               font=("goudy old style", 20, "bold"))
#         self.lbl_Apos.place(x=50, y=90, height=150, width=200)

#         self.lbl_Aneg = Label(self.frame, text="Total A- (ml)\n[ 0 ]", bd=5, relief=RIDGE, bg="#FFCCCB", fg="white",
#                               font=("goudy old style", 20, "bold"))
#         self.lbl_Aneg.place(x=300, y=90, height=150, width=200)

#         self.lbl_Bpos = Label(self.frame, text="Total B+ (ml)\n[ 0 ]", bd=5, relief=RIDGE, bg="#3385FF", fg="white",
#                               font=("goudy old style", 20, "bold"))
#         self.lbl_Bpos.place(x=550, y=90, height=150, width=200)

#         self.lbl_Bneg = Label(self.frame, text="Total B- (ml)\n[ 0 ]", bd=5, relief=RIDGE, bg="#7FB3D5", fg="white",
#                               font=("goudy old style", 20, "bold"))
#         self.lbl_Bneg.place(x=800, y=90, height=150, width=200)

#         self.lbl_ABpos = Label(self.frame, text="Total AB+ (ml)\n[ 0 ]", bd=5, relief=RIDGE, bg="#C0C0C0", fg="white",
#                                font=("goudy old style", 20, "bold"))
#         self.lbl_ABpos.place(x=50, y=250, height=150, width=200)

#         self.lbl_ABneg = Label(self.frame, text="Total AB- (ml)\n[ 0 ]", bd=5, relief=RIDGE, bg="#7F8C8D", fg="white",
#                                font=("goudy old style", 20, "bold"))
#         self.lbl_ABneg.place(x=300, y=250, height=150, width=200)

#         self.lbl_Opos = Label(self.frame, text="Total O+ (ml)\n[ 0 ]", bd=5, relief=RIDGE, bg="#FFCC99", fg="white",
#                               font=("goudy old style", 20, "bold"))
#         self.lbl_Opos.place(x=550, y=250, height=150, width=200)

#         self.lbl_Oneg = Label(self.frame, text="Total O- (ml)\n[ 0 ]", bd=5, relief=RIDGE, bg="#D35400", fg="white",
#                               font=("goudy old style", 20, "bold"))
#         self.lbl_Oneg.place(x=800, y=250, height=150, width=200)

#     def center_window(self):
#         # Get the screen width and height
#         screen_width = self.root.winfo_screenwidth()
#         screen_height = self.root.winfo_screenheight()

#         # Calculate x and y coordinates to center the window
#         x = (screen_width - 1100) // 2
#         y = (screen_height - 500) // 2

#         # Set the window position
#         #self.root.geometry(f"1100x500+{x}+{y}")

#         title_width = self.root.winfo_reqwidth()
#         self.root.title(" " * ((1100 - title_width) // 12) + "Blood Group Data")

# if __name__ == "__main__":
#     root = Tk()
#     app = BloodGroupWindow(root)
#     root.mainloop()

from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

class BloodGroupWindow:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Blood Group Information")

        self.total_blood = {
            "A+": 0,
            "A-": 0,
            "B+": 0,
            "B-": 0,
            "AB+": 0,
            "AB-": 0,
            "O+": 0,
            "O-": 0
        }

        self.frame = Frame(self.root, bd=2, relief=RIDGE)
        self.frame.pack(fill=BOTH, expand=True, padx=20, pady=20)  # Added padding to center the frame

        self.lbl_title = Label(self.frame, text="Blood Group Data", font=("Arial", 24, "bold"), bg="white")
        self.lbl_title.grid(row=0, column=0, columnspan=4, pady=(0, 20))  # Span title label across all columns

        # Create labels for each blood group
        self.create_blood_group_labels()

        # Call the method to calculate blood and update labels
        self.calculate_blood()
        self.update_labels()

        # Center the frame in the window
        self.center_window()

    def calculate_blood(self):
        # Simulating the database query to calculate blood
        # Here we just manually set some values for demonstration
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()

        try:
            cur.execute("SELECT gender, Bld_grp FROM donor")
            rows = cur.fetchall()

            for row in rows:
                gender, blood_group = row
                if gender.lower() == "male":
                    donation_amount = 400
                elif gender.lower() == "female":
                    donation_amount = 350
                else:
                    # handle other genders if needed
                    continue
    
                self.total_blood[blood_group] += donation_amount
        except Exception as ex:
            messagebox.showerror("Error", f"Error calculating blood: {str(ex)}", parent=self.root)

        

    def create_blood_group_labels(self):
        # Labels for each blood group
        self.labels = {}
        positions = [(50, 90), (300, 90), (550, 90), (800, 90), (50, 250), (300, 250), (550, 250), (800, 250)]
        colors = ["#FF5733", "#FFCCCB", "#3385FF", "#7FB3D5", "#C0C0C0", "#7F8C8D", "#FFCC99", "#D35400"]
        for blood_group, position, color in zip(self.total_blood.keys(), positions, colors):
            label = Label(self.frame, text=f"Total {blood_group} (ml)\n[ {self.total_blood[blood_group]} ]",
                          bd=5, relief=RIDGE, bg=color, fg="white", font=("goudy old style", 20, "bold"))
            label.place(x=position[0], y=position[1], height=150, width=200)
            self.labels[blood_group] = label

    def update_labels(self):
        # Update labels with calculated blood data
        for blood_group, label in self.labels.items():
            label.config(text=f"Total {blood_group} (ml)\n[ {self.total_blood[blood_group]} ]")

    def center_window(self):
        # Get the screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calculate x and y coordinates to center the window
        x = (screen_width - 1100) // 2
        y = (screen_height - 500) // 2

        # Set the window position
        #self.root.geometry(f"1100x500+{x}+{y}")

        title_width = self.root.winfo_reqwidth()
        self.root.title(" " * ((1100 - title_width) // 12) + "Blood Group Data")

if __name__ == "__main__":
    root = Tk()
    app = BloodGroupWindow(root)
    root.mainloop()


