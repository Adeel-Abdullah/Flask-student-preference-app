import sqlite3
from sqlite3 import Error

db_filename = r"db.sqlite3"
# SQL DDL script to create tables
try:
    with open('schema.sql','r') as ddl_script:
        ddl = ddl_script.read()
    # Connect to SQLite database
    with sqlite3.connect(db_filename) as db:
    # Create a cursor object
        cs = db.cursor()
    # Execute SQL DDL script to create tables
        cs.executescript(ddl)
    # Commit changes and close connection
        db.commit()
except Error as e:
    print(e)
    db.rollback()




# SQL DML script to insert data
try:
    with open('dataDML.sql','r') as dml_script:
        dml = dml_script.read()
    # Connect to SQLite database
    with sqlite3.connect(db_filename) as db:
    # Create a cursor object
        cs = db.cursor()
    # Execute SQL DML script to insert data
        cs.executescript(dml)
        db.commit()
except Error as e:
    print(e)
    db.rollback()
    

print("Database populated successfully!")

