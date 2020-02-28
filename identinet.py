#!/usr/bin/env python3

import sqlite3
from sqlite3 import Error

#
# Database Handler
#

class Database:
    def __init__(self, path):
        self.connection = None
        try:
            self.connection = sqlite3.connect(path)
            print("[OK] Connected to database.")

        except Error as e:
            print(f"[ERROR] {e}")

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

    def execute(self, query):
        ret = []
        c = self.connection.cursor()
        try:
            res = c.execute(query)
        except Error as e:
            print(f"[ERROR] {e}")
        else:
            for r in res:
                ret.append(r)

        c.close()
        return ret


    def insert(self, query, values):
        c = self.connection.cursor()
        try:
            c.execute(query, values)
            self.connection.commit()
        except Error as e:
            print(f"[ERROR] {e}")

        c.close()



#
# MAIN
#

db = Database('identinet.db')
print("Checking database")
if db.check() == False:
    print("Identinet table not found. Initializing")
    db.create_table()

print("(? for help)")
while True:
    inp = input("> ")
    if inp == '?':
        print("identinet version 1")
        print("a - add Entry")
        print("l - list all Entries")
        print("= - Select Entries")
        print("x - exit")

    elif inp == "a":
        url = input("URL: ")
        email = input("Email: ")
        user = input("Username: ")

        db.insert("INSERT INTO identinet(url,email,username) VALUES (?, ?, ?)", (url, email, user))

    elif inp == 'l':
        ret = db.execute("SELECT url, email, username FROM identinet")

        print("(URL, Email, User)")
        for r in ret:
            print(r)


    elif inp == '=':
        col = input("Column: ")
        val = input("Value: ")

        ret = db.execute(f"SELECT url, email, username FROM identinet WHERE {col} = '{val}'")

        print("(URL, Email, User)")
        for r in ret:
            print(r)
        c.close()

    elif inp == 'x':
        break
