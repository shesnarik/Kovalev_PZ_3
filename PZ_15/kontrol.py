import sqlite3 as sq
from data_users import info_users

with sq.connect("org.db") as con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS poruchitel")
    cur.execute("""CREATE TABLE IF NOT EXISTS poruchitel (
        poruchenie_id INTEGER PRIMARY KEY AUTOINCREMENT,
        ispolnit TEXT,
        nazvamie TEXT NOT NULL,
        data_vidach DATETIME DEFAULT 0,
        srok_isp INTEGER DEFAULT 0)""")

with sq.connect("org.db") as con:
    cur = con.cursor()
    cur.executemany("INSERT INTO tourist VALUES (?, ?, ?, ?, ?, ?, ?)", info_users)

with sq.connect("org.db") as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM tourist WHERE Stoim_put > 100000")
    res = cur.fetchall()
    print(res)

with sq.connect("org.db") as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM tourist WHERE Prod_poezd > 10")
    res = cur.fetchall()
    print(res)

with sq.connect("org.db") as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM tourist WHERE Stoim_put < 150000 AND Prod_poezd > 5")
    res = cur.fetchall()
    print(res)


with sq.connect("org.db") as con:
    cur = con.cursor()
    cur.execute("UPDATE tourist SET Stoim_put = Stoim_put+3000 WHERE Region LIKE 'А%'")
    resul = cur.fetchall()


with sq.connect("org.db") as con:
    cur = con.cursor()
    cur.execute("UPDATE tourist SET Stoim_put = Stoim_put-7000 WHERE Region LIKE 'Европа'")
    cur.execute("SELECT * FROM tourist")
    resul = cur.fetchall()
    print(resul)

with sq.connect("org.db") as con:
    cur = con.cursor()
    cur.execute("UPDATE tourist SET Prod_poezd = Prod_poezd+2 WHERE country LIKE 'Т%'")
    resul = cur.fetchall()


with sq.connect("org.db") as con:
    cur = con.cursor()
    cur.execute("DELETE FROM tourist WHERE klient_id = 2")
    resul = cur.fetchall()

with sq.connect("org.db") as con:
    cur = con.cursor()
    cur.execute("DELETE FROM tourist WHERE  famil LIKE 'К%'")
    resul = cur.fetchall()

with sq.connect("org.db") as con:
    cur = con.cursor()
    cur.execute("DELETE FROM tourist WHERE Stoim_put < 100000")
    resul = cur.fetchall()