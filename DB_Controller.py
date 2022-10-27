import sqlite3 as sq
from os import path


class db_Controller:
    def __init__(self, DB_Path):
        if not path.exists(DB_Path):
            self.connection = sq.connect(DB_Path)
            self.db = self.connection.cursor()
            self.db.execute('''CREATE TABLE passwords
                                          (name text UNIQUE , UserName text, pass text, length INTEGER)''')
        else:
            self.connection = sq.connect(DB_Path)
            self.db = self.connection.cursor()

    def Insert(self, name, username, password, length):
        try:
            self.db.execute(
                "INSERT INTO passwords VALUES (?, ?, ?, ?)",
                (name, username, password, length))
            self.connection.commit()
            return True
        except:
            return False

    def SelectItem(self, name):
        try:
            self.db.execute("SELECT * FROM passwords WHERE LOWER(name)=?", (name.lower(),))
            return self.db.fetchall()
        except:
            return list()

    def DeleteItem(self, name):
        if len(self.SelectItem(name)) != 0:
            self.db.execute("DELETE FROM passwords WHERE name=?", (name,))
            self.connection.commit()
            return True
        else:
            return False

    def SelectOnePage(self, pageNumber):
        self.db.execute('SELECT name FROM passwords ORDER BY name LIMIT 10 OFFSET ?', (str(pageNumber * 10),))
        return self.db.fetchall()
