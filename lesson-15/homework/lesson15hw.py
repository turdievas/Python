#Review Exercises

import sqlite3
#1
create = """create table roaster 
            (name text, species text,age int)"""
with sqlite3.connect('my_new_db.db') as conn:
    cursor = conn.cursor()
    cursor.execute(create)
#2
import sqlite3
insert  = """insert into roaster values
             ("Benjamin Sisko", 'Human', 40),
             ("Jadzia Dax", 'Trill', 300),
             ("Kira Nerys", 'Bajoran', 29)"""
with sqlite3.connect('my_new_db.db') as conn:
    cursor = conn.cursor()
    cursor.execute(insert)
#3.
import sqlite3
with sqlite3.connect('my_new_db.db') as conn:
    cursor = conn.cursor()
    cursor.execute(
        "update roaster set name=? where species=? and age=?",
        ('Ezri Dax', 'Bajoran', 29))
#4.
import sqlite3
with sqlite3.connect('my_new_db.db') as conn:
    cursor = conn.cursor()
    res = cursor.execute(
        "select * from roaster where species =?",
        ('Bajoran',))
print(res.fetchall())
