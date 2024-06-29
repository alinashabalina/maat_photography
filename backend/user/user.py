from flask_login import LoginManager, UserMixin

from init_db import DataBase

login_manager = LoginManager()


class UserDB(DataBase, UserMixin):

    def __init__(self):
        super().__init__()
        self.cur.execute('DROP TABLE IF EXISTS users;')
        self.cur.execute(
            '''CREATE TABLE IF NOT EXISTS users (id serial \
        PRIMARY KEY, username varchar(150), email varchar(256), password_hash varchar, is_admin boolean);''')
        self.conn.commit()

    def add_user(self, email, password):
        self.cur.execute('INSERT INTO users (username, email, password_hash, is_admin)'
                         'VALUES (%s, %s, %s, %s)',
                         ('',
                          email, password, False))
        self.conn.commit()
        self.cur.execute(f"SELECT * FROM users WHERE users.email = '{email}'")
        return self.cur.fetchone()[1]

    def find_user(self, email):
        self.cur.execute(f"SELECT * FROM users WHERE users.email = '{email}'")
        return self.cur.fetchone()

    def find_user_by_id(self, user_id):
        self.cur.execute(f"SELECT * FROM users WHERE users.id = {user_id}")
        return self.cur.fetchone()





