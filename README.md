# Blood-Links 🩸

**Blood-Links** is a comprehensive **Blood Bank Management System** designed to streamline the management of hospitals, donors, blood products, and billing processes. Built with Python and Tkinter, it provides an easy-to-use interface for administrators to efficiently manage blood bank operations.

---

## Screenshots

> <img width="957" height="539" alt="image" src="https://github.com/user-attachments/assets/97b5e619-ea03-4541-9d16-9ef07ee54099" />
> <img width="825" height="399" alt="image" src="https://github.com/user-attachments/assets/a397d136-bb6a-47b5-ba98-f750021afb26" />
> <img width="826" height="419" alt="image" src="https://github.com/user-attachments/assets/dc3abb15-b6c6-41a3-b04b-c790961299c1" />
> <img width="960" height="540" alt="image" src="https://github.com/user-attachments/assets/76ea8016-1002-477b-a7a3-6882c9c9c576" />
<img width="602" height="401" alt="image" src="https://github.com/user-attachments/assets/f0013af1-5719-4876-b939-27ce212e68c8" />


---
## Demo
Watch this demo video -> https://drive.google.com/file/d/1ThBsLCECEZQ43Arom3PQDCpn9mvv5Zna/view?usp=sharing

---

## Features

- **Hospital Management**: Add, update, delete, and search hospital records with detailed contact and address information.
- **Donor Management**: Maintain donor records and automatically calculate eligibility based on the last donation date.
- **Product & Supplier Management**: Manage blood products and suppliers, including price, quantity, category, and status.
- **Sales & Billing**: Generate, view, and search customer bills; maintain organized invoice records.
- **Reports & Lists**: View scrollable tables of hospitals, donors, products, and eligible donors.

---

## Technologies Used

- Python 3.x  
- Tkinter for GUI  
- SQLite3 for database management  
- Pillow for image handling  

---

## Modules

1. **Hospital Management (`hospital.py`)**
   - Manage hospital details such as invoice number, name, contact, email, location, and address.
   - Features: Add, Update, Delete, Search, and Display hospital records.

2. **Eligible Donors (`product.py`)**
   - Display eligible donors based on donation date.
   - Automatically calculates next eligible donation date (after 4 months).

3. **Sales & Billing (`sales.py`)**
   - View customer bills.
   - Search by invoice number and maintain organized text-based invoice records.

4. **Supplier & Product Management (`supplier.py`)**
   - Add, update, delete, and view supplier and product information.
   - Maintain details such as price, quantity, category, and status.

---

## Setup & Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/blood-links.git
   cd blood-links
   ```

2. **Install dependencies**
   ```bash
   pip install pillow
   ```

3. **Database**
   - Ensure `ims.db` SQLite3 database is present in the project directory.
   - Create the required tables (`hospital`, `donor`, `product`) if not already available.

4. **Run the application**
   ```bash
   python hospital.py   # For hospital management
   python product.py    # For eligible donors
   python sales.py      # For sales/billing
   python supplier.py   # For supplier/product management
   ```

---

## Usage

- Start the app by running dashboard.py.
- Use the GUI to add, update, delete, or search records.
- Scrollable tables and entry forms allow quick navigation and management.
- Customer bills are saved as text files in the `bill/` directory.

---

## Database Structure

**Hospital Table**
| Column | Type |
|--------|------|
| invoice | TEXT PRIMARY KEY |
| name    | TEXT |
| contact | TEXT |
| email   | TEXT |
| location | TEXT |
| address | TEXT |

**Donor Table**
| Column | Type |
|--------|------|
| name   | TEXT |
| email  | TEXT |
| gender | TEXT |
| contact | TEXT |
| dob    | TEXT |
| dod    | TEXT |
| Bld_grp | TEXT |
| address | TEXT |
| location | TEXT |

**Product Table**
| Column | Type |
|--------|------|
| P_Id   | INTEGER PRIMARY KEY AUTOINCREMENT |
| Supplier | TEXT |
| Category | TEXT |
| Name     | TEXT |
| Price    | REAL |
| Qty      | INTEGER |
| Status   | TEXT |

---


