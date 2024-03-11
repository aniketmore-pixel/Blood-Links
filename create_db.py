import sqlite3
def create_db():
    con=sqlite3.connect(database=r'ims.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS donor(Do_id INTEGER PRIMARY KEY AUTOINCREMENT ,name text,email text,gender text,contact text,dob text,dod text,Bld_grp text,address text,location text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS hospital(invoice INTEGER PRIMARY KEY AUTOINCREMENT ,name text,contact text,email text,location text,address text)")
    con.commit()


create_db()