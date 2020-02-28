#!/usr/bin/env python3

import sqlite3

from sqlite3 import Error

class Database:
    def __init__(self, path):
        self.connection = None
        try:
            self.connection = sqlite3.connect(path)
            print("[OK] Connected to database.")

        except Error as e:
            print(f"[ERROR] {e}")

            "MUAHAHAHAHAHHAHAHAHAHAHAHAHAH IM HERE!"

    def check(self):
        c = self.connection.cursor()
        res = None
        # Check for table
        try:
            res = c.execute("SELECT * FROM identinet")
        except Error as e:
            print(f"[ERROR] {e}")

        c.close()

        if res == None:
            return False
        return True

    def create_table(self):
        c = self.connection.cursor()
        try:
            c.execute("CREATE TABLE identinet (url text, email text, username text)")
            self.connection.commit()
        except Error as e:
            print(f"[ERROR] {e}")
        c.close()




db = Database('identinet.db')
print("Checking database")
if db.check() == False:
    print("Identinet table not found. Initializing")
db.create_table()

print("(? for help)")
while True:
    inp = input(">")
    if inp == '?':
        print("Help me")
    elif inp == "a":
        url = input("URL: ")
        email = input("Email: ")
        user = input("Username: ")

        c = db.connection.cursor()
        c.execute(f"INSERT INTO identinet(url,email,username) VALUES (?, ?, ?)", (url, email, user))
        db.connection.commit()
        c.close()

    elif inp == 'l':
        c = db.connection.cursor()
        ret = c.execute("SELECT url, email, username FROM identinet")

        print("(URL, Email, User)")
        for r in ret:
            print(r)
        c.close()

    elif inp == 'x':
        break



print("Printing config")
c = db.connection.cursor()
res = None
try:
    res = c.execute("SELECT * FROM identinet")
except Error as e:
        print(f"[ERROR] {e}")
else:

    for r in res:
        print(r)
