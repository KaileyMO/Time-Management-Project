import sqlite3

def add_event(name, time, twilight, date):
    con = sqlite3.connect("sql.db")
    cs = con.cursor()

    cs.execute("INSERT INTO event(name, time, twilight, date) VALUES(?, ?, ?, ?)",
            (name, time, twilight, date))

    con.commit()
    con.close()

def remove_event(id_num):
    con = sqlite3.connect("sql.db")
    cs = con.cursor()

    query = ("DELETE FROM event "
                f"WHERE id = {id_num}")
    cs.execute(query)

    con.commit()
    con.close()

def full_list():
    con = sqlite3.connect("sql.db")
    cs = con.cursor()

    query = (f"SELECT * FROM event")

    cs.execute(query)
    result = cs.fetchall()

    con.close()

    return result

def display_item(month, day, year):
    con = sqlite3.connect("sql.db")
    cs = con.cursor()

    query = (f"SELECT * FROM event WHERE date = '{month}-{day}-{year}'")

    cs.execute(query)
    result = cs.fetchall()

    con.close()

    return result

def get_note():
    con = sqlite3.connect("sql.db")
    cs = con.cursor()

    query = (f"SELECT * FROM page WHERE id = 1")

    cs.execute(query)
    result = cs.fetchall()

    con.close()

    return result

def update_notes(new_body):
    con = sqlite3.connect("sql.db")
    cs = con.cursor()

    query = (f"UPDATE page SET body = '{new_body}' WHERE id = 1")

    cs.execute(query)

    con.commit()
    con.close()

def delete_categories():
    con = sqlite3.connect("sql.db")
    cs = con.cursor()

    query = ("DELETE FROM category")
    cs.execute(query)

    con.commit()
    con.close()

def add_categories(name, price):
    con = sqlite3.connect("sql.db")
    cur = con.cursor()

    cur.execute("INSERT INTO category (name, price) VALUES (?, ?)", (name, price))
    con.commit()

    return cur.lastrowid

def get_categories():
    con = sqlite3.connect("sql.db")
    cs = con.cursor()

    query = (f"SELECT * FROM category")

    cs.execute(query)
    result = cs.fetchall()

    con.close()

    return result

def display(table):
    con = sqlite3.connect("sql.db")
    cs = con.cursor()

    query = (f"SELECT * FROM {table}")

    cs.execute(query)
    result = cs.fetchall()

    con.close()

    print(result)
