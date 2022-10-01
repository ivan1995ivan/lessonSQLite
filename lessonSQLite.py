import sqlite3

base = sqlite3.connect('new.db')
cur = base.cursor()

base.execute('CREATE TABLE data(login, pasword)')
base.commit()
