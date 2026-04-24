import sqlite3

con = sqlite3.connect("sql.db")
query = ("CREATE TABLE event ("
                " id integer Primary Key AUTOINCREMENT,"
                " name text,"
                " time int,"
                " twilight text,"
                " date text)")

cs = con.cursor()
cs.execute(query)

query = ("CREATE TABLE page ("
            " id integer Primary Key AUTOINCREMENT,"
            " body text)")
cs.execute(query)
query = ("INSERT INTO page VALUES"
            "(1, 'Write your notes in this text editor...')")
cs.execute(query)

query = ("CREATE TABLE category ("
            " id integer Primary Key AUTOINCREMENT,"
            " name text,"
            " price int)")
cs.execute(query)
query = ("INSERT INTO category VALUES"
            "(1, 'Car Payment', 200),"
            "(2, 'Electricity', 100),"
            "(3, 'Movies', 30)")
cs.execute(query)

con.commit()
con.close()