import sqlite3

base = sqlite3.connect('new.db')
cur = base.cursor()

# base.execute('CREATE TABLE IF NOT EXISTS {}(login PRIMARY KEY, pasword)'.format('data'))
# base.commit()

# cur.execute('INSERT INTO data VALUES(?, ?)', ('jonny123', '123456789'))
# base.commit()
# cur.execute('INSERT INTO data VALUES(?, ?)', ('billy123', 'password'))
# base.commit()

# r = cur.execute('SELECT login FROM data').fetchall()
# r = cur.execute('SELECT pasword FROM data WHERE login ==?',('jonny123',)).fetchone()
# cur.execute('UPDATE data SET pasword == ? WHERE pasword == ?', ('123456789', 'password'))
# base.commit()
# cur.execute('DELETE FROM data WHERE login == ?', ('jonny123',))
# base.commit()
base.execute('DROP TABLE IF EXISTS data')
base.commit()
base.close()