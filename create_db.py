import sqlite3
def create_db():
    con=sqlite3.connect(database=r'ims.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS donor(Do_id INTEGER PRIMARY KEY AUTOINCREMENT ,name text,email text,gender text,contact text,dob text,dod text,Bld_grp text,address text,location text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS hospital(invoice INTEGER PRIMARY KEY AUTOINCREMENT ,name text,contact text,email text,location text,address text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS category (cid INTEGER PRIMARY KEY AUTOINCREMENT,name text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS product(P_Id INTEGER PRIMARY KEY AUTOINCREMENT ,Supplier text,Category text,Name text,Price text,Qty text,Status text)")
    con.commit()

create_db()