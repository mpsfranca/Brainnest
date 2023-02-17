import os
import sqlite3

PATH = os.path.join(os.getcwd(),"database","todo.db")

class Database:
    def __init__(self):
        self.connection = sqlite3.connect(PATH)
        self.cursor = self.connection.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS todo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT
        )
        """)
        self.connection.commit()

    def get_items(self):
        self.cursor.execute("SELECT * FROM todo")
        return self.cursor.fetchall()

    def print_items(self):
        for item in self.get_items():
            print(f"Id : {item[0]} - Task : {item[1]}")

    def add_todo(self,task):
        self.cursor.execute("INSERT INTO todo (task) VALUES (?)",(task,))
        self.connection.commit()

    def remove_todo(self,id):
        self.cursor.execute("DELETE FROM todo WHERE id=?",(id,))
        self.connection.commit()

        